import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.cge.cl/servicios-en-linea/oficina-virtual/")
driver.maximize_window()
time.sleep(3)
element = driver.find_element(By.ID, "navbarDropdown")



element = driver.find_element(By.ID, "txtRutLoginE").click()
    # 6 | type | id=txtRutLoginE | 1234123412
element = driver.find_element(By.ID, "txtRutLoginE").send_keys("1234123412")
    # 7 | click | id=txtClaveLoginE | 
element = driver.find_element(By.ID, "txtClaveLoginE").click()
    # 8 | type | id=txtClaveLoginE | asdasdasd
element = driver.find_element(By.ID, "txtClaveLoginE").send_keys("asdasdasd")
    # 9 | click | id=imbIngresarLogin | 
element = driver.find_element(By.ID, "imbIngresarLogin").click()












