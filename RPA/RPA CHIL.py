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
driver.get("http://www.chilquinta.cl")
driver.maximize_window()
time.sleep(7)
element = driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .btn-sv").click()
time.sleep(5)
element = driver.find_element(By.NAME, "username").send_keys("97030000-7")
time.sleep(5)
element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/form/div[1]/div/input[2]").send_keys("chilquinta")
time.sleep(5)
element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/form/button[1]").click()



