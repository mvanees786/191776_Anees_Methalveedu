
from selenium import webdriver  
import time  
print("test case started")  
#open Google Chrome browser  
driver = webdriver.Chrome("D:/chromedriver.exe")  
#maximize the window size  
driver.maximize_window()  
#delete the cookies  
driver.delete_all_cookies()  
#navigate to the url  
driver.get("http://127.0.0.1:5000/")  
time.sleep(2)


#identify the user name text box and enter the value  
driver.find_element_by_id("name").send_keys("Anees Methalveedu")  
time.sleep(2)

#identify the Employee id text box and enter the value
driver.find_element_by_id("eid").send_keys("191776") 
time.sleep(1)

#identify the company name text box and enter the value
driver.find_element_by_id("cname").send_keys("Ust Global")
time.sleep(2)

#identify the email  text box and enter the value
driver.find_element_by_id("eml").send_keys("191776@ust-global.com")

#Click on submit button
driver.find_element_by_xpath("/html/body/div/div/form/input[5]").click()
time.sleep(5)
 
#close the browser  
driver.close()  
print("Ust login has been successfully completed")  