from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('file:///C:/Users/joaog/AppData/Local/Temp/Temp1_Ex_Files_Python_Automation_Testing.zip/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html')

login_form_ab = driver.find_element_by_xpath('/html/body/form[1]') #xpath absoluto
login_form_relative = driver.find_element_by_xpath('//form[1]') #xpath relativo
login_form_id = driver.find_element_by_xpath("//form[@id='loginForm']") #xpath relativo


print(f'The name of the element is: {login_form_ab}')
print(f'The name of the element is: {login_form_relative}')
print(f'The name of the element is: {login_form_id}')


driver.implicitly_wait(100)
driver.quit()
