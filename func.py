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
from login import Pups

s = Service('./WorkScript/chromedriver.exe')                                                             
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))     


def Pack_Delete(Packlist, link, email, password):
   sublink = "/tools/unknown_pack_removal"
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
      if Pack != '': 
         print(Pack)
         
def Pack_DV(Packlist, link, email, password): 
   sublink = "/tools/move_pack_to_clearance_zone"
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]',Packlist): 
        if Pack != '': 
         print(Pack)
         
          
def Pack_Nedopostavka(Packlist, link, email, password):
   sublink = "/tools/mark_pack_missing"
   Pups(link, email, password, sublink)
   for Pack in re.split('[";|,|:|\n|\\| "]', Packlist): 
      if Pack != '': 
         print(Pack)
         
          