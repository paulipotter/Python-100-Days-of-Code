from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome(executable_path=os.popen('which chromedriver').read().strip())

driver.get('https://www.amazon.com/Anker-Charger-Compact-Foldable-MacBook/dp/B09C5RG6KV/ref=sr_1_3?crid=3N2R8UKFMOL52&keywords=anker&qid=1653524021&sprefix=ank%2Caps%2C213&sr=8-3')
price = driver.find_element(by=By.CLASS_NAME, value="a-section a-spacing-micro")
print(price)
#  close the particular tab
driver.close()

#  quit the entire browser
#driver.quit()
