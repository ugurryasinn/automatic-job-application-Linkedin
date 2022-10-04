from selenium import webdriver
import time

chrome_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()
time.sleep(5)

e_posta = driver.find_element_by_name("session_key")
e_posta.send_keys("")

password = driver.find_element_by_name("session_password")
password.send_keys("")

button = driver.find_element_by_class_name("btn__primary--large")
button.click()
time.sleep(3)

find_job = driver.find_element_by_id("ember171") 
find_job.click()
time.sleep(2)

easy_apply = driver.find_element_by_css_selector(".jobs-s-apply button")
easy_apply.click()
