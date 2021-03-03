from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Firefox()
driver.maximize_window()
driver.get('file:///C:/Users/joaog/OneDrive/Documentos/pythonProject/pythonProject/Exercise%20Files/CH03/03_02/html_code_03_02.html')

select = Select(driver.find_element_by_name('numReturnSelect'))
select.select_by_index(4)
time.sleep(1)
select.select_by_visible_text("200")
time.sleep(1)
select.select_by_value("250")
time.sleep(1)

options = select.options
print(options)

submit_button = driver.find_element_by_name('continue')
submit_button.submit()
time.sleep(2)
