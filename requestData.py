import requests
import setValues
import time

# 서버의 IP 주소와 포트
BASE_URL = 'http://154.90.62.39:5000'

def save_wait_times_to_file(waitTimes):
    try:
        with open('waitTimes.txt', 'w', encoding='utf-8') as f:
            f.write("\n# waitTimes\n")
            for key, (min_value, max_value) in waitTimes.items():
                f.write(f"{key}:{min_value}~{max_value}\n")
        print("Wait times saved to waitTimes.txt")
    except Exception as e:
        print(f"Error saving wait times to file: {e}")

def save_product_data(product_data):
    file_path = 'product_list.txt'
    
    with open(file_path, 'w', encoding='utf-8') as file:
        total = 0
        for item in product_data:
            accessNum = int(item[-1])
            quotient = accessNum // 500
            total += accessNum
            line = f'{quotient*setValues.windowCount},{quotient},' + ','.join(map(str, item))
            file.write(line + '\n')
        file.write(str(total))

def save_proxy_ips(proxy_ips):
    file_path = 'hiPaiIp.txt'

    with open(file_path, 'w', encoding='utf-8') as file:
        for ip in proxy_ips:
            file.write(ip + '\n')

def save_id(id_data):
    try:
        with open('id.txt', 'w', encoding='utf-8') as file:
            for item in id_data:
                file.write(f"{item['id']},{item['password']}\n")
        print("ID data saved to id.txt")
    except Exception as e:
        print(f"Error saving ID data: {e}")

def get_product():
    max_retries = 3
    for attempt in range(max_retries):
        try:
            params = {'amount': setValues.targetCount, 'unit': setValues.unit}
            response = requests.get(f'{BASE_URL}/get_product', params=params, timeout=10)
            if response.status_code == 200:
                product_data = response.json().get('data', [])
                waitTimes = response.json().get('waitTimes', {})  # waitTimes 값 가져오기
                save_product_data(product_data)
                print(f"Product data retrieved and saved: {product_data}")
                save_wait_times_to_file(waitTimes)
                return
            else:
                print(f"Failed to retrieve product data: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error in get_product (attempt {attempt + 1}): {e}")
            time.sleep(3)
    print("Max retries reached for get_product")

def get_ip():
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(f'{BASE_URL}/get_ip', timeout=10)
            if response.status_code == 200:
                proxy_ips = response.json().get('proxies', [])
                save_proxy_ips(proxy_ips)
                print(f"Proxy IPs retrieved and saved: {proxy_ips}")
                return
            else:
                print(f"Failed to retrieve proxy IPs: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error in get_ip (attempt {attempt + 1}): {e}")
            time.sleep(3)
    print("Max retries reached for get_ip")

def get_id():
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(f'{BASE_URL}/get_id', timeout=10)
            if response.status_code == 200:
                id_data = response.json().get('id_data', [])
                save_id(id_data)
                print(f"ID retrieved and saved: {id_data}")
                return
            else:
                print(f"Failed to retrieve ID: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error in get_ip (attempt {attempt + 1}): {e}")
            time.sleep(3)
    print("Max retries reached for get_id")