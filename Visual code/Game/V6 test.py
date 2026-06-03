from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from colorama import Fore,Style
import os, time
import sys
import threading
import configparser
import pyperclip
import re
config = configparser.ConfigParser()

# 設定 ChromeOptions 

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": r"C:\Users\howar\Downloads",  # 你要的下載資料夾路徑
    "download.prompt_for_download": False,
    "directory_upgrade": True
}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)  # ✅ 錯誤時不自動關閉瀏覽器

# ====== 設定下載路徑 ======
download_path = r"C:\Users\howar\Downloads"

# ====== 初始化 Chrome Driver ======
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)  # ✅ 錯誤時不自動關閉瀏覽器

# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
config_keyfile = os.path.join(current_dir, 'IN.ini')
# 讀取配置文件
config.read(config_keyfile, encoding='utf-8')
################確認遊戲模板(請輸入 'U1、U2.../V1、V2...')###########################
ui_version = 'IN'
product_numbers = ['INV6']
################確認帳號#######################################
phone='8888888888' #for 登入
# 初始化Chrome浏览器
driver = webdriver.Chrome(service=Service(), options=options)
# 打开网页
WebDriverWait(driver, 10)
for product in product_numbers:
    url = config.get(ui_version, product)
    driver.get(url)
    driver.maximize_window() #網頁整頁

sleep(1)
#-------------------------1.A.首頁模塊 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A.首頁 Popup 
    # 首頁[Subscribe] 訂閱 
print('\033[33m首頁[Subscribe] 訂閱 \033[0m')
Subscribe =  WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Later')]"))
).click()
print('A-1.Subscribe_Later \033[32mOK\033[0m')


'''#首頁[surprise_reward_popup] 【1】>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\033[107m\033[30m" + "A.[首頁/popup]" + "\033[0m")
popup = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'popup_surprise_reward')]"))
).click()
print('A-1.surprise_reward popup \033[32mOK\033[0m')
try:
    popup = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'The reward has been claimed')]"))
    )
    print('A-1.已領取過獎勵toast \033[32mOK\033[0m')
        # 領取過獎勵重整網頁
    driver.refresh()
    sleep(3)
    try:
        popup = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'first_recharge_popup')]"))
        )
        print("A-1-1.點擊首充 popup \033[32mOK\033[0m")
         # 找到關閉按鈕並點擊
        close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
        print("A-1-1.【關閉】首充 popup \033[32mOK\033[0m")
    except TimeoutException:
        print("\033[93mA-1-1.未偵測到 ，可略過。\033[0m")
except TimeoutException:
        print("\033[93m" + "A-1.未偵測到已領取文字，繼續流程..." + "\033[0m")
'''

    #首頁[充值大輪盤_popup]【A】
print('\033[33m充值大輪盤【A】\033[0m')
try:
    popup = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'SPIN')]"))
    )
    print('A.Prize wheel_popup \033[32mOK\033[0m')
    
    sleep(1)
    try:
        popup = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'first_recharge_popup')]"))
        )
        print("A-1-1.點擊首充 popup \033[32mOK\033[0m")
         # 找到關閉按鈕並點擊
        close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
        print("A-1-1.【關閉】首充 popup \033[32mOK\033[0m")
    except TimeoutException:
        print("\033[94m模擬內彈.未偵測到 ，可略過。\033[0m")
    
    close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
    print("A-1-1.【關閉】首充 popup \033[32mOK\033[0m")
except TimeoutException:
        print("\033[94m" + "A-1.未偵測活動元素，繼續流程..." + "\033[0m")

sleep(0.5)
    #首頁[首充_popup]【2】
print('\033[33m首充Popup\033[0m')
try:
    popup = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'popup_first_recharge_vb')]"))
    )
    print('A-2.FirstRecharge_popup \033[32mOK\033[0m')
    
    sleep(1)
    try:
        popup = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'first_recharge_popup')]"))
        )
        print("A-1-1.首充 popup \033[32mOK\033[0m")
         # 找到關閉按鈕並點擊
        close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
        print("A-1-1.【關閉】首充 popup \033[32mOK\033[0m")
    except TimeoutException:
        print("\033[94m模擬內彈.未偵測到 ，可略過。\033[0m")
    
    close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
    print("A-1-1.【關閉】首充 popup \033[32mOK\033[0m")
except TimeoutException:
        print("\033[94m" + "A-1.未偵測活動元素，繼續流程..." + "\033[0m")

sleep(0.5)
    #首頁[mission_popup]【3】>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('\033[33mmission 任務中心 \033[0m')
try:
    popup = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-4 box-border')]"))
    )
    print('A-3.mission_popup \033[32mOK\033[0m')

    sleep(1)
    try:
        popup = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'first_recharge_popup')]"))
        )
        print("A-1-1.點擊首充 popup \033[32mOK\033[0m")
         # 找到關閉按鈕並點擊
        close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
        print("A-1-1.【關閉】首充 popup \033[32mOK\033[0m")
    except TimeoutException:
        print("\033[94m模擬內彈.未偵測到 ，可略過。\033[0m")

    close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
    print("A-3.【關閉】mission popup \033[32mOK\033[0m")
except TimeoutException:
        print("\033[94m" + "A-1.未偵測活動元素，繼續流程..." + "\033[0m")

sleep(0.5)
    #首頁[club_popup]【4】>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('\033[33mclub 俱樂部 \033[0m')

try:
    popup = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'popup_club')]"))
    )
    print('A-4.club popup \033[32mOK\033[0m') 
    sleep(3)
    try:
        popup = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'first_recharge_popup')]"))
        )
        print("A-1-1.點擊首充 popup \033[32mOK\033[0m")
         # 找到關閉按鈕並點擊
        close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
        print("A-1-1.【關閉】首充 popup \033[32mOK\033[0m")
    except TimeoutException:
        print("\033[94m模擬內彈.未偵測到 ，可略過。\033[0m")
        
    close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
    print("A-4.【關閉】popup_club \033[32mOK\033[0m")
except TimeoutException:
        print("\033[94m" + "A-4.未偵測活動元素，繼續流程..." + "\033[0m")


sleep(1)
    #首頁[telegram_popup]【5】>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
try:
    popup = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'popup_subscribe_telegram')]"))
)
    print('A-5.telegram popup \033[32mOK\033[0m')

    # 找到關閉按鈕並點擊
    close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
    print("A-5.關閉telegram popup \033[32mOK\033[0m")
except TimeoutException as e:
    print("A-5.telegram >>>> \033[91m" + "元素不存在" + "\033[0m", str(e).split("Stacktrace")[0]) # 只保留 Stacktrace 前的部分
    checked = True  # 防止重複執行

except Exception as e:
    print("\033[91mA-5 其他錯誤：\033[0m", str(e).split("Stacktrace")[0])                          # 只保留 Stacktrace 前的部分
    checked = True  # 防止重複執行

sleep(1)
    #首頁[Jackpot_popup]【6】>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
try:
    popup = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'popup_jackpot')]"))
)
    print('A-6.jackpot popup \033[32mOK\033[0m')

    # 找到關閉按鈕並點擊
    get_button = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
    print("A-6.關閉jackpot popup \033[32mOK\033[0m")
    
except TimeoutException as e:
    print("A-6.Jackpot >>>> \033[91m" + "元素不存在" + "\033[0m", str(e).split("Stacktrace")[0]) # 只保留 Stacktrace 前的部分
    checked = True  # 防止重複執行

except Exception as e:
    print("\033[91mA-6 其他錯誤：\033[0m", str(e).split("Stacktrace")[0])                         # 只保留 Stacktrace 前的部分
    checked = True  # 防止重複執行

sleep(1)
# B.1-1Header_download 【B】>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('\033[33mHeader_download區 \033[0m')

try:
    print("找到下載按鈕，準備點擊")
    before_files = set(os.listdir(download_path))
    
    download_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Download')]"))
    )
    download_btn.click()
    print("\033[32m已點擊下載按鈕\033[0m")

    time.sleep(3)  # 等新分頁或下載觸發

except Exception as e:
    print("\033[91m找不到下載按鈕：\033[0m", e)

# ====== 切換到新分頁（若有） ======
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])
    print(f"🔀 已切換到新分頁：{driver.current_url}")

# ====== 等待檔案出現 ======
def wait_for_download(download_path, before_files, timeout=20, auto_delete=True):
    print("📂 等待下載完成...")

    start_time = time.time()
    while time.time() - start_time < timeout:
        after_files = set(os.listdir(download_path))
        new_files = after_files - before_files

        # 排除還在下載中的檔案
        completed_files = [f for f in new_files if f.endswith(".apk")] # 刪除【.apk】 檔案
        '''completed_files = [f for f in new_files if not f.endswith(".crdownload")] ''' # 刪除下載檔案
        if completed_files:
            print(f"\033[32m✅ 下載完成：{completed_files}\033[0m")

            if auto_delete:
                for file in completed_files:
                    try:
                        os.remove(os.path.join(download_path, file))
                        print(f"\033[31m🗑️ 已刪除：\033[0m")
                    except Exception as e:
                        print(f"\033[91m⚠️ 無法刪除 {file}：{e}\033[0m")
            return True
        time.sleep(1)
    print("\033[91m❌ 下載失敗或超時\033[0m")
    return False

# 執行等待下載完成邏輯
wait_for_download(download_path, before_files)
'''try:
    popup = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Download')]"))
    )
    print('B-1.點擊【Download】 \033[32mOK\033[0m') 
    close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
    print("B-1.【關閉】popup_club \033[32mOK\033[0m")
except TimeoutException:
        print("\033[93m" + "A-1.未偵測到已領取文字，繼續流程..." + "\033[0m")
'''

    # B.1-2Header_download >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('\033[33mB.Close_download \033[0m')

try:
    # 等待並點擊關閉 download bar
    download_Close_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='ic_close_2']"))
    )
    print('B-1-2.download條 \033[32mOK\033[0m')
    download_Close_btn.click()
    print("B.1-2.【關閉】download條 \033[32mOK\033[0m")

    try:
        # 等待信封圖示出現後點擊
        no_download = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'ic_mail_unread')]"))
        )
        no_download.click()

        # 等待 Mail 選項出現後點擊
        mailbox = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Mail')]"))
        )
        mailbox.click()
        print("B-1-2.download條 不存在 \033[32mOK\033[0m")

        driver.back()
        print("回首頁 \033[32mOK\033[0m")
    except TimeoutException:
        print("\033[94m未偵測到信封或 Mail 元素，可略過。\033[0m")
        checked = True

    try: # 模擬觸發內彈
        popup = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'popup_first_recharge_vb')]"))
        )
        print("A-1-1.點擊首充 popup \033[32mOK\033[0m")
         # 找到關閉按鈕並點擊
        close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
        print("A-1-1.【關閉】首充 popup \033[32mOK\033[0m")
    except TimeoutException:
        print("\033[94m模擬內彈.未偵測到 ，可略過。\033[0m")
    
    '''    
    # 方法2 JS(Java Script)強制關閉 
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='ic_close_2']"))
    )
    driver.execute_script("arguments[0].click();", element)
    print("✅ JS 點擊關閉成功")
except Exception as e:
    print("❌ JS 點擊失敗：", str(e))
    '''
except TimeoutException as e:
    print("B.1-2.【關閉】download條 >>>> \033[91m元素不存在\033[0m", str(e).split("Stacktrace")[0])
    checked = True

except Exception as e:
    print("\033[91mB.1-2 其他錯誤：\033[0m", str(e).split("Stacktrace")[0])
    checked = True

 # B.1-3 Header_充值輪盤 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('\033[33mB.1-3.Header_充值輪盤 \033[0m')
checked = True
sleep(1)
try:
    # 等待並點擊關閉 download bar
    Luckywheel = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='ic_lucky_wheel']"))
    )
    print('B-1-3A.找到充值輪盤圖示 \033[32mOK\033[0m')
    checked = True
    '''
    if len(driver.find_elements(By.CSS_SELECTOR, "div.z-[1005]")) > 0:
        print("⛔ 有遮罩，跳過 Luckywheel 點擊")
    else:
        Luckywheel.click()
        print('B-1-3.點擊輪盤圖示 \033[32mOK\033[0m')
    '''
    sleep(0.5)
    Luckywheel = WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='ic_lucky_wheel']"))
    ).click()
    print('B-1-3B.點擊輪盤圖示 \033[32mOK\033[0m')

    sleep(0.5)
    try:
        # 進入充值輪盤頁面
        no_download = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Deposit Now')]"))
        )
        print("B-1-3C.充值輪盤頁面 \033[32mOK\033[0m")

        driver.back()
        print("回首頁 \033[32mOK\033[0m")   
    except TimeoutException as e:
        print("\033[94m未偵測到元素，可略過。\033[0m")
        checked = True
    

    try: # 模擬觸發內彈
        popup = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'first_recharge_popup')]"))
        )
        print("A-1-1.點擊首充 popup \033[32mOK\033[0m")
         # 找到關閉按鈕並點擊
        close_btn = driver.find_element(By.XPATH, "//img[@alt='ic_close']").click()
        print("A-1-1.【關閉】首充 popup \033[32mOK\033[0m")
    except TimeoutException:
        print("\033[94m模擬內彈.未偵測到 ，可略過。\033[0m")
    
except TimeoutException as e:
    print("B.1-3 >>>> \033[91m元素不存在\033[0m", str(e).split("Stacktrace")[0])
    checked = True
except Exception as e:
    print("\033[91mB.1-3 其他錯誤：\033[0m", str(e).split("Stacktrace")[0])
    checked = True

