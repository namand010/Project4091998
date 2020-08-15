from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\namand\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.google.com')
wb=driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
wb.send_keys("Where are you now")
#driver.find_element_by_xpath("//input[@class='gNO89b' and @data-ved='0ahUKEwjYscus57znAhUFxTgGHVDvB4MQ4dUDCAo']").click()
wb.submit()


