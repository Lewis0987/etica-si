from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options ##模擬Mobile
from selenium.webdriver.support import expected_conditions as EC
import os
import configparser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException 
import time
import sys
import threading
import pyperclip
import re
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
phone1='9999999888' #for 登入

#========================================================================================================================================================================
#啟動Mobile FOR Chrome
# 定義裝置模擬參數
mobile_emulation = {"deviceName": "iPhone 12 Pro"}
# 設置 Chrome 選項
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# 啟動 Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
# 打開要測試的網站
driver.get("https://carnaval777bet.vip") 
#========================================================================================================================================================================
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

sleep(5)
    #A.[登入/註冊]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\033[107m\033[30m" + "A.[登入/註冊]" + "\033[0m")

''' #登入頁
enter_button = WebDriverWait(driver, 5).until(
EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Entrar')]")) #針對span的文字尋找
).click()
print('3.點擊登入頁_Enter \033[32mOK\033[0m')'''
    #登入Popup
loginpopup = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Entrar')]"))
).click()
print('AA.loginpopup \033[32mOK\033[0m')
    #手機號
username_field = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.XPATH, "//*[contains(@type, 'number')]"))
    )
username_field.send_keys("9999999888")
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
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#首頁Banner=============================================================================
print("\033[44m\033[32m" + "E.a 首頁Banner" + "\033[0m") 
#=首充20%
actions = ActionChains(driver)
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 1']"))
        ).click()
print('E.1-1.banner_首頁20% \033[32mOK\033[0m')
sleep(0.5)
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='banner_1']"))
        )
actions.click(element).perform()
print('E.1-2.banner_首頁20% \033[32mOK\033[0m')
try:
    inside1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Primeira recarga')]")))
    print('E.1-3.內頁_首充20% \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.1-3.未找到包含元素"+ "\033[0m")
driver.back()

#=次充10%
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 2']"))
        ).click()
print('E.2-1.banner_次充10% \033[32mOK\033[0m')
sleep(0.5)
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='banner_2']"))
        )
actions.click(element).perform()
print('E.2-2.banner_次充10% \033[32mOK\033[0m')
try:
    inside2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Recarga benefícios')]")))
    print('E.2-3.內頁_次充10% \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.2-3.未找到包含元素"+ "\033[0m")
driver.back()

#=邀請
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 3']"))
        ).click()
print('E.3-1.banner_邀請 \033[32mOK\033[0m')
sleep(0.5)
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='banner_3']"))
        )
actions.click(element).perform() 
print('E.3-2.banner_邀請 \033[32mOK\033[0m')
try:
    inside3 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Como convidar usuários?')]")))
    print('E.3-2.內頁邀請 \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"E.3-2.未找到包含元素"+ "\033[0m")
driver.back()

#=VIP
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 4']"))
        ).click()
print('E.4-1.banner_VIP \033[32mOK\033[0m')
sleep(0.5)

element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='banner_4']"))
        )
actions.click(element).perform() 
print('E.4-2.banner_VIP \033[32mOK\033[0m')
try:
    inside4 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Meu progresso VIP')]")))
    print('E.4-3.內頁VIP \033[32mOK\033[0m')
except TimeoutException: 
    pass
    print("\033[91m" +"E.4-3.未找到包含元素"+ "\033[0m")
driver.back()
sleep(1)

#=簽到(check in)
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 5']"))
        ).click()
print('E.5-1.banner_VIP \033[32mOK\033[0m')
sleep(0.5)
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='banner_5']"))
        )
actions = ActionChains(driver)
actions.click(element).perform() 
print('E.5-2.banner簽到 \033[32mOK\033[0m')
try:
    inside5 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'visualizar registros >')]")))
    print('E.5-3.內頁簽到 \033[32mOK\033[0m')
except TimeoutException:
    pass
    print("\033[91m" +"E.5-3.未找到包含元素"+ "\033[0m")

#header_點擊通知中心
notification_click= WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'notification')]"))
).click()
print('24.header_點擊通知鈴icon \033[32mOK\033[0m')

#通知中心列表
try:
    notification_list = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Centro de Notificação']"))
)
    print('24-1.開啟通知列表 \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"找不到元素"+ "\033[0m", e)


#關閉通知列表
notification_again_click = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Centro de Notificação']"))
).click() #次點擊通知列表
try:
    Close_notification = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder,'Pesquisar nome do jogo')]"))
)
    print('24-2.回到首頁 \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"24-2.顯示錯誤"+ "\033[0m", e)
  

#=====================================================


# 通知列表信件數量(未讀、已讀=總數量)
print("\033[44m\033[32m" + "25.通知列表信件數量" + "\033[0m")
try:
    # 等待未讀信件元素出現
    unread_elements = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'NotificationItem__NotificationItemRedDot')]"))
    )
    # 等待已讀信件元素出現(包含未讀元素存在=已讀總數量)
    read_elements = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'NotificationItem__NotificationItemTitle')]"))
    )

    # 統計未讀信件數量(標記紅點)
    unread_count = len(unread_elements)
    print(f"25-1.未讀信件數量: \033[32m{unread_count}\033[0m")
    # 統計已讀信件數量(未有紅點)
    read_count = len(read_elements) ##判斷已讀+未讀數量---顯示總數量
    read_counts = read_count - unread_count ##未有紅點 - 標記紅點
    print(f"25-2.已讀信件數量: \033[32m{read_counts}\033[0m")
    # 計算總數量
    total_count = read_counts + unread_count
    print(f"25-3.總數量(未+已): \033[32m{total_count}\033[0m")
    input('Press Enter to exit...')

# 統計通知鈴的數量
    print("\033[44m\033[32m" + "26. 通知鈴數量" + "\033[0m")
    notification_icons = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'MessageCountBadge')]"))
        )
    bell_count = sum(int(icon.text) for icon in notification_icons)
    #通知鈴=通知列表數量
    print(f"26-1.通知鈴數量: \033[34m{bell_count}\033[0m")
# 判斷三項數量是否相等(總數量、通知鈴數量、未讀數量)
    if unread_count == bell_count == total_count:
        print("26-2.總數量、通知鈴數量、未讀數量皆相符\033[32mOK\033[0m")
    elif unread_count == bell_count != total_count:  ## 如果condition1為False且condition2為True，執行這裡的代碼
        print("26-2.未讀數量、通知鈴數量皆相符\033[32m OK\033[0m")
    else:
        print("26-2.\033[91m" +"三項數量皆不符"+ "\033[0m")
except Exception as e:
    print("\033[91m" +"出現異常"+ "\033[0m", e)

# 初始化已讀和未讀計數
    read_count = 0
    unread_count = 0

    # 遍歷每個通知元素，計算已讀和未讀數量
    for notification in notifications:
        # 檢查通知是否標記為已讀
        red_unread = notification.find_element(By.XPATH, "//div[contains(@class, 'flex-between fixed right-0 top-[44px] bottom-0 flex w-[450px] flex-col bg-[var(--background-primary)] p-4 text-left')]").is_displayed()
        if red_unread:
            unread_count += 1
        else:
            read_count += 1

    # 打印已讀和未讀數量
    print("已讀數量:", read_count)
    print("未讀數量:", unread_count) 
except TimeoutException:
    print("找不到通知列表元素。")

input('Press Enter to exit...')




