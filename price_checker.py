import time
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

flight_link = "https://www.kiwi.com/en/search/results/city-of-brussels-belgium/tirana-albania/2021-12-21/no-return"
chrome_options = webdriver.ChromeOptions()
# no headless because the website recognizes its a bot
chrome_options.add_argument('window-size=10x10')
driver = webdriver.Chrome('chromedriver', options=chrome_options)
# fake normal navigation from home page to flight instead directly to flights link + wait time
driver.get("https://www.kiwi.com")
# small window instead
driver.set_window_size(10, 10)
time.sleep(3)
# go to flight's link, you can find your own at kiwi.com
driver.get(flight_link)
# wait 15 secs to load all matches of flights
time.sleep(15)
# find price location using xpath and save into variable
price = driver.find_element(By.XPATH, "//*[@id='SearchView']/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div/strong/span").text
# close the driver
driver.quit()
# get current date and time
now = datetime.now()
date_today = now.strftime("%d/%m/%y %H:%M")

# send it via sms to your phone number(add prefix ex +034) including time date + price
resp = requests.post('https://textbelt.com/text', {
  'phone': '+yournumberhere',
  'message': date_today + '\nWizzAir flight Brussels - Tirana 21 dec \n Price : ' + price,
  'key': 'textbelt',
})
resp.cookies.clear()
# clear cookies
print(resp.json())
# prints success if sent
