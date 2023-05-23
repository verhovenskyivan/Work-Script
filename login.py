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
import keyboard
import pwinput


s = Service('./workscript-main/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")

driver = webdriver.Chrome(options = options, service=Service(ChromeDriverManager().install()))
       
def Pups(linkd, email, password, sublink):
   link = linkd.split('/')
   Link_Start = "https://"
   Pack_Delition_sublink = sublink
   Pups_Link = link[2]
   Full_link = Link_Start + Pups_Link + Pack_Delition_sublink
   print(Full_link)
   driver.get(Full_link) 
   print(email)
   print(password)
   driver.find_element(By.ID, 'identity').send_keys(email)#Ввод логина
   driver.find_element(By.ID, 'credential').send_keys(password)#Ввод пароля
   driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)#Авторизация