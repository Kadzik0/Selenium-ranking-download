from re import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime

currTime=datetime.now().strftime(r"%Y%m%d%H%M")
print(currTime)

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

options = Options()
# options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
driver.get("https://valium.pl")

driver.maximize_window()

searchInputLogin = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div/div/div[1]/form/div[1]/input')
searchInputLogin.send_keys('buff100lvl')

searchInputPassword = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div/div/div[1]/form/div[2]/input')
searchInputPassword.send_keys('ascobol123;')

searchButtonSubmit = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div/div/div[1]/form/div[3]/button')
searchButtonSubmit.click()

searchButtonRanking = driver.find_element(By.XPATH, '/html/body/header/div[1]/ul/li[3]/a')
searchButtonRanking.click()

searchButtonDungeons = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div/div[2]/div[2]/div[2]/a')
searchButtonDungeons.click()

searchButtonComboBox = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div/select/option[11]')
searchButtonComboBox.click()

searchButtonShowBtn = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div[2]/div[2]/form/div/div[2]/input')
searchButtonShowBtn.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.save_screenshot(f'{currTime}_jotunRanking.png')

# time.sleep(3)
driver.quit()