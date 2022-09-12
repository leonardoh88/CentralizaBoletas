import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
import pandas as pd
import os


driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

driver.get("http://www.chilquinta.cl")

driver.maximize_window()
time.sleep(5)
element = driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .btn-sv").click()
time.sleep(3)
element = driver.find_element(By.NAME, "username").send_keys("97030000-7")
time.sleep(2)
element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/form/div[1]/div/input[2]").send_keys("chilquinta")
time.sleep(2)
element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/form/button[1]").click()
time.sleep(5)



WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    'button.close')))\
        .click()

time.sleep(5)
element = driver.find_element(By.ID, "navbarDropdown")
time.sleep(3)
element = driver.find_element(By.LINK_TEXT, "PAGAR FACTURAS PENDIENTES").click()
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) a:nth-child(2) .svg-inline--fa").click()
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR, "/html/body/pdf-viewer//viewer-toolbar//div/div[3]/viewer-download-controls//cr-icon-button//div/iron-icon").click()
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[9]/div/div/a[2]/span/svg").click()


