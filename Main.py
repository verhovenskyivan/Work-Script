from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter.scrolledtext import *
from wintoast import ToastNotifier
from selenium import webdriver
from functools import cache
from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import  re, time

s = Service('./workscript-main/chromedriver.exe')

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_argument("--headless")
option.add_argument = {'user-data-dir':'/Users/Application/Chrome/Default'}

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = option )

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
   t.insert(INSERT, Object + "\n" + ' ' + actiontype + '\n') 
   time.sleep(0.5) 
   t.update() 
   t.focus_force() 
   t.see('end')    

'''
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
   Driver_action(get_object, Pups, get_user)'''
                            
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
            info = ("Не"+ actiontype + "\n")
            output(Pack, info)
            #Pack_status(Packlist, link, email, password, sublink)
            link_create(link, sublink)
            show_notify('Что-то пошло не так')
      time.sleep(0.2)
   show_notify('Процесс завершен')
   output('------------','------------- \n')
   
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
            Pack_status(Packlist, link, email, password, sublink)
            link_create(link, sublink)
            show_notify('Что-то пошло не так)')
      time.sleep(0.2)
   show_notify('Процесс завершен')
   output('------------','------------- \n')
                         
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
            Pack_status(Packlist, link, email, password, sublink)
            link_create(link, sublink)
               
@cache
def Order_status(Orderlist, link, email, password, status_sublink):
   Pups(link, email, password, status_sublink)
   for Order in re.split('[";|,|:|\n|\\|/|//|.| | "]', Orderlist):
      if Order != '':
         try:
            driver.find_element(By.NAME, 'filterValue').send_keys(Order) 
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            index = driver.find_element(By.XPATH, 
                  '/html/body/div[4]/div[4]/form/table/tbody/tr/td[4]/a').get_attribute('href').split('/')
            order_id = index[5]                
            info = ('\n' + " Cтатус: "  + 
                  (driver.find_element(By.XPATH, f'//*[@id="order{order_id}Status"]').text) + '\n')
            output(Order, info)
            driver.find_element(By.NAME, 'filterValue').clear()
         except NoSuchElementException:#Обработка ошибки 
              index = driver.find_element(By.XPATH, 
                     '/html/body/div[4]/div[4]/table/tbody/tr/td[1]').text 
              info = driver.find_element(By.XPATH, 
                     f'//*[@id="order{index}Status"]').text
              driver.find_element(By.NAME, 'filterValue').clear()
              output(Order, info)
      time.sleep(0.2)
   show_notify('Процесс завершен')
   output('------------','------------- \n')

@cache
def Pack_status(Packlist, link, email, password, status_sublink):
   Pups(link, email, password, status_sublink)
   for Pack in re.split('[";|,|:|\n|\\|/|//| "]', Packlist):
      if Pack != '':
         try:
            driver.find_element(By.ID, "input-search").send_keys(Pack)
            driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
            value = driver.find_element(By.XPATH, '/html/body/div[4]/div[4]/table/tbody/tr/td[6]').text
            quant = driver.find_element(By.XPATH, '/html/body/div[4]/div[4]/table/tbody/tr/td[7]').text
            info = (" Cтатус: " + value + '\n' + " Товаров: " + quant + "\n")
            output(Pack, info)
            driver.find_element(By.ID, "input-search").clear()
         except NoSuchElementException:#Обработка ошибки  
            output(Pack, 'Не найден')
            driver.find_element(By.ID, "input-search").clear()    
   show_notify('Процесс завершен')
   output('------------','------------- \n')          
            
def Sold_sender(Orderlist, link, email, password, sublink):
   Pups(link, email, password, sublink)
   for Order in re.split('[";|,|:|\n|\\|/|//| "]',Orderlist): 
      if Order != '': 
         driver.find_element(By.CLASS_NAME, "form-control").send_keys(Order)#Ввод в графу поиска
         driver.find_element(By.XPATH,'/html/body/div[4]/div[4]/div[2]/form/button[1]').send_keys(Keys.ENTER)#Нажатие кнопки поиск
         try:
            delivered = driver.find_elements(By.XPATH,"//td[contains(text(),'UpdateStatusSingleOrder')]/preceding-sibling::td[1]") 
            for delivery in delivered:
               restart_btn = f'href="/queue/restart/id/{delivery.text}"'
               print(restart_btn)
            output(Order, 'Солды отправлены')
         except NoSuchElementException:
            output(Order, 'Не найден')
   output('------------','------------- \n')

@cache
def clear():
   packs_entry.delete(0, END)
   Link_entry.delete(0, END)
   
def clear_textbox():
   t.delete("1.0","end")
   
@cache
def get_korob():
   korob = Toplevel()
   korob_entry = tk.Entry(korob, width= 45)
   korob_entry.insert(0, "Введи Короб:")
   korob_entry.pack()
   korob.focus_force()
   PKOb = tk.Button(korob, text = "Переместить в короб", bg = 'white', command = lambda: [Pack_Korob(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), korob_entry.get(),
      '/tools/move_objects_to_rejectbox', '//*[@id="filterForm"]/button', "btn btn-default", " Перемещен в короб отказов"), clear()])
   PKOb.pack()

@cache
def show_notify(status):
   notify = ToastNotifier()
   notify.show_toast('Pups helper' , status , icon_path='./image.jpg', duration= 10)

#Конец команд и функций

#Объявление интерфейса Tkinter
root = tk.Tk()
root.title("Pups Helper")
root.geometry("675x800")
root['background'] = 'white'

# --- Первый фрейм --- 
first_frame = tk.Frame(root, bg = 'white', width = 200, height = 400)
first_frame.grid(row = 0, column = 0, padx = 5, pady = 5)

# --- Лэйбл с надписью F1RST LINE ---       
tk.Label(first_frame, text = "F1RST LINE", bg = 'white', relief = RAISED).grid(row = 0, column = 0, padx = (300,0), pady = 3)

# --- Лэйбл логина --- 
tk.Label(text = "Логин", bg = 'white').grid(row = 1, column = 1, padx = (10, 160), pady = (0, 5))

# --- Поле ввода логина и его параметры --- 
login_entry = tk.Entry(root, width=20)
login_entry.grid(row = 2, column = 1, padx = (10, 160), pady = (0, 50))

# --- Лэйбл пароля --- 
tk.Label(text="Пароль", bg = 'white').grid(row = 1, column = 1, padx = (165, 10), pady = (0, 5))

# --- Поле ввода пароля и его параметры --- 
pass_entry = tk.Entry(root, show = "*", width = 20) 
pass_entry.grid(row = 2, column = 1, padx = (165, 10), pady = (0, 50))

# --- Лэйбл с запросом ввести ссылку --- 
tk.Label(text='Введи ссылку:', bg = "white").grid(row = 2, column=0, padx = (100, 100), pady = (0, 5))

# --- Поле ввода ссылки и его параметры --- 
Link_entry = tk.Entry(root, width = 45)
Link_entry.grid(row = 2, column = 0, padx = (10, 10), pady = (30, 0))

# --- Лэйбл с запросом ввести паки/заказы --- 
tk.Label(text='Введи паки/заказы:', bg = "white").grid(row = 3, column=0, padx = (100, 100), pady = (0, 5))

# --- Поле ввода паков/заказов --- 
packs_entry = tk.Entry(root, width = 45,)
packs_entry.grid(row = 4, column = 0, padx = (10, 10), pady = 5)

# --- Кнопка удаления паков --- 
DB = tk.Button(text = "Удалить паки",  bg = 'white', command = lambda: [Pack_act(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/tools/unknown_pack_removal', "submit0", "jq-remove-pack-button", " удален",), clear()])
# --- Параметры кнопки удаления паков --- 
DB.grid(row = 15, column = 0, padx = 10, sticky = 'nsew'  )   

# --- Кнопка пометки недопоставкой --- 
NDB = tk.Button(text = "Пометить недопоставкой",  bg = 'white', command = lambda: [Pack_act(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/tools/mark_pack_missing', "submit0", "jq-mark-pack-missing-button", " помечен недопоставкой"), clear()])
# --- Параметры кнопки пометки недопоставкой --- 
NDB.grid(row = 16, column = 0, padx = 10, pady = 5, sticky = "nsew")

# --- Кнопка переноса в ДВ --- 
DVB = tk.Button(text = "Переместить в зону ДВ", bg = 'white', command = lambda: [Pack_Perenos(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/tools/move_pack_to_clearance_zone', "btn-default", "btn-default", " Перемещен в зону ДВ"), clear()])
# --- Параметры кнопки переноса в ДВ --- 
DVB.grid(row = 17, column = 0, padx = 10, pady = 5, sticky = "nsew")

# --- Кнопка переноса в короб отказов --- 
PKO = tk.Button(text = "Переместить паки в короб отказов", bg = 'white', command = lambda: [get_korob()])
# --- Параметры кнопки переноса в короб отказов --- 
PKO.grid(row = 18, column = 0, padx = 10, pady = 5, sticky = "nsew")

# --- Кнопка вывода статусов паков --- 
StatusPack = tk.Button(text = "Статус Паков", bg = 'white', command = lambda: [Pack_status(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(), 
      '/containers/all/'), clear()])
# --- Параметры кнопки статуса паков --- 
StatusPack.grid(row = 19, column = 0, padx = 10, pady = 5, sticky = "nsew")

# --- Кнопка статуса заказов --- 
StatusOrders = tk.Button(text = "Статус Заказа", bg = 'white', command = lambda: [Order_status(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(),
     '/orders/index/page/1/order_by/deliveryDate/desc/?filterNames=o.orderNr&filterValue='), clear()])
# --- Параметры кнопки статуса заказов ---   
StatusOrders.grid(row = 20, column = 0, padx = 10, pady = 5, sticky = "nsew")

Sold_Sender_btn = tk.Button(text = "Отправить солды", bg = 'white', command = lambda: [Sold_sender(
   packs_entry.get(), Link_entry.get(), login_entry.get(), pass_entry.get(),
      '/queue/page/1?search=' )])
Sold_Sender_btn.grid(row = 21, column = 0, padx = 10, pady = 5, sticky = "nsew")

# --- Кнопка очистки поля вывода ---
clear_button = tk.Button(text = 'Очистить', bg = 'white', command = clear_textbox)
#--- Параметры кнопки очистки вывода ---
clear_button.grid(row = 6, column=1, sticky='e')

# --- Поле текстового вывода и его параметры --- 
t = Text(root,height=30,width= 35,wrap = WORD)
t.grid(row = 7, rowspan=15 , column = 1, sticky="nes")

# --- Скролл для поля текстового вывода и его параметры --- 
s = Scrollbar(root, orient = VERTICAL)
s.grid(row = 7,rowspan=15, column = 1,  padx=(50,0), pady=(0,27),   sticky = "nse") 

root.mainloop()      
