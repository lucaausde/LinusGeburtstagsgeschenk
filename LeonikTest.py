from selenium import webdriver
import time
from datetime import datetime
import pyautogui

# get current date
now = datetime.now()

# set the date and time format
date_format = "%m-%d-%Y %H:%M:%S"

# convert string to actual date and time
time1 = datetime.strptime(now.strftime('%m-%d-%Y %H:%M:%S'), date_format)
time2 = datetime.strptime('8-14-2019 00:00:01', date_format)

diff = time2 - time1

print(str(diff.seconds))


browser = webdriver.Chrome('chromedriver')

browser.get('https://web.whatsapp.com/')
time.sleep(5)
do = browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]')
do.click()
#time.sleep(diff.seconds)
do = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
do.send_keys('Hallo Leo. Dies ist eine automatisierte Nachricht. So ganz nebenbei: Linus hat in ' + str(diff.seconds) + " Sekunden Geburtstag :)")
pyautogui.press('enter')
#time.sleep(3)
#browser.quit()
