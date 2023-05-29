from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter.scrolledtext import *
from selenium import webdriver
from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import  re

s = Service('./workscript-main/chromedriver.exe')
options = webdriver.ChromeOptions()
      driver.find_element(By.ID, 'credential').send_keys(password)#Ввод пароля
      driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)#Авторизация
   except WebDriverException:
      t.insert(INSERT, "\n " + " page down")
      t.insert(INSERT, "page down" + "\n")

def Pack_act(Packlist, link, email, password, sublink, search_button, act_button, actiontype,):
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
      if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.NAME,search_button).send_keys(Keys.ENTER)#Нажатие кнопки поиск
         driver.find_element(By.NAME, search_button).send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, act_button).send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            t.insert(INSERT, "\n " + Pack + actiontype )
            t.insert(INSERT, + Pack + actiontype )
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            t.insert(INSERT, "\n " + Pack + " Не"+ actiontype)
            t.insert(INSERT, Pack + " Не"+ actiontype + "\n ")
            file_object = open('Паки.txt', 'a')
            file_object.write(Pack + "Не"+ actiontype + link[2])
            file_object.write("\n")
            packstatus(Packlist, link, email, password, sublink)
            link_create(link, sublink)

def Pack_Perenos(Packlist, link, email, password, sublink, search_button, act_button, actiontype,):
    Pups(link, email, password, sublink)
    for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
      if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.CLASS_NAME, search_button).send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, act_button).send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            t.insert(INSERT, Pack + actiontype + "\n ")
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            t.insert(INSERT, Pack + " Не"+ actiontype + "\n ")
            file_object = open('Паки.txt', 'a')
            file_object.write(Pack + "Не"+ actiontype + link[2])
            file_object.write("\n")
            file_object.close() 
            packstatus(Packlist, link, email, password, sublink)
            link_create(link, sublink)
   
def packstatus(Packlist, link, email, password, status_sublink):
   Pups(link, email, password, status_sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]', Packlist):
            driver.find_element(By.ID, "input-search").send_keys(Pack)
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            value = driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr[2]/td[6]').text
            t.insert(INSERT, "\n " + Pack + " имеет статус: " + value ) 
            t.insert(INSERT, Pack + " имеет статус: " + value  + "\n ") 
            quant = driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr[2]/td[8]').text
            t.insert(INSERT, "\n" + Pack + "имеет статус: " + quant )
            t.insert(INSERT, Pack + "имеет статус: " + quant + "\n")
            driver.find_element(By.ID, "input-search").clear()
         except NoSuchElementException:#Обработка ошибки  
            t.insert(INSERT, "\n "  + Pack + ' Не существует')        
            t.insert(INSERT, Pack + ' Не существует' + "\n")        
#Конец команд и фукнций

#Начало интерфейса
      '/tools/mark_pack_missing', "submit0", "jq-mark-pack-missing-button", " помечен недопоставкой"), clear()])
NDB.grid(row = 8, column = 0, padx = 10, pady = 5, sticky = "nsew")

DVB = tk.Button(text = "Переместить в зону ДВ", bg = 'White', command = lambda: [Pack_act(
DVB = tk.Button(text = "Переместить в зону ДВ", bg = 'White', command = lambda: [Pack_Perenos(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/tools/move_pack_to_clearance_zone', "btn-default", "btn-default", " Перемещен в зону ДВ"), clear()])
DVB.grid(row = 9, column = 0, padx = 10, pady = 5, sticky = "nsew")

PKO = tk.Button(text = "Переместить паки в короб отказов", bg = 'White', command = lambda: [Pack_act(
PKO = tk.Button(text = "Переместить паки в короб отказов", bg = 'White', command = lambda: [Pack_Perenos(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(),
      'tools/move_objects_to_rejectbox', "submit0", "submit0", " Перемещен в короб отказов"), clear()])
PKO.grid(row = 10, column = 0, padx = 10, pady = 5, sticky = "nsew")
t_label = tk.Label(text = "", font = "Arial, 12")
t_label.grid(row = 12, column = 0)

root.mainloop()
s = Scrollbar(root, orient = VERTICAL)
s.grid(row = 12, column = 0,  padx=(280, 0), pady=(0, 25), sticky = "nsew") 

root.mainloop()      
