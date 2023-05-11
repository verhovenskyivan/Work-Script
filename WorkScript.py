from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time, sys, os, subprocess, logging

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

Pack_List = [input ("Enter pack: ").split(",")]
Pack = 0
while Pack < len(Pack_List):
   Pack_List[Pack]
   Pack+=1
   if Pack >= len(Pack_List):
      break

driver.get(link)

def Pack_Find():
   driver.find_element(By.ID, 'identity').send_keys(email)#Ввод логина
   driver.find_element(By.ID, 'credential').send_keys(password)#Ввод пароля
   driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)#Авторизация

def Pack_Delete():
     while Pack < len(Pack_List):
      Pack_List[Pack]
      Pack+=1
      if Pack >= len(Pack_List):
       break
     driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
     driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)#Нажатие кнопки поиск
     try:
      driver.find_element(By.CLASS_NAME, "jq-remove-pack-button").send_keys(Keys.ENTER)#Нажатие кнопки удаление
      driver.switch_to.alert.accept()#Свич на алерт и его принятие     
     except NoSuchElementException:#Обработка ошибки
       driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
       driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
       
Pack_Find()
Pack_Delete()
time.sleep(1)
subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

logging.info("INFO")
logging.warning("WARNING")
logging.basicConfig(level=logging.WARNING, filename="Logger.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.error("Error", exc_info=True)
