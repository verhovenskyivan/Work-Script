from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from multiprocessing import Process
from win10toast import ToastNotifier
import time, sys, os, Secret, re, array,itertools, re
from alive_progress import alive_bar

s = Service('./WorkScript/chromedriver.exe')                                                              

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

toast = ToastNotifier()
toast.show_toast("Process started")

with open('Config.txt','r') as file:
   for details in file:
      email, password  = details.split(',')
        
with open('Link.txt','r') as f:
      link  = f.readline()

Pack = input("Enter pack: ")

def Get_Link():
   driver.get(link)

def User():
   driver.find_element(By.ID, 'identity').send_keys(email)
   driver.find_element(By.ID, 'credential').send_keys(password)

def Pack_Find():
   driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)
   driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
 
def Pack_Delete():
   driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
   driver.find_element(By.CLASS_NAME, "jq-remove-pack-button").send_keys(Keys.ENTER)
   driver.switch_to.alert.accept()
   
def Script_First_Part():
   Get_Link()
   User()

def Script_Second_Part():
   Pack_Find()
   Pack_Delete()
   time.sleep(1)
   driver.close()

Script_First_Part()
Script_Second_Part()

while driver.close:
   toast.show_toast(Pack,"Process finished")

while True:
   Script_Second_Part()

     
