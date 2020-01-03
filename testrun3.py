import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service('chromedriver')
service.start()

driver = webdriver.Remote(service.service_url)
driver.get('https://www.ecosia.org');
time.sleep(5)

driver.quit()
