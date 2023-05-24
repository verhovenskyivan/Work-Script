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
import threading
import tkinter as tk
from selenium.common.exceptions import WebDriverException


s = Service('./workscript-main/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")

driver = webdriver.Chrome(options = options, service=Service(ChromeDriverManager().install()))

def link_create(linkd, sublink):
   link = linkd.split('/')
   Link_Start = 'https://'
   Pups_Link = link[2]
   Full_link = Link_Start + Pups_Link + sublink
   driver.get(Full_link) 

def Pups(link, email, password, sublink):
   try:
    link_create(link, sublink)
    driver.find_element(By.ID, 'identity').send_keys(email)#Ввод логина
    driver.find_element(By.ID, 'credential').send_keys(password)#Ввод пароля
    driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)#Авторизация
   except WebDriverException:
    print("page down")


def Pack_act(Packlist, link, email, password, sublink, search_button, act_button, actiontype):
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
      if Pack != '': 
         print(Pack)
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.NAME,search_button).send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, act_button).send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            print(Pack + actiontype)
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            print(Pack + "Не"+ actiontype)
            packstatus(Packlist, link, email, password)
            link_create(link, sublink)



def packstatus(Packlist, link, email, password):
   status_sublink = '/containers/all/'
   Pups(link, email, password, status_sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]', Packlist):
    if Pack != '':
     try:
            #link_create
            driver.find_element(By.ID, "input-search").send_keys(Pack)
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            value = driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr[2]/td[6]').text
            print(Pack + "имеет статус: " + value)
            quant = driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr[2]/td[8]').text
            print(Pack + "имеет кол-во товаров: " + quant)
            #driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
            #driver.find_element(By.CLASS_NAME, "btn-default").send_keys(Keys.ENTER)
            driver.find_element(By.ID, "input-search").clear()
     except NoSuchElementException:#Обработка ошибки
            print(Pack)

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


DB = tk.Button(text="Удалить паки", command=lambda: [Pack_act(packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), '/tools/unknown_pack_removal', "submit0", "jq-remove-pack-button", "удален"), clear()]) 
DB.grid(row=7, column=0, padx=10, pady=5,  sticky="nsew")
NDB = tk.Button(text="Пометить недопоставкой", command=lambda: [Pack_act(packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), '/tools/move_pack_to_clearance_zone', "btn-default", "btn-default", " Перемещен в зону ДВ"), clear()])
NDB.grid(row=8, column=0, padx=10, pady=5, sticky="nsew")
DVB = tk.Button(text="Переместить в зону ДВ", command=lambda: [Pack_act(packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), '/tools/mark_pack_missing', "submit0", "jq-mark-pack-missing-button", " помечен недопоставкой"), clear()])
DVB.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")
Statusbt = tk.Button(text="Статус паков", command=lambda: packstatus(packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get()))
Statusbt.grid(row=10, column=0, padx=10, pady=5, sticky="nsew")

root.mainloop()