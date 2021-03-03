from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('http://www.seleniumhq.org/')
driver.implicitly_wait(100)

elementq = driver.find_element_by_id('q')
elementname = driver.find_element_by_class_name('q')
elementxpath = driver.find_element_by_xpath('')
elementclassname = driver.find_element_by_class_name('selenium_sponsors')

print(elementq)
print(elementname)
print(elementxpath)
print(elementclassname)


'''NÃO FUNCIONOU, POIS O SITE MUDOIU'''


time.sleep(5)
driver.quit()