from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import configparser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
import time
import sys
config = configparser.ConfigParser()

# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
config_keyfile = os.path.join(current_dir, 'IN.ini')
# 讀取配置文件
config.read(config_keyfile, encoding='utf-8')
################確認遊戲模板(請輸入 'U1、U2.../V1、V2...')###########################
ui_version = 'IN'
product_numbers = ['INV5']
################確認帳號#######################################
phone1='9999999123' #for 登入
def main():
    ###更換成mobile
    mobileEmulation = {'deviceName': 'iPhone 12 Pro'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # 請更換成你的 Chrome 安裝路徑
    driver = webdriver.Chrome(options=options)
    
    for product in product_numbers:
        url = config.get(ui_version, product)
        '''sys.stdout.reset_counts()'''#用來清除紀錄或重置字元/位元組的計數
        # 打开网页
        driver.get(url)
        WebDriverWait(driver, 10)
        driver.maximize_window() #網頁整頁
        
#-------------------------1.首頁
        sleep(2)
            #首頁[notify popup]
        print("\033[107m\033[30m" + "A.[notify popup]" + "\033[0m")
        notifypopup = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Later')]"))
                ).click()
        print('A-1.notifypopup \033[32mOK\033[0m')
            #首頁[popup]
        sleep(0.5)
        notifypopup = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'flex justify-center items-center cursor-pointer')]"))
                ).click()
        print('A-2.首頁popupp \033[32mOK\033[0m')
            #首頁[Signup]
        signup = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Sign up')]"))
                ).click()
        try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Welcome")]'))
                )
                # 如果找到了元素，表示成功導向註冊頁
                print("A-3. 成功導向註冊\033[32mOK\033[0m")
                print("A-3. 找到元素，內容為:", div_element.text)                
        except TimeoutException:
                # 如果超时，表示登录失败
                print("\033[91m" +"1. 導向失败"+ "\033[0m")
        
            #-------------------------2.註冊模塊
        print("\033[107m\033[30m" + "2.註冊模塊" + "\033[0m")

        
        input('Press Enter to exit...')
       

#-------------------------1.登入/註冊模塊     
        print("\033[107m\033[30m" + "B.登入/註冊模塊" + "\033[0m")
                #header 首頁icon
        header = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "icon icon-ic_home")]'))
                ).click()
        try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "/images/v5/fab_add_default.webp")]'))
                )
                # 如果找到了元素，表示成功導向註冊頁
                print("A-3. 成功導向註冊\033[32mOK\033[0m")
                print("A-3. 找到元素，內容為:", div_element.text)                
        except TimeoutException:
                # 如果超时，表示登录失败
                print("\033[91m" +"1. 導向失败"+ "\033[0m")
        print('B.註冊 \033[32mOK\033[0m')
#<<<<<<<<<<<<<<<<<<<<<背景偵測popup，結束>>>>>>>>>>>>>>>>>>>>>>
sleep(10)
if __name__ == "__main__":
    main()



