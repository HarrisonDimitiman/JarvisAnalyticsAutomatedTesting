from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def netProduction(driver):
    # wait = WebDriverWait(driver, 120)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4')))

    driver.implicitly_wait(1000000000) 
    dayProd = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4").text
    clickMonth = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/ul/li[1]/a')
    clickMonth.click()
    getMonthProduction = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/span/div[1]/div[2]/div/div[6]/div/div[2]/h4").text
    print("FUCK SHIT")
    print("DAY PRODDD " + dayProd)
    print("MONTH SCHED AMOUNT " + getMonthProduction)
    
    return getMonthProduction
    
    
    