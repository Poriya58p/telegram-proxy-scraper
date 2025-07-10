import requests
from bs4 import BeautifulSoup
import re
import random
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# تنظیم لاگینگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# لیست User-Agentها
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def fetch_proxies_from_text_urls(urls):
    all_links = []
    headers = {'User-Agent': get_random_user_agent()}
    
    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            lines = response.text.splitlines()
            links = [line.strip() for line in lines if re.match(r'^tg://proxy\?server=.+&port=\d+&secret=.+$', line.strip())]
            all_links.extend(links)
            logging.info(f"Fetched {len(links)} proxies from {url}")
        except requests.RequestException as e:
            logging.error(f"HTTP error fetching {url}: {e}")
        time.sleep(random.uniform(1, 3))
    return all_links

def fetch_proxies_from_telegram_channel(url):
    proxies = []
    options = Options()
    options.add_argument('--headless')  # اجرای بدون رابط گرافیکی
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent={get_random_user_agent()}')
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(5)  # منتظر بارگذاری صفحه
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        proxy_elements = soup.find_all('a', href=re.compile(r'^tg://proxy\?server=.+&port=\d+&secret=.+$'))
        proxies = [element.get('href') for element in proxy_elements]
        logging.info(f"Fetched {len(proxies)} proxies from {url}")
    except Exception as e:
        logging.error(f"Error fetching data from {url}: {e}")
    finally:
        driver.quit()
    time.sleep(random.uniform(2, 5))
    return proxies

def save_proxies_to_file(proxy_list, filename='proxy.txt'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for proxy in proxy_list:
                file.write(proxy + '\n')
        logging.info(f"Saved {len(proxy_list)} proxies to {filename}")
    except IOError as e:
        logging.error(f"Error writing to {filename}: {e}")

if __name__ == "__main__":
    text_urls = [
        "https://raw.githubusercontent.com/MahsaNetConfigTopic/proxy/main/proxies.txt",
        # URLهای دیگر را اینجا اضافه کنید
    ]
    
    telegram_urls = [
        "https://t.me/s/iporoto",
        "https://t.me/s/HiProxy",
        "https://t.me/s/iproxy",
        "https://t.me/s/iRoProxy",
        "https://t.me/s/proxyforopeta",
        "https://t.me/s/IRN_Proxy",
        "https://t.me/s/MProxy_ir",
        "https://t.me/s/ProxyHagh",
        "https://t.me/s/PyroProxy",
        "https://t.me/s/ProxyMTProto",
        "https://t.me/s/MTPro_XYZ",
        "https://t.me/s/vpns",
        "https://t.me/s/mtmvpn"
    ]
    
    # جمع‌آوری پروکسی‌ها از منابع متنی
    text_proxies = fetch_proxies_from_text_urls(text_urls)
    
    # جمع‌آوری پروکسی‌ها از کانال‌های تلگرام
    telegram_proxies = []
    for url in telegram_urls:
        proxies = fetch_proxies_from_telegram_channel(url)
        telegram_proxies.extend(proxies)
    
    # ترکیب و حذف پروکسی‌های تکراری
    all_proxies = list(set(text_proxies + telegram_proxies))
    
    # ذخیره پروکسی‌ها
    save_proxies_to_file(all_proxies)
