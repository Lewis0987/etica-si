from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

# 開啟本地 HTML 頁面
file_path = f"file:///{os.getcwd()}/login.html"
driver = webdriver.Chrome()
# 打开网页
driver.maximize_window() #網頁整頁
driver.get(file_path)    #透過路徑啟動

# 輸入帳號和密碼
driver.find_element(By.ID, "username").send_keys("Lewis")
driver.find_element(By.ID, "password").send_keys("1111")

input('Press Enter to exit...')
# 點擊登入按鈕
'''driver.find_element(By.ID, "loginBtn").click()'''
# 點擊取消按鈕
driver.find_element(By.ID, "cancelBtn").click()

sleep(2)

# 等待用户输入后关闭浏览器(確保瀏覽器不關閉)
input()
input('Press Enter to exit...')

