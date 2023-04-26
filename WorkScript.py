from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import UI
import Secret

s = Service('./WorkScript/chromedriver.exe')                                                              

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

def login_pups(self,username : str, password : str):
    self.add_input(by=By.ID, value ='identity', text = username)
    self.add_input(by=By.ID, value ='credential', text = password)
    self.click_button(by=By.CLASS_NAME, value= 'btn btn-primary')

driver.get(Secret.link)
driver.find_element(By.ID, 'identity').send_keys(Secret.email)
driver.find_element(By.ID, 'credential').send_keys(Secret.password)
driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)
driver.find_element(By.CLASS_NAME, "form-control").send_keys(Secret.Pack)
driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
driver.find_element(By.CLASS_NAME, "jq-remove-pack-button").send_keys(Keys.ENTER)


