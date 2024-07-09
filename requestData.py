import requests, time, os

# 서버의 IP 주소와 포트
BASE_URL = 'http://154.90.62.39:5000'

def save_product_data(product_data):
    try:
        file_path = 'product_list.txt'

        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())
        
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in product_data:
                line = ','.join(map(str, item))
                file.write(line + '\n')
    except:
        time.sleep(3)
        save_product_data(product_data)

def save_proxy_ips(proxy_ips):
    try:
        with open('hiPaiIp.txt', 'w', encoding='utf-8') as file:
            for ip in proxy_ips:
                file.write(ip + '\n')
    except:
        time.sleep(3)
        save_proxy_ips(proxy_ips)

def get_product():
    response = requests.get(f'{BASE_URL}/get_product')
    if response.status_code == 200:
        product_data = response.json().get('data', [])
        save_product_data(product_data)
    else:
        print(f"Failed to retrieve product data: {response.status_code}")

def get_ip():
    response = requests.get(f'{BASE_URL}/get_ip')
    if response.status_code == 200:
        proxy_ips = response.json().get('proxies', [])
        save_proxy_ips(proxy_ips)
    else:
        print(f"Failed to retrieve proxy IPs: {response.status_code}")