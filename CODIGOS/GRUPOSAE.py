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





driver.get("https://www.gruposaesa.cl/hogar/oficina-virtual/mi-perfil/mis-boletas/")






driver.maximize_window()
time.sleep(4)
element = driver.find_element(By.NAME, "rut_login").send_keys("76.181.492-3")
time.sleep(2)
element = driver.find_element(By.NAME, "contrasena_login").send_keys("tu22")
time.sleep(3)

#Click para iniciar sesión


WebDriverWait(driver, 4)\
    .until(EC.element_to_be_clickable((By.XPATH,
    '/html/body/div[1]/div[5]/div[2]/form/fieldset/div/input')))\
    .click()


WebDriverWait(driver, 4)\
    .until(EC.element_to_be_clickable((By.XPATH,
    '/html/body/div[1]/div[4]/div/div/div[1]/div/span')))\
    .click()




WebDriverWait(driver, 4)\
    .until(EC.element_to_be_clickable((By.XPATH,
    '/html/body/div[1]/div[2]/ul[1]/li[3]/a')))\
    .click()

WebDriverWait(driver, 4)\
    .until(EC.element_to_be_clickable((By.XPATH,
    '/html/body/div/div[2]/ul[2]/li[5]/a')))\
    .click()



WebDriverWait(driver, 4)\
    .until(EC.element_to_be_clickable((By.XPATH,
    '/html/body/div/div[2]/div[3]/div/table/tbody/tr[1]/td[7]/a')))\
    .click()