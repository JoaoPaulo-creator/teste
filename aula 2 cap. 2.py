from selenium import webdriver


driver = webdriver.Firefox()
driver.get('file:///C:/Users/joaog/AppData/Local/Temp/Temp1_Ex_Files_Python_Automation_Testing.zip/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html')

login_form = driver.find_element_by_id('loginForm')
print(login_form)
