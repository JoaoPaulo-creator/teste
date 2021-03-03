from selenium import webdriver


driver = webdriver.Firefox()
driver.get('file:///file/path/example.html')

login_form = driver.find_element_by_id('loginForm')
print(login_form)
