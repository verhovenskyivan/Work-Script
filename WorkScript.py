#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from multiprocessing import Process
from win10toast import ToastNotifier
import time
import sys
import os
import UI
import Secret

s = Service('./WorkScript/chromedriver.exe')                                                              


Pack = input("Enter pack: ")


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
  

toast = ToastNotifier()
toast.show_toast(Pack,"Process started")


driver.minimize_window()
driver.get(Secret.link)
driver.find_element(By.ID, 'identity').send_keys(Secret.email)
driver.find_element(By.ID, 'credential').send_keys(Secret.password)
driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)
driver.find_element(By.CLASS_NAME, "form-control").send_keys(Pack)
driver.find_element(By.NAME,"submit0").send_keys(Keys.ENTER)
driver.find_element(By.CLASS_NAME, "jq-remove-pack-button").send_keys(Keys.ENTER)
driver.switch_to.alert.accept()
time.sleep(1)
driver.quit()

if __name__ == '__name__':
    process = Process(target=driver)
    process.start()
    process.join()
     
