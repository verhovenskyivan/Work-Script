from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service('./WorkScript/chromedriver.exe')                                                              

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://bob-ru.lamoda.tech/tools/axapta")

orders = input("Введи заказы: ")
driver.find_element(By.ID, "input-orders").send_keys(orders.split([";|,|:|\n|\\| "]))
driver.find_element(By.CLASS_NAME, "btn btn-primary").send_keys(Keys.ENTER)
print(orders.split([";|,|:|\n|\\| "])) + 'Заказы отправлены'