from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import os


def writeEmails(email_senders):
    """Write out a list of email senders to a text file.

    Args:
        email_senders - the list of email sender names
    """
    file = open("emails.txt", "w")
    for name in email_senders:
        file.write(name)
    file.close()


# Read in the login information from the user
def getLogin():
    file = open("login.txt", "r")
    email = file.read()
    password = file.read()
    return email, password


if __name__ == "__main__":

    # Define constants: login link and the path to the chromedriver.exe file
    GMAIL_LOGIN = "https://accounts.google.com/ServiceLogin?service=mail"
    CHROMEDRIVER_PATH = os.getcwd()

    GMAIL = "unlist.rcos@gmail.com"
    PASSWORD = "RCOS_unlist!"

    try:
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
        time.sleep(1)
        print("Found", len(emails), "emails!")

        # Create a dictionary to hold email sender names that have been found
        #         KEY: sender (string)
        #       VALUE: unsubscribe link (string)
        # value is empty string "" if no link found
        email_dict = {}

        for i in range(len(emails)):
            emails = driver.find_elements_by_xpath("//*[@class='yW']/span")
            sender = emails[i].text
            print("Sender:", sender)

            # Continue if an unsubscribe link has already been found
            print (sender in email_dict)
            if (sender in email_dict) and (email_dict[sender] != ""):
                print("Skipping this email, its already been unsubscribed")
                continue

            # If a new email is found, see if we can unsubscribe from it
            if sender not in email_dict:
                time.sleep(1)
                emails[i].click() # Click the email
                time.sleep(1)

                try:
                    driver.find_element_by_class_name("Ca").click()
                    time.sleep(1)
                    driver.find_element_by_name("s").click()
                    time.sleep(1)
                    driver.execute_script("window.history.go(-1)")
                    email_dict[sender] = "FOUND" # needs to be changed later
                except NoSuchElementException:
                    print("Already unsubscribed")
                    driver.execute_script("window.history.go(-1)")
                    time.sleep(1)
                    continue

    except:
        print("An error occurred...")
    finally:
        driver.close()
        sys.exit(0)
