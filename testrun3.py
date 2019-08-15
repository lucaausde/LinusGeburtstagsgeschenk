import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service('chromedriver')
service.start()

driver = webdriver.Remote(service.service_url)
driver.get('http://www.google.com/xhtml');
time.sleep(5)

driver.quit()