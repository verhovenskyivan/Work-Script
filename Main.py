from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter.scrolledtext import *
from selenium import webdriver
from functools import cache
from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import  re, time
from winotify import Notification, audio

s = Service('./workscript-main/chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")
options.add_argument = {'user-data-dir':'/Users/Application/Chrome/Default'}

driver = webdriver.Chrome(options = options, service=Service(ChromeDriverManager().install()))

@cache
def link_create(linkd, sublink):
   link = linkd.split('/')
   Link_Start = 'https://'
   Pups_Link = link[2]
   Full_link = Link_Start + Pups_Link + sublink
   driver.get(Full_link) 

@cache
def Pups(link, email, password, sublink):
   try:
      link_create(link, sublink)
      driver.find_element(By.ID, 'identity').send_keys(email)
      driver.find_element(By.ID, 'credential').send_keys(password)
      driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)
   except WebDriverException:
      t.insert(INSERT, "\n" + "page down" + "\n")
      time.sleep(0.5)
      t.update()
      t.focus_force()
      t.see('end')     
 
@cache       
def output(Object, actiontype): 
   t.insert(INSERT, ' ' + Object + actiontype + "\n") 
   time.sleep(0.5) 
   t.update() 
   t.focus_force() 
   t.see('end')    
   
@cache 
def writer(Object, actiontype, link):
   file_object = open('Паки.txt', 'a')
   file_object.write(Object + "Не"+ actiontype + link[2])
   file_object.write("\n")
   file_object.close() 

@cache 
def Driver_action(Object_List, link, email, password, sublink, search_button_insert, 
                  search_button_press, act_button, actiontype):
   Pups(link, email, password, sublink)
   for Object in re.split('[";|,|:|\n|\\|/|//| "]',Object_List): 
      if Object != '': 
         driver.find_element(By.CLASS_NAME, search_button_insert).send_keys(Object)#Ввод в графу поиска
         driver.find_element(By.NAME, search_button_press).send_keys(Keys.ENTER)  
         try:
            if DB or NDB or DVB:
               driver.find_element(By.CLASS_NAME, act_button).send_keys(Keys.ENTER)#Нажатие кнопки удаление
               driver.switch_to.alert.accept()#Свич на алерт и его принятие 
               output(Object, actiontype)
               driver.find_element(By.CLASS_NAME, "form-control").clear()
            elif PKO:
               driver.find_element(By.CLASS_NAME, act_button).send_keys(Keys.ENTER)#Нажатие кнопки удаление
               driver.switch_to.alert.accept()#Свич на алерт и его принятие 
               t.insert(INSERT, Object + actiontype + "\n")
               output(Object, actiontype)
               driver.find_element(By.CLASS_NAME, "form-control").clear()
            elif StatusOrders or StatusPack:
               driver.find_element(By.ID, "input-search").send_keys(Object)
               driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
               value = driver.find_element(By.CLASS_NAME, "cell-status").text
               #driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr/td[6]').text
               output(Object) + t.insert(INSERT,"\n" + Object + " имеет статус:" + "\n" + value )
               quant = driver.find_element(By.CLASS_NAME, 'cell-itemQuantity').text
               #driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr/td[8]').text
               output(Object) + t.insert(INSERT, "\n" + Object  + " Кол-во позиций:" + ' ' + quant + "\n" )
         except NoSuchElementException or NoAlertPresentException:
            writer(Object, actiontype, link)
            output(Object, actiontype)

def get_object(object):
   packs_entry.get = object
 
def get_user(email, password):
   login_entry.get = email
   pass_entry.get = password     
            
def Pack_Action():
   Driver_action(get_object, Pups, get_user, )
                            
@cache
def Pack_act(Packlist, link, email, password, sublink, search_button, act_button, actiontype,):
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\|/|//| "]',Packlist): 
      if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.NAME, search_button).send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.CLASS_NAME, act_button).send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()
            output(Pack, actiontype)
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:
            driver.find_element(By.CLASS_NAME, "form-control").clear()
            t.insert(INSERT, Pack + " Не"+ actiontype + "\n")
            output(Pack, actiontype)
            #writer(Pack,actiontype, link) 
            packstatus(Packlist, link, email, password, sublink)
            link_create(link, sublink)
         driver.find_element(By.CLASS_NAME, "form-control").clear()

@cache
def Pack_Perenos(Packlist, link, email, password, sublink, search_button, act_button, actiontype,):
    Pups(link, email, password, sublink)
    for Pack in re.split('[";|,|:|\n|\\|/|//| "]',Packlist): 
      if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
         driver.find_element(By.CLASS_NAME, search_button).send_keys(Keys.ENTER)
         try:
            driver.find_element(By.CLASS_NAME, act_button).send_keys(Keys.ENTER)
            driver.switch_to.alert.accept()
            output(Pack, actiontype)
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException or NoAlertPresentException:
            driver.find_element(By.CLASS_NAME, "form-control").clear()
            t.insert(INSERT, Pack + " Не"+ actiontype + "\n")
            output(Pack, actiontype)
            #writer(Pack, actiontype, link)
            packstatus(Packlist, link, email, password, sublink)
            link_create(link, sublink)
                  
@cache
def Pack_Korob(Packlist, link, email, password, korob, sublink, search_button, act_button, actiontype):
    Pups(link, email, password, sublink)
    for Pack in re.split('[";|,|:|\n|\\|/|//| "]',Packlist): 
      if Pack != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)#Ввод в графу поиска
         driver.find_element(By.XPATH, search_button).send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            get_korob(korob)
            driver.find_element(By.XPATH, '//*[@id="layout-container-inner"]/div/form/div/input[3]').send_keys(korob)
            driver.find_element(By.CLASS_NAME, act_button).send_keys(Keys.ENTER)#Нажатие кнопки удаление
            driver.switch_to.alert.accept()#Свич на алерт и его принятие 
            output(Pack, actiontype)
            driver.find_element(By.CLASS_NAME, "form-control").clear()
         except NoSuchElementException:#Обработка ошибки
            output(Pack, actiontype)
            #writer(Pack, actiontype, link)
            packstatus(Packlist, link, email, password, sublink)
            link_create(link, sublink)
               
@cache
def Order_status(Orderlist, link, email, password, status_sublink):
   Pups(link, email, password, status_sublink)
   for Order in re.split('[";|,|:|\n|\\|/|//|  "]', Orderlist):
     if Order != '':
         try:
            driver.find_element(By.NAME, 'filterValue').send_keys(Order) 
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            value = driver.find_element(By.XPATH, '//*[@id="order11213235Status"]').text
            quant = driver.find_element(By.XPATH, '//*[@id="layout-container-inner"]/table/tbody/tr/td[3]').text
            info = (" имеет статус: "  + value + " Кол-во товаров: " + quant + "\n")
            output(Order, info)
         except NoSuchElementException:#Обработка ошибки 
            output(Order, 'Не существует' + "\n")
         driver.find_element(By.NAME, 'filterValue').clear()
            
@cache
def packstatus(Packlist, link, email, password, status_sublink):
   Pups(link, email, password, status_sublink)
   for Pack in re.split('[";|,|:|\n|\\|/|//| "]', Packlist):
     if Pack != '':
         try:
            driver.find_element(By.ID, "input-search").send_keys(Pack)
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            value = driver.find_element(By.CLASS_NAME, "cell-status").text
            #driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr/td[6]').text
            output(Pack) + t.insert(INSERT,"\n" + Pack + " имеет статус:" + "\n" + value )
            quant = driver.find_element(By.CLASS_NAME, 'cell-itemQuantity').text
            #driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr/td[8]').text
            output(Pack) + t.insert(INSERT, "\n" + Pack  + " Кол-во позиций:" + ' ' + quant + "\n" )
            driver.find_element(By.ID, "input-search").clear()
         except NoSuchElementException:#Обработка ошибки  
           output(Pack)
           #writer(Pack, link)      
         
            
def Sold_sender(Orderlist, link, email, password, sublink, search_button):
   Pups(link, email, password, sublink)
   for Order in re.split('[";|,|:|\n|\\|/|//| "]',Orderlist): 
      if Order != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Order)#Ввод в графу поиска
         driver.find_element(By.CLASS_NAME, search_button).send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            driver.find_element(By.LINK_TEXT, 'sold')
            driver.find_element(By.CLASS_NAME, 'ajax queue-restart' ).send_keys(Keys.ENTER)
            driver.find_element(By.LINK_TEXT, 'arrive')
            driver.find_element(By.CLASS_NAME, 'ajax queue-restart' ).send_keys(Keys.ENTER)
         except NoSuchElementException:
            print ("No such element")

       
'''def get_status():
   status = Toplevel()
   get_entry = tk.Entry(status, width= 45)
   get_entry.grid(row = 1, column = 0, padx = (40, 10), pady = (30, 0))
   get_entry.pack()
   status_order_button = Button(status, text = 'Статус заказов', bg = 'White', command = lambda: [Order_status(get_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(),
      '//*[@id="all-packs-table"]/tbody/tr/td[4]'), clear()])
   status_order_button.pack() 
   status_pack_button = Button(status, text = "Статус паков", bg = 'White', command = lambda: [packstatus(
   get_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/containers/all/'), clear()]) 
   status_pack_button.pack()'''
   
@cache                      
def Link_temp_text(e):
   Link_entry.delete(0, "end")
   
@cache
def Pack_temp_text(e):
   packs_entry.delete(0, "end")
   
@cache
def clear():
   packs_entry.delete(0, END)
   packs_entry.insert(0, "Введи паки")
   Link_entry.delete(0, END)
   Link_entry.insert(0, "Введи ссылку")
   
@cache
def get_korob():
   korob = Toplevel()
   korob_entry = tk.Entry(korob, width= 45)
   korob_entry.insert(0, "Введи Короб:")
   korob_entry.pack()
   korob.focus_force()
   PKOb = tk.Button(korob, text = "Переместить в короб", bg = 'White', command = lambda: [Pack_Korob(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), korob_entry.get(),
      '/tools/move_objects_to_rejectbox', '//*[@id="filterForm"]/button', "btn btn-default", " Перемещен в короб отказов"), clear()])
   PKOb.pack()
                  
notify = Notification(app_id='Main.py',
                      title='Pack Helper',
                      msg='Процесс завершен',
                      duration='long',
                      icon='./workscript-main/icon.png')                   
#Конец команд и фукнций

#Начало интерфейса
root = tk.Tk()
root.title("Pack Helper")
root.geometry("300x480")
root['background'] = 'White'

first_frame = tk.Frame(root, bg = 'white', width = 200, height = 400)
first_frame.grid(row = 0, column = 0, padx = 5, pady = 5)

style = Style()
style.map('TButton', foreground = ([('active', 'black')]))                    
style.configure("TButton", font=("Arial", 10),bold = True, borderwidth = 2)
      
tk.Label(first_frame, text = "F1RST LINE", bg = 'White', relief = RAISED).grid(row = 0, column = 0, padx = 100, pady = 3)

tk.Label(text = "Логин", bg = 'White').grid(row = 1, column = 0, padx = (10, 160), pady = (0, 5))
login_entry = tk.Entry(root, width=20)
login_entry.grid(row = 2, column = 0, padx = (10, 160), pady = (0, 50))

tk.Label(text="Пароль", bg = 'White').grid(row = 1, column = 0, padx = (165, 10), pady = (0, 5))
pass_entry = tk.Entry(root, show = "*", width = 20) 
pass_entry.grid(row = 2, column = 0, padx = (165, 10), pady = (0, 50))

Link_entry = tk.Entry(root, width = 45)
Link_entry.grid(row = 2, column = 0, padx = (10, 10), pady = (30, 0))
Link_entry.insert(0, "Введи ссылку")
Link_entry.bind("<FocusIn>", Link_temp_text)

packs_entry = tk.Entry(root, width = 45) 
packs_entry.grid(row = 3, column = 0, padx = (10, 10), pady = 5)
packs_entry.insert(0, "Введи паки/заказы:")
packs_entry.bind("<FocusIn>", Pack_temp_text)

DB = tk.Button(text = "Удалить паки",  bg = 'White', command = lambda: [Pack_act(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/tools/unknown_pack_removal', "submit0", "jq-remove-pack-button", " удален",), clear()])
DB.grid(row = 7, column = 0, padx = 10, pady = 5,  sticky="nsew")   

NDB = tk.Button(text = "Пометить недопоставкой",  bg = 'White', command = lambda: [Pack_act(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/tools/mark_pack_missing', "submit0", "jq-mark-pack-missing-button", " помечен недопоставкой"), clear()])
NDB.grid(row = 8, column = 0, padx = 10, pady = 5, sticky = "nsew")

DVB = tk.Button(text = "Переместить в зону ДВ", bg = 'White', command = lambda: [Pack_Perenos(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/tools/move_pack_to_clearance_zone', "btn-default", "btn-default", " Перемещен в зону ДВ"), clear()])
DVB.grid(row = 9, column = 0, padx = 10, pady = 5, sticky = "nsew")

PKO = tk.Button(text = "Переместить паки в короб отказов", bg = 'White', command = lambda: [get_korob()])
PKO.grid(row = 10, column = 0, padx = 10, pady = 5, sticky = "nsew")

StatusPack = tk.Button(text = "Статус Паков", bg = 'White', command = lambda: [packstatus(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/containers/all/'), clear()])
StatusPack.grid(row = 11, column = 0, padx = 10, pady = 5, sticky = "nsew")

StatusOrders = tk.Button(text = "Статус Заказа", bg = 'White', command = lambda: [Order_status(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(),
     '/orders/index/'), clear()])  
StatusOrders.grid(row = 12, column = 0, padx = 10, pady = 5, sticky = "nsew")

t = Text(root, height = 7, width = 35, wrap = WORD)
t.grid(row = 13, column = 0)

s = Scrollbar(root, orient = VERTICAL)
s.grid(row = 13, column = 0,  padx=(280, 0),  sticky = "nsew") 

root.mainloop()      