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

config = configparser.ConfigParser()
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
config_keyfile = os.path.join(current_dir, 'game.ini')
# 讀取配置文件
config.read(config_keyfile, encoding='utf-8')
################確認遊戲模板(請輸入 'U1、U2.../V1、V2...')###########################
ui_version = 'IN'
product_numbers = ['V6']
################確認帳號#######################################
phone='8888888888' #for 登入
# 初始化Chrome浏览器
driver = webdriver.Chrome()
# 打开网页
WebDriverWait(driver, 10)
for product in product_numbers:
    url = config.get(ui_version, product)
    driver.get(url)
    driver.maximize_window() #網頁整頁


'''
def main():
    for product in product_numbers:
        url = config.get(ui_version, product)
        sys.stdout.reset_counts()

        # 打开网页
        driver.get(url)
        WebDriverWait(driver, 10)
        #網頁整頁
        driver.maximize_window()
if __name__ == "__main__":
    main()
'''
sleep(3)
    #A.[登入/註冊]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\033[107m\033[30m" + "A.[登入/註冊]" + "\033[0m")
    #登入Popup
loginpopup = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Entrar')]"))
).click()
print('A.loginpopup \033[32mOK\033[0m')
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
#===================================================================================================

driver.refresh()
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
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# E.[首頁/內頁Banner]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\033[107m\033[30m" + "E.[首頁/內頁Banner]" + "\033[0m")
#首頁Banner=============================================================================
print("\033[44m\033[32m" + "E.a 首頁Banner" + "\033[0m") 
#=首充20%
Banner1_Firstrecharge = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Go to slide 1')]"))
    ).click()
print('E.1-1.首充20% \033[32mOK\033[0m') 
banner1 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='banner_1']"))
        ).click()
actions = ActionChains(driver)
actions.click(banner1).perform() 
print('banner1')
sleep(1)

#=次充10%
Banner2_Secondaryrecharge  = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Go to slide 2')]"))
    ).click()
print('E.2-1.次充10% \033[32mOK\033[0m')
banner2 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='banner_2']"))
)

driver.execute_script("arguments[0].click();", banner2)
actions.click(banner2).perform() 
print('banner2')
sleep(1)

#=邀請
Banner3_invite = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Go to slide 3')]"))
    ).click()
print('E.3-1.邀請 \033[32mOK\033[0m')
banner3 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='banner_3']"))
)

driver.execute_script("arguments[0].click();", banner3)
print('banner3')
sleep(1)

#=VIP
Banner4_VIP = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Go to slide 4')]"))
    ).click()
print('E.4-1.VIP \033[32mOK\033[0m')
banner4 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='banner_4']"))
)

driver.execute_script("arguments[0].click();", banner4)
print('banner4')
sleep(1)

#=簽到
Banner5_checkin = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Go to slide 5')]"))
    ).click()
print('E.5-1.簽到check in \033[32mOK\033[0m')
banner5 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='banner_5']"))
)

driver.execute_script("arguments[0].click();", banner5)
print('banner5')

try:
    inside5 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'visualizar registros >')]")))
    print('E.5-2.內頁簽到 \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.5-2.未找到包含元素"+ "\033[0m")
'''
##內頁Insidebanner=============================================================================
print("\033[44m\033[32m" + "E.b 內頁Insidebanner" + "\033[0m") 

#=首充 20% 
Banner1_Firstrecharge = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to slide 1']"))
        ).click()
print('首充 20% ')
sleep(0.5)
banner1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='banner_1']"))
        )
actions = ActionChains(driver)
actions.click(banner1).perform() 
print('actions_首充 20% ')
try:
    inside1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Primeira recarga')]")))
    print('E.1-2.內頁首充 20% \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.1-2.未找到包含元素"+ "\033[0m")
driver.back()

#=次充 10% 
Banner2_Secondaryrecharge = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to slide 2']"))
        ).click()
print('次充 20% ')
sleep(0.5)
banner2 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='banner_2']"))
        )
actions = ActionChains(driver)
actions.click(banner2).perform() 
try:
    inside2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Recarga benefícios')]")))
    print('E.2-2.內頁次充 10% \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.2-2.未找到包含元素"+ "\033[0m")
driver.back()

#=邀請
Banner3_Secondaryrecharge = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to slide 3']"))
        ).click()
print('邀請')
sleep(0.5)
banner3 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='banner_3']"))
        )
actions = ActionChains(driver)
actions.click(banner3).perform() 
try:
    inside3 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Como convidar usuários?')]")))
    print('E.3-2.內頁邀請 \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.3-2.未找到包含元素"+ "\033[0m")
driver.back()

#=VIP
Banner4_Secondaryrecharge = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to slide 4']"))
        ).click()
print('VIP')
sleep(0.5)
banner4 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='banner_4']"))
        ).click()
actions = ActionChains(driver)
actions.click(banner4).perform() 
try:
    inside4 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Meu progresso VIP')]")))
    print('E.4-2.內頁VIP \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.4-2.未找到包含元素"+ "\033[0m")
driver.back()

for p in range(10):
        driver.find_element(By.XPATH, "//button[@aria-label='Go to next slide").click()
        print(f'7.\033[34mnext banner {p+1}次\033[0m \033[32m\u2713\033[0m') #{p+N}連續次數
# 循环点击刷新按钮N次


#nextbanner3
sleep(0.5)
banner3 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='banner_3']"))
        )
actions = ActionChains(driver)
actions.click(banner3).perform() 
try:
    inside3 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Como convidar usuários?')]")))
    print('E.3-2.內頁邀請 \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.3-2.未找到包含元素"+ "\033[0m")
driver.back()


#=簽到
Banner5_Secondaryrecharge = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to slide 5']"))
        ).click()
print('簽到')
banner5 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='banner_5']"))
        ).click()
actions = ActionChains(driver)
actions.click(banner5).perform() 
print('簽到actions')

wait = WebDriverWait(driver, 10)
banner5 = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='banner_5']")))
banner5.click() 
actions = ActionChains(driver)
actions.move_to_element(banner5).perform()
banner5.click()
try:
    inside5 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'visualizar registros >')]")))
    print('E.5-2.內頁簽到 \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.5-2.未找到包含元素"+ "\033[0m")
driver.back()
'''
input('Press Enter to exit...')

#離開修改個人頁
back = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@aria-label, 'left')]"))
).click()
print('BACK \033[32mOK\033[0m') 


#= 個人帳戶視窗
Convidar = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(@alt,'phone')]"))
)
action = ActionChains(driver) ## 模擬鼠標
action.double_click(Convidar).perform() ## 双击鼠标左键 
input('Press Enter to exit...')









