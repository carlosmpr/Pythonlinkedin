from selenium import webdriver
import time
chrome_driver_location = "E:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_location)
driver.get("https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=python%20developer&location=United%20States")
sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()

time.sleep(5)
user_name = driver.find_element_by_id("username")
user_name.send_keys("cybertest0508@gmail.com")


password= driver.find_element_by_id("password")
password.send_keys("An@rio4002")
button = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
button.click()