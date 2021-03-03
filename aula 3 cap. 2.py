from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('file:///C:/Users/joaog/AppData/Local/Temp/Temp1_Ex_Files_Python_Automation_Testing.zip/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html')

username = driver.find_element_by_name('username')
print(f'The name of the element is: {username}')

driver.implicitly_wait(100)
driver.quit()
