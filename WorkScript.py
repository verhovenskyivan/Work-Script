from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time, sys, os, subprocess, logging
import re 
from tkinter import Tk

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

Packlist = input ("Enter pack: ")

win = Tk()

cliptext = win.clipboard_get().split('/')
Link_Start = "https://"
Pack_Delition_sublink = "/tools/unknownpackremoval"
Pups_Link = cliptext[2]
Full_link = Link_Start + Pups_Link + Pack_Delition_sublink
for link in cliptext.split('/'):
   print(Full_link)

driver.get(Full_link)

def Pack_Find():
   driver.find_element(By.ID, 'identity').send_keys(email)#Ввод логина
   driver.find_element(By.ID, 'credential').send_keys(password)#Ввод пароля
   driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)#Авторизация

def Pack_Delete():
     for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
       if Pack != '': 
         print(Pack)
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, "jq-remove-pack-button").send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            print(Pack + "Пак удален")
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            print(Pack + "Пак не удален")
            driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
            driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
            driver.find_element(By.CLASS_NAME, "form-control").clear()

Pack_Find()
Pack_Delete()
time.sleep(1)
subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

logging.info("INFO")
logging.warning("WARNING")
logging.basicConfig(level=logging.WARNING, filename="Logger.log",filemode="a",
                   format="%(asctime)s %(levelname)s %(message)s")
logging.error("Error", exc_info=True)
