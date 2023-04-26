from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
import os
import UI
import Secret

s = Service('./WorkScript/chromedriver.exe')                                                              


from getpass import getpass

email = input("Enter email: ")
password = getpass("Enter password: ")
link = input("Enter link: ")
Pack = input("Enter pack: ")


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
   
driver.get(link)
driver.find_element(By.ID, 'identity').send_keys(email)
driver.find_element(By.ID, 'credential').send_keys(password)
driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)
driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
driver.find_element(By.CLASS_NAME, "jq-remove-pack-button").send_keys(Keys.ENTER)
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()
