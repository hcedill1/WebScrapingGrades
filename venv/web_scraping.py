import pandas as pd
import credentials as cred
from bs4 import BeautifulSoup
from selenium import webdriver

def runWithoutClosing():
    while(True):
        pass

def main():

    driver = webdriver.Chrome(
        executable_path='/Users/hernancedillo/Documents/GitHubLocalRepo/WebScrapingGrades/venv/chromeDriver/chromedriver')
    driver.get('https://oxylabs.io/blog')
    usernameCred = cred.username
    passwordCred = cred.password
    runWithoutClosing()


if __name__ == "__main__":
    main()




