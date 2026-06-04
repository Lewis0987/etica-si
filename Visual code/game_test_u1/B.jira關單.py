from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import configparser

# 启动 Chromedriver
driver = webdriver.Chrome()
################測試完畢QA單(請輸入)###########################
url = "http://jira.he-x-tech.com:8080/browse/QA-11407"
################測試完畢QA單(請輸入)###########################

driver.get(url)
WebDriverWait(driver, 10)
#帳號
driver.find_element(By.CSS_SELECTOR, "#login-form-username").send_keys("roger")
#密碼
driver.find_element(By.CSS_SELECTOR, "#login-form-password").send_keys("1qaz234%")
#登入
driver.find_element(By.XPATH, "//*[contains(@value, '登录')]").click()
#主單關閉測試
driver.find_element(By.CSS_SELECTOR, "#action_id_41").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, "#action_id_51").click()
#批量關閉子任務
elements = driver.find_elements(By.XPATH, '//span[text()="选项"]')
if len(elements) > 1:
    elements[1].click()

driver.find_element(By.XPATH, "//*[contains(@title, '批量操作')]").click()
#全選
driver.find_element(By.CSS_SELECTOR, "#bulkedit-select-all").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
sleep(1)
#轉換問題
driver.find_element(By.XPATH, "//*[contains(@value, 'bulk.workflowtransition.operation.name')]").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
#轉換開始測試
driver.find_element(By.XPATH, "//*[contains(@value, 'Software Simplified Workflow for Project QA_41_3')]").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
sleep(10)

driver.get(url)
WebDriverWait(driver, 10)
#批量關閉子任務
elements = driver.find_elements(By.XPATH, '//span[text()="选项"]')
if len(elements) > 1:
    elements[1].click()

driver.find_element(By.XPATH, "//*[contains(@title, '批量操作')]").click()
#全選
driver.find_element(By.CSS_SELECTOR, "#bulkedit-select-all").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
sleep(1)
#轉換問題
driver.find_element(By.XPATH, "//*[contains(@value, 'bulk.workflowtransition.operation.name')]").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
#轉換開始測試
driver.find_element(By.XPATH, "//*[contains(@value, 'Software Simplified Workflow for Project QA_51_10001')]").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
driver.find_element(By.CSS_SELECTOR, "#next").click()
sleep(10)
#關閉[新包]單
driver.find_element(By.CSS_SELECTOR, ".issue-link.link-title.resolution").click()
sleep(1)
#關閉測試
driver.find_element(By.CSS_SELECTOR, "#action_id_41").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, "#action_id_51").click()
driver.quit()