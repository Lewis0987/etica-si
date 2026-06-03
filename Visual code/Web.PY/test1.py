from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException 
from colorama import Fore,Style
import time
import sys
import threading
import os
import configparser
import pyperclip
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
config = configparser.ConfigParser()
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
config_keyfile = os.path.join(current_dir, 'game.ini')
# 讀取配置文件
config.read(config_keyfile, encoding='utf-8')
################確認遊戲模板(請輸入 'U1、U2.../V1、V2...')###########################
ui_version = 'U1'
product_numbers = ['V7']
################確認帳號#######################################
phone='9999999888' #for 登入
# 初始化Chrome浏览器
driver = webdriver.Chrome()
# 打开网页
WebDriverWait(driver, 10)
for product in product_numbers:
    url = config.get(ui_version, product)
    driver.get(url)
    #網頁整頁
    driver.maximize_window()   
# 创建 WebDriver 对象

# A.[登入/註冊]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\033[107m\033[30m" + "A.[登入/註冊]" + "\033[0m")
#登入Popup
loginpopup = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Entrar')]"))
).click()
print('AA.loginpopup \033[32mOK\033[0m')
    #手機號
username_field = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.XPATH, "//*[contains(@type, 'number')]"))
    )
username_field.send_keys(phone)
print('1.輸入number \033[32mOK\033[0m')
    #密碼
inputotp_field = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.XPATH, "//*[contains(@type, 'password')]"))
    )
inputotp_field.send_keys("1111")
print('2.輸入password \033[32mOK\033[0m')
    #登入
enter_button = WebDriverWait(driver, 5).until(
EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Entrar')]")) #針對button的文字尋找
).click()
print('3.點擊button_Enter \033[32mOK\033[0m')
sleep(3)
print("\033[107m\033[30m" + "B.[首頁登入]" + "\033[0m")
#關閉Popup(1)_Convite Recompensa
close_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@alt, 'Close Icon')]"))
).click()
print('4.關閉彈窗_Convite Recompensa \033[32mOK\033[0m')
sleep(1)

#關閉Popup(2)_Equilíbrio insuficiente!
close_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@alt, 'Close Icon')]"))
).click()
print('5.關閉彈窗_Equilíbrio insuficiente! \033[32mOK\033[0m')
sleep(1)
#==========================================================================================

# 获取 Header 元素的位置信息
try:
    logomenu = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'logo-menu')]"))
    )
    print('logo-menu ok')

    header_location = logomenu.location_once_scrolled_into_view

# 获取 Banner 元素的位置信息
    banner_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//img[@alt='banner_2']"))
)
    banner_location = banner_element.location_once_scrolled_into_view

# 计算 Header 和 Banner 之间的垂直距离
    vertical_distance = banner_location['y'] - header_location['y']
    print(f"The vertical distance between Header and Banner is: {vertical_distance}px")
except TimeoutException:
    print("\033[91m" +"E.1-2.未找到包含元素"+ "\033[0m")
