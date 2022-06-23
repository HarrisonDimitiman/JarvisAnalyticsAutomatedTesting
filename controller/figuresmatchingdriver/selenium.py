from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from controller.figuresmatchingdriver.calendar import getcalendarmetricvalue
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(modules, metrics):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://mb2.stage.jarvisanalytics.com/')
    

    usernameXpath = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/form/div[1]/div/input')
    usernameXpath.send_keys('harristestadmin')
    passwordXpath = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/form/div[2]/div[2]/input')
    passwordXpath.send_keys('qa')
    loginButton = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/form/button')
    loginButton.click()

    for x in modules:
        print("---"+x)
        for y in metrics:
            if x == "Financials":
                driver.get('https://mb2.stage.jarvisanalytics.com/financial/summary')
                if y == "Net Production":
                    calNetProdVal = getcalendarmetricvalue.netProduction(driver)
                if y == "Gross Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Gross Production "+y)
                if y == "Adjustment":
                    print("Nisulod Siya Sa Financial then ge Print ang Adjustment "+y)
            if x == "Operations":
                driver.get('https://mb2.stage.jarvisanalytics.com/operations/offices')
                if y == "Net Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Net Production "+y)
                if y == "Gross Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Gross Production "+y)
                if y == "Adjustment":
                    print("Nisulod Siya Sa Financial then ge Print ang Adjustment "+y)
            if x == "Dashboard":
                driver.get('https://mb2.stage.jarvisanalytics.com/dashboard')
                if y == "Net Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Net Production "+y)
                if y == "Gross Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Gross Production "+y)
                if y == "Adjustment":
                    print("Nisulod Siya Sa Financial then ge Print ang Adjustment "+y)

    driver.quit()

    # heyJude = "Let's Sing"
    # return heyJude

