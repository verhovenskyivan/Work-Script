from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

s = Service('./WorkScript/chromedriver.exe')                                                              

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("")

Pack = input("Enter Pack: ")
email = ""
password = ""

driver.find_element(By.ID, 'identity').send_keys(email)#Ввод логина
driver.find_element(By.ID, 'credential').send_keys(password)#Ввод пароля
driver.find_element(By.NAME, "submit").send_keys(Keys.ENTER)#Авторизация


driver.find_element(By.ID, "input-search").send_keys(Pack)
driver.find_element(By.NAME, "submit0").send_keys(Keys.ENTER)
value = driver.find_element(By.XPATH, '//*[@id="list-table"]/tbody/tr[2]/td[6]').text #поиск и выгрузка статуса из папса
print(value)
