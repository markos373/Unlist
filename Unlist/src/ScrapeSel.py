from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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

    time.sleep(2)
    driver.find_element_by_name('password').send_keys(PASS)
    driver.find_element_by_id("passwordNext").click()
   # driver.find_element_by_xpath('//button[@id="passwordNext"]')
    time.sleep(5)
    print("ATTEMPTING")
    emails = []
    emails = driver.find_elements_by_xpath("//*[@class='yW']/span")
    f = open("emails.txt", "w+")
    for email in emails:
        f.write(email.text)
        f.write("\n")
    f.close()
    for i in range(len(emails)):
        emails = driver.find_elements_by_xpath("//*[@class='yW']/span")
        time.sleep(2)
        emails[i].click()
        time.sleep(2)
        
        try:
            driver.find_element_by_class_name("Ca").click()
        except NoSuchElementException:
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)
            continue
        time.sleep(1)
        driver.find_element_by_name("s").click()
        time.sleep(1)
        driver.execute_script("window.history.go(-1)")
        time.sleep(1)

   # driver.close()

    