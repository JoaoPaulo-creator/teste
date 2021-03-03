from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('file:///C:/Users/joaog/AppData/Local/Temp/Temp1_Ex_Files_Python_Automation_Testing.zip/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html')

content = driver.find_element_by_class_name('content')

print(f'The class of the element is: {content}')


driver.implicitly_wait(100)
driver.quit()
