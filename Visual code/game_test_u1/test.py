from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import configparser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException 
import time
import sys
###VVVVVVVVVVV計算print出的錯誤率VVVVVVVVVVVVVVVVV##############
class ColorPrintCounter:
    def __init__(self):
        self.total_count = 0
        self.red_count = 0
        self.green_count = 0

    def write(self, text):
        sys.__stdout__.write(text)
        color_codes = ["\033[32m", "\033[91m"]
        for color_code in color_codes:
            if color_code in text:
                self.total_count += 1
                if color_code == "\033[32m":
                    self.green_count += 1
                elif color_code == "\033[91m":
                    self.red_count += 1

    def flush(self):
        sys.__stdout__.flush()
    def reset_counts(self):
        self.total_count = 0
        self.red_count = 0
        self.green_count = 0
sys.stdout = ColorPrintCounter()
###^^^^^^^^^^^^計算print出的錯誤率^^^^^^^^^^^^^^^^^^#############
config = configparser.ConfigParser()
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
config_keyfile = os.path.join(current_dir, 'game.ini')
# 讀取配置文件
config.read(config_keyfile, encoding='utf-8')
################確認遊戲模板(請輸入 'U1、U2.../V1、V2...')###########################
ui_version = 'U1'
product_numbers = ['VV']
################確認遊戲模板(請輸入 'U1、U2.../V1、V2...')###########################
# 初始化Chrome浏览器
driver = webdriver.Chrome()

for product in product_numbers:
    url = config.get(ui_version, product)
    sys.stdout.reset_counts()
    driver.get(url)
    WebDriverWait(driver, 10)
    driver.maximize_window()


    print("\033[43m\033[30m" + "1.提現" + "\033[0m")
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
    ).send_keys('99999990000')
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
    ).send_keys('1111')
    button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
    ).click()
    sleep(2)
    
    #111111111111111111111111
    button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@alt= "notification"]'))
    ).click()
    elements = driver.find_elements(By.XPATH, "//*[contains(@class,'NotificationItemRedDot')]")
    count = len(elements)
    print("符合条件的元素数量:", count)





    
    sleep(10)
