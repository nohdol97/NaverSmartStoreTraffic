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
        for item in product_data:
            accessNum = int(item[-1])
            quotient = accessNum // 500
            # 앞에 두 개의 같은 값을 추가
            line = f'{quotient},{quotient},' + ','.join(map(str, item))
            file.write(line + '\n')

def save_proxy_ips(proxy_ips):
    file_path = 'hiPaiIp.txt'

    with open(file_path, 'w', encoding='utf-8') as file:
        for ip in proxy_ips:
            file.write(ip + '\n')

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