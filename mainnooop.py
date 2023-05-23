from tkinter import *
from tkinter.ttk import *
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
#from login import Pups
#from funcbu import Pack_Nedopostavka, Pack_Delete, Pack_DV
import threading
import tkinter as tk
from selenium.common.exceptions import WebDriverException


s = Service('./workscript-main/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")

driver = webdriver.Chrome(options = options, service=Service(ChromeDriverManager().install()))

def Pups(linkd, email, password, sublink):
   link = linkd.split('/')
   Link_Start = 'https://'
   Pack_Delition_sublink = sublink
   Pups_Link = link[2]
   Full_link = Link_Start + Pups_Link + Pack_Delition_sublink
   print(Full_link) 
   try:
    driver.get(Full_link) 
   except WebDriverException:
    print("page down")
   driver.find_element(By.ID, 'identity').send_keys(email)#Ввод логина
   driver.find_element(By.ID, 'credential').send_keys(password)#Ввод пароля
   driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)#Авторизация

def Pack_Otkaz(Packlist, link, email, password, korob): 
   sublink = '/tools/move_objects_to_rejectbox'
   Pups(link, email, password, sublink, korob)
   for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
        if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.CLASS_NAME, "btn btn-secondary").send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, "parent-barcode").send_keys(korob)#Нажатие кнопки удаление
            driver.find_element(By.CLASS_NAME, "btn-default").send_keys(Keys.ENTER)
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            print(Pack + " Перемещен в зону ДВ")
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            driver.get("/containers/all")
            driver.find_element(By.ID, "input-search").send_keys(Pack)
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            value = driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr[2]/td[6]').text
            print(Pack + "имеет статус: " + value)
            Pups()
            driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
            driver.find_element(By.CLASS_NAME, "btn-default").send_keys(Keys.ENTER)
            driver.find_element(By.CLASS_NAME, "form-control").clear()


def Pack_Delete(Packlist, link, email, password):
   sublink = '/tools/unknown_pack_removal'
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
      if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, "jq-remove-pack-button").send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            print(Pack + " удален")
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            driver.get("/containers/all")
            driver.find_element(By.ID, "input-search").send_keys(Pack)
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            value = driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr[2]/td[6]').text
            print(Pack + "имеет статус: " + value)
            Pups()
            driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
            driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
            driver.find_element(By.CLASS_NAME, "form-control").clear()

def Pack_DV(Packlist, link, email, password): 
   sublink = '/tools/move_pack_to_clearance_zone'
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
        if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.CLASS_NAME, "btn-default").send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, "btn-default").send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            print(Pack + " Перемещен в зону ДВ")
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            driver.get("/containers/all")
            driver.find_element(By.ID, "input-search").send_keys(Pack)
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            value = driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr[2]/td[6]').text
            print(Pack + "имеет статус: " + value)
            Pups()
            print(Pack + " Не перемещен в зону ДВ")
            driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
            driver.find_element(By.CLASS_NAME, "btn-default").send_keys(Keys.ENTER)
            driver.find_element(By.CLASS_NAME, "form-control").clear()
          
def Pack_Nedopostavka(Packlist, link, email, password):
   sublink = '/tools/mark_pack_missing'
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]', Packlist): 
      if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, "jq-mark-pack-missing-button").send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            print(Pack + " помечен недопоставкой")
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            driver.get("/containers/all")
            driver.find_element(By.ID, "input-search").send_keys(Pack)
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            value = driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr[2]/td[6]').text
            print(Pack + "имеет статус: " + value)
            Pups()
            driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            driver.find_element(By.CLASS_NAME, "form-control").clear()

def packstatus(Packlist, link, email, password):
   sublink = '/containers/all/'
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]', Packlist):
    try:
     driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
     driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
     status = driver.find_element(By.CLASS_NAME, "cell-status") 
     quant = driver.find_element(By.CLASS_NAME, "cell-itemQuantity")
     #status = driver.find_element_by_class_name("cell-status")
     #quant = driver.find_element_by_class_name("cell-itemQuantity")
     print(status)
     print(quant)
    except NoSuchElementException:#Обработка ошибки
            print(link)

root = tk.Tk()
root.title("FirstLine Helper")
root.geometry("300x400")

first_frame = tk.Frame(root, width=200, height=400)
first_frame.grid(row= 0, column= 0, padx=5, pady=5)

style = Style()
style.map('TButton', foreground = ([('active', 'black')]))                    
style.configure("TButton", font=("Arial", 10),bold=True, borderwidth=2)

def clear():
    packs_entry.delete(0, END)
    packs_entry.insert(0, "Введи паки")
    Link_entry.delete(0, END)
    Link_entry.insert(0, "Введи ссылку")


tk.Label(first_frame, text="EXPRESS_PUPS", relief=RAISED).grid(row=0, column=0, padx=100, pady=3)

tk.Label(text="Логин").grid(row=1, column=0, padx=5, pady=3)
login_entry = tk.Entry(root, width=20)
login_entry.grid(row=2, column=0, padx=0, pady=5)

tk.Label(text="Пароль").grid(row=3, column=0, padx=5, pady=3)
pass_entry = tk.Entry(root, show="*", width=20)
pass_entry.grid(row=4, column=0, padx=0, pady=5)

Link_entry = tk.Entry(root, width=40)
Link_entry.grid(row=5, column=0, padx=5, pady=5)
Link_entry.insert(0, "Введи ссылку")

packs_entry = tk.Entry(root, width=40)
packs_entry.grid(row=6, column=0, padx=5, pady=5)
packs_entry.insert(0, "Введи паки")


DB = tk.Button(text="Удалить паки", command=lambda: [Pack_Delete(packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get()), clear()])
DB.grid(row=7, column=0, padx=10, pady=5,  sticky="nsew")
NDB = tk.Button(text="Пометить недопоставкой", command=lambda: [Pack_Nedopostavka(packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get()), clear()])
NDB.grid(row=8, column=0, padx=10, pady=5, sticky="nsew")
DVB = tk.Button(text="Переместить в зону ДВ", command=lambda: [Pack_DV(packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get()), clear()])
DVB.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")
Statusbt = tk.Button(text="Статус паков", command=lambda: packstatus(packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get()))
Statusbt.grid(row=10, column=0, padx=10, pady=5, sticky="nsew")

root.mainloop()