from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
import logging
import re
from tkinter import Tk
import keyboard
import pwinput
import Main



s = Service('./WorkScript/chromedriver.exe')                                                              

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


def Pups():
   cliptext = Main.Link_entry.get()
   Link_Start = "https://"
   Pack_Delition_sublink = "/tools/unknown_pack_removal"
   Pups_Link = cliptext[2]
   Full_link = Link_Start + Pups_Link + Pack_Delition_sublink
   print(Full_link)
   driver.get(Full_link) 
 
def Pack_Find():
   driver.find_element(By.ID, 'identity').send_keys(Main.email)#Ввод логина
   driver.find_element(By.ID, 'credential').send_keys(Main.password)#Ввод пароля
   driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)#Авторизация

def Pack_Delete():
   for Pack in re.split('[";|,|:|\n|\\| "]',Packlist= Main.Pack_entry): 
      if Pack != '': 
         print(Pack)
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, "jq-remove-pack-button").send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            print(Pack + " удален")
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            print(Pack + " не удален ")
            file_object = open('Паки.txt', 'a')
            file_object.write(Pack + " не удален",)
            file_object.write("\n")
            file_object.close()      
            driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
            driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
            driver.find_element(By.CLASS_NAME, "form-control").clear()