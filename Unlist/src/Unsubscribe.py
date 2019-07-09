from selenium import webdriver
import time
import os

if __name__ == "__main__":

    # Define constants: login link and the path to the chromedriver.exe file
    GMAIL_LOGIN = "https://accounts.google.com/ServiceLogin?service=mail"
    CHROMEDRIVER_PATH = os.getcwd()

    GMAIL = "unlist.rcos@gmail.com"
    PASSWORD = "RCOS_unlist!"

    #try:
    # Asssumes that chromedriver.exe is placed in the current working directory
    driver = webdriver.Chrome(CHROMEDRIVER_PATH + "/chromedriver.exe")

    # Tell the driver to open up the webpage
    driver.get(GMAIL_LOGIN)

    # Sleep to ensure a clean open
    time.sleep(1)

    # Send the email to the login page
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(GMAIL)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    time.sleep(2)

    # Send the password to the login page
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(PASSWORD)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    time.sleep(2)

    # Accept automated browsing
    try:
        driver.find_element_by_xpath('//*[@id="identifierDone"]').click()

    print("Program complete")

    # Close the driver
    finally:
        driver.close()
