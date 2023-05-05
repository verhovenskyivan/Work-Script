from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time, sys, os, subprocess

s = Service('./WorkScript/chromedriver.exe')                                                              

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

with open('Config.txt','r') as file:
   for details in file:
      email, password  = details.split(',')
        
with open('Link.txt','r') as f:
      link  = f.readline()

Pack = input ("Enter pack: ").split(", | \n")
Pack_List = [Pack]

driver.get(link)

def Pack_Find():
   driver.find_element(By.ID, 'identity').send_keys(email)
   driver.find_element(By.ID, 'credential').send_keys(password)
   driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)
 
def Pack_Delete():
   driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
   driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
   try:
      driver.find_element(By.CLASS_NAME, "jq-remove-pack-button").send_keys(Keys.ENTER)
      driver.switch_to.alert.accept()
   except NoSuchElementException:
      driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
      driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
 
Pack_Find()
Pack_Delete()
time.sleep(1)
subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])


 



