from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path=os.popen('which chromedriver').read().strip())

driver.get('https://www.amazon.com')

#  close the particular tab
driver.close()

#  quit the entire browser
driver.quit()

