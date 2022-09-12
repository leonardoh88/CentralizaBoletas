import time
import json
from optparse import Option
import pandas as pd
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(executable_path=r"C:\\dchrome\\chromedriver.exe")

time.sleep(3)

driver.get("https://www.litoral.cl/empresa/resumen")



driver.maximize_window()
time.sleep(4)
element = driver.find_element(By.NAME, "nr_rut_empresa").send_keys("970300007")
time.sleep(2)
element = driver.find_element(By.NAME, "nr_rut_usuario").send_keys("970300007")
time.sleep(2)
element = driver.find_element(By.NAME, "password").send_keys("bestado")
time.sleep(3)

#Click para iniciar sesión

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    'button button-secondary button--small'.replace(' ', '.'))))\
    .click()

WebDriverWait(driver, 4)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    'i.icon-eye-blue.icon--left')))\
    .click()

WebDriverWait(driver, 4)\
    .until(EC.element_to_be_clickable((By.XPATH,
    '/html/body/main/section/div/div[4]/div[1]/div/div[1]/div[1]/table/tfoot/tr/td[4]/a')))\
    .click()

WebDriverWait(driver, 3)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    'i.icon-pdf')))\
    .click()
           
WebDriverWait(driver, 3)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    'i.iron-icon')))\
    .click()
    
WebDriverWait(driver, 4)\
    .until(EC.element_to_be_clickable((By.XPATH,
    '/html/body/pdf-viewer//viewer-toolbar//div/div[3]/viewer-download-controls//cr-icon-button//div/iron-icon')))\
    .click()