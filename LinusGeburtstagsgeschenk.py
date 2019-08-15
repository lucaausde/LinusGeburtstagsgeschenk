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
time.sleep(10)
do = browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]')
do.click()

time.sleep(diff.seconds)

do = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
do.send_keys('Hallo Linus, über die nächste Zeit werden etliche Nachrichten von einem selbstgeschriebenem Programm geschickt. Ich wünsche dir einen ...')
pyautogui.press('enter')

# Declare array holding tons of translations of "happy birthday"

happy_birthday = ["wunderbaren Geburtstag!", "a happy birthday! - Englisch", "հիանալի ծննդյան օր! - Armenisch (lol)", "un magnifique anniversaire! - Französisch", "in prachtige jierdei! - Friesisch", "ένα θαυμάσιο γενέθλιο! - Griechisch (Für den Philosophen des Jahrhunderts)", "lā hānau maikaʻi! - Hawaiianisch", "멋진 생일 - Koreanisch", "un maravilloso cumpleaños! - Spanisch", "wspaniałe urodziny! - Polnisch", "прекрасный день рождения! UND NATÜRLICH RUSSISCH"]

for xhappy in happy_birthday:
    find_path = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
    find_path.send_keys(xhappy)
    pyautogui.press('enter')
    time.sleep(600)

#time.sleep(3)
#browser.quit()
