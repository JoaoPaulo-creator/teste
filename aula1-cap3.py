from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://www.python.org/')

search = driver.find_element_by_name('q')
search.clear()
search.send_keys('pycon', u'\ue007')
#search.send_keys(Keys.ENTER)
time.sleep(1)

#driver.close()

