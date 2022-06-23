from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def netProduction(driver):
    # wait = WebDriverWait(driver, 120)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4')))
    try:
        element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4"))
        )
    finally:
        print("FUCK SHIT")
    clickMonth = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/ul/li[1]')
    clickMonth.click()
    print("HELLO")
    