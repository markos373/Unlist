from selenium import webdriver
import os


if __name__ == "__main__":

    GMAIL_LOGIN = "https://accounts.google.com/ServiceLogin?service=mail"
    PATH = os.getcwd()

    # Asssumes that chromedriver.exe is placed in the current working directory
    driver = webdriver.Chrome(PATH)
    driver.get(GMAIL_LOGIN)
