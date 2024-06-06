from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import os.path

boss_data = []
csv_file = 'bosses.csv'
file_exists = os.path.isfile(csv_file)

def scraping(url, dlc):
    driver = webdriver.Chrome()  
    driver.get(url)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    driver.quit()

    boss_cards = soup.find_all('h3', class_='col-sm-4')

    for boss in boss_cards:
        boss_name = boss.text.strip()
        is_optional = boss_name.endswith('*')
        boss_name = boss_name.rstrip('*').strip()
        boss_data.append([boss_name,'ds1', None, dlc, is_optional])
 
url_base = 'https://darksouls.wiki.fextralife.com/'

scraping(url_base + "Bosses", False)
scraping(url_base + "Expansion+Bosses", True)

with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(['name', 'game','picture', 'dlc', 'optional'])
    writer.writerows(boss_data)

print(f"Data has been appended to {csv_file}")