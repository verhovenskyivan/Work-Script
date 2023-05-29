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
options.add_experimental_option("detach", True)
options.add_argument("--headless")
#options.add_argument("--headless")
driver = webdriver.Chrome(options = options, service=Service(ChromeDriverManager().install()))

def link_create(linkd, sublink):
            file_object.close() 
            packstatus(Packlist, link, email, password, sublink)
            link_create(link, sublink)

def Pack_Korob(Packlist, link, email, password, sublink, search_button, korob, act_button, actiontype):
    Pups(link, email, password, sublink)
    for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
      if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.XPATH, search_button).send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.XPATH, '//*[@id="layout-container-inner"]/div/form/div/input[3]').send_keys(korob)
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
      '/tools/move_pack_to_clearance_zone', "btn-default", "btn-default", " Перемещен в зону ДВ"), clear()])
DVB.grid(row = 9, column = 0, padx = 10, pady = 5, sticky = "nsew")

PKO = tk.Button(text = "Переместить паки в короб отказов", bg = 'White', command = lambda: [Pack_Perenos(
PKO = tk.Button(text = "Переместить паки в короб отказов", bg = 'White', command = lambda: [Pack_Korob(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(),
      'tools/move_objects_to_rejectbox', "submit0", "submit0", " Перемещен в короб отказов"), clear()])
      '/tools/move_objects_to_rejectbox', '//*[@id="filterForm"]/button', korob_entry.get(), "submit0", " Перемещен в короб отказов"), clear()])
PKO.grid(row = 10, column = 0, padx = 10, pady = 5, sticky = "nsew")

Statusbtn = tk.Button(text = "Статус паков", bg = 'White', command = lambda: packstatus(
t_label = tk.Label(text = "", font = "Arial, 12")
t_label.grid(row = 12, column = 0)


korob_entry = Entry(root, width= 25)
korob_entry.insert(0, "Введи Короб:")
korob_entry.grid()
korob_Button = Button(root, text="Далее", command = korob_entry.get())

s = Scrollbar(root, orient = VERTICAL)
s.grid(row = 12, column = 0,  padx=(280, 0), pady=(0, 25), sticky = "nsew") 


root.mainloop()      
