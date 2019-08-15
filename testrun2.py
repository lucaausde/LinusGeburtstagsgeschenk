from selenium import webdriver

browser = webdriver.Chrome('/Users/Privat/Downloads/chromedriver')

browser.get('https://web.whatsapp.com/')
do = browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]')
do.click()
do = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]')
do.send_keys('Hallo')
do = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
do.click()
#time.sleep(3)
#browser.quit()