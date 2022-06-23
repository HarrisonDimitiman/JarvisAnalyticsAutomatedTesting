from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from controller.figuresmatchingdriver.calendar import getcalendarmetricvalue
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(modules, metrics):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://solo.next.jarvisanalytics.com/')
    

    usernameXpath = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/form/div[1]/div/input')
    usernameXpath.send_keys('testryan')
    passwordXpath = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/form/div[2]/div[2]/input')
    passwordXpath.send_keys('Jarvis.123')
    loginButton = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/form/button')
    loginButton.click()

    for x in modules:
        print("---"+x)
        for y in metrics:
            if x == "Calendar":
                driver.get('https://solo.next.jarvisanalytics.com/calendar/appointments')
                if y == "Net Production":
                    try:
                        element = WebDriverWait(driver, 120).until(
                            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4"))
                        )
                    finally:
                        print("FUCK SHIT")
                    clickMonth = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/ul/li[1]')
                    clickMonth.click()
                    print("HELLO")
                    # calNetProdVal = getcalendarmetricvalue.netProduction(driver)
                if y == "Gross Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Gross Production "+y)
                if y == "Adjustment":
                    print("Nisulod Siya Sa Financial then ge Print ang Adjustment "+y)
            if x == "Dashboard":
                driver.get('https://solo.next.jarvisanalytics.com/solo/results')
                if y == "Net Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Net Production "+y)
                if y == "Gross Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Gross Production "+y)
                if y == "Adjustment":
                    print("Nisulod Siya Sa Financial then ge Print ang Adjustment "+y)
            if x == "Front Office":
                driver.get('https://solo.next.jarvisanalytics.com/front-office/schedule')
                if y == "Net Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Net Production "+y)
                if y == "Gross Production":
                    print("Nisulod Siya Sa Financial then ge Print ang Gross Production "+y)
                if y == "Adjustment":
                    print("Nisulod Siya Sa Financial then ge Print ang Adjustment "+y)

    driver.quit()

    # heyJude = "Let's Sing"
    # return heyJude

