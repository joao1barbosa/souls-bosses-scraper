from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://darksouls.wiki.fextralife.com/Bosses'


webdriver = webdriver.Chrome()
webdriver.get(url)

webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

page_source = webdriver.page_source
soup = BeautifulSoup(page_source, 'lxml')
webdriver.quit()

boss_names = []

boss_cards = soup.find_all('h3', class_='col-sm-4')

for boss in boss_cards:
    boss_names.append(boss.text.strip())

print(boss_names)

# a_tags = soup.find_all('a', class_='wiki_link')

# # Append the text content of each tag to the list
# for tag in a_tags:
#     boss_names.append(tag.text.strip())

# # Print the collected names
# for boss_name in boss_names:
#     print(boss_name)