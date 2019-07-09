from selenium import webdriver
import time
import os
if __name__ == "__main__":
    login_url = "https://accounts.google.com/ServiceLogin?service=mail"
    driver_path = os.getcwd()
    USER = "unlist.rcos@gmail.com"
    PASS = "RCOS_unlist!"
    driver = webdriver.Chrome(driver_path+"/chromedriver.exe")
    
    driver.get(login_url)
    driver.find_element_by_id("identifierId").send_keys(USER)
    driver.find_element_by_id("identifierNext").click()

    time.sleep(3)
    driver.find_element_by_name('password').send_keys(PASS)
    driver.find_element_by_id("passwordNext").click()
   # driver.find_element_by_xpath('//button[@id="passwordNext"]')
    time.sleep(2)
   # driver.close()

    