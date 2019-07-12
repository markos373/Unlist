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
    driver.implicitly_wait(5)

    # Tell the driver to open up the webpage
    driver.get(GMAIL_LOGIN)

    # Sleep to ensure a clean open
    time.sleep(2)

    # Send the email to the login page
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(GMAIL)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    time.sleep(2)

    # Send the password to the login page
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(PASSWORD)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    time.sleep(2)

    # Accept automated browsing --- this still needs to be tested
    """
    try:
        driver.find_element_by_xpath('//*[@id="identifierDone"]').click()
    except:
        print("Did not prompt user to accept automated browsing...")
    try:
        driver.find_element_by_xpath("//div[@role='link']").click()
    except:
        print("Did not prompt user for confirm email...")
    """

    # Load up all of the emails
    emails = driver.find_elements_by_xpath("//*[@class='yW']/span")
    time.sleep(2)
    print("Found", len(emails), "emails!")

    # Create a dictionary to hold email sender names that have been found
    #         KEY: sender (string)
    #       VALUE: unsubscribe link (string)
    # value is empty string "" if no link found
    email_dict = {}
    for email in emails:
        sender = email.text

        # Continue if an unsubscribe link has already been found
        if (sender in email_dict) and (email_dict[sender] != ""):
            continue

        # If a new email is found, see if we can unsubscribe from it
        if sender not in email_dict:
            email.click()
            #Span.Ca obtain the unsibscribe link


        print(sender)


    # Close the driver
    #finally:
    #    driver.close()
