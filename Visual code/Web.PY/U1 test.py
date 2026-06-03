from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains ##模擬鼠標
from colorama import Fore, Style 
import time
import sys
import threading
import os
import configparser
import pyperclip
import re

# 單一網址開啟
''' 
################新安卓單(請輸入)###########################
url = "https://carnaval777bet.vip/"
################新安卓單(請輸入)###########################
driver.get(url)
WebDriverWait(driver, 10)
driver = webdriver.Chrome()
'''
# 多開網址開啟
'''
def main():
    # 初始化Chrome浏览器
    driver = webdriver.Chrome()

    for product in product_numbers:
        url = config.get(ui_version, product)
        sys.stdout.reset_counts() 

        # 打开网页
        driver.get(url)
        WebDriverWait(driver, 10)
        driver.maximize_window()
if __name__ == "__main__":
    main()
'''
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
    '''sys.stdout.reset_counts()''' # 計算print出的錯誤率
    driver.get(url)
    driver.maximize_window() # 網頁整頁   
sleep(3)   
# A.[登入/註冊]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\033[107m\033[30m" + "A.[登入/註冊]" + "\033[0m")
#登入Popup
loginpopup = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Entrar')]"))
).click()
print('AA.loginpopup \033[32mOK\033[0m')
# 手機號
username_field = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@type, 'number')]"))
)
username_field.send_keys(phone)
print('1.輸入number \033[32mOK\033[0m')

# 密碼
inputotp_field = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@type, 'password')]"))
)
inputotp_field.send_keys("1111")
print('2.輸入password \033[32mOK\033[0m')

# 登入
enter_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Entrar')]")) #針對button的文字尋找
).click()
print('3.點擊button_Enter \033[32mOK\033[0m')
sleep(3)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>A.[登入/註冊]完成
print("\033[102m\033[30m" + "A.[登入/註冊]完成" + "\033[0m")

# B.[首頁登入]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\033[107m\033[30m" + "B.[首頁登入]" + "\033[0m")
# 關閉Popup(1)_Convite Recompensa
close_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@alt, 'Close Icon')]"))
).click()
print('4.關閉彈窗_Convite Recompensa \033[32mOK\033[0m')
sleep(1)

# 關閉Popup(2)_Equilíbrio insuficiente!
close_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@alt, 'Close Icon')]"))
).click()
print('5.關閉彈窗_Equilíbrio insuficiente! \033[32mOK\033[0m')
sleep(1)

# 點擊refresh icon
try:
    refresh_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'refresh')]"))
).click()
    print('6.刷新_Balance \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"6.元素不存在"+ "\033[0m", e)
sleep(0.5)

# 循环点击刷新按钮N次
for p in range(3):
    driver.find_element(By.XPATH, "//img[contains(@alt, 'refresh')]").click()
    print(f'7.\033[34mBalance刷新 {p+1}次\033[0m \033[32m\u2713\033[0m') #{p+N}連續次數
sleep(0.5)

# 首頁logo
try:
    logomenu = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'logo-menu')]"))
).click()
    print('8.首頁logo \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"8.元素不存在"+ "\033[0m", e)
sleep(1) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>B.[首頁登入完成]
print("\033[102m\033[30m" + "B.[首頁登入 完成]" + "\033[0m")

# C.[Header bar]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\033[107m\033[30m" + "C.[Header bar]" + "\033[0m")
# header_遊戲(Jogos)
try:
    Jogos_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'Header__HeaderButtonText-sc-1kbky4o-2 bGMlmR') and text()='Jogos']"))
).click()
    print('9.header點擊 [Jogos] \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"9.元素不存在"+ "\033[0m", e)   

# header_遊戲(點擊Jogos_子選單點選Telegrama TG客服)
try:
    Telegramabutton_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Telegrama']"))
).click()
    print('10.導向Telegrama頁 \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"10.元素不存在"+ "\033[0m", e)
sleep(1) 

# header_遊戲(點擊Jogos_子選單點選Sobre nós 關於我們)
try:
    Sobrenósbutton_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Sobre nós']"))
).click()
    print('11.導向Sobre nós頁 \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"11.元素不存在"+ "\033[0m")  
    
# header_活動(Atividade)
Atividade_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'Header__HeaderButtonText-sc-1kbky4o-2 bGMlmR') and text()='Atividade']"))
).click()
print('12.header點擊 [Atividade] \033[32mOK\033[0m')

# header_活動(Atividades_子選單_點選Check in簽到)
checkin_element =WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.XPATH, "//button[text()='Check-in']"))
).click()
print('13.header點擊 [Check-in] \033[32mOK\033[0m')

# header_活動(Atividades_跳轉Check in簽到)
try:
    checkin_element = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'font-bold text-xl') and contains(text(), 'Regras de recompensa diária VIP')]"))
        )
    print('13-1.Check-in頁 \033[32mOK \033[0m')
except TimeoutException as e:
    print('\033[91m14.Check in 跳轉失敗 \033[0m') 

# header_活動(Atividades_子選單_點選Primeiro depósito 首存20%)
element = WebDriverWait(driver, 5).until( 
    EC.presence_of_element_located((By.XPATH,'//div[contains(text(), "Atividade")]')) #展開子選單
).click()
print("\033[35m展開 子選單 \033[0m")
Primeirodepósito_element = WebDriverWait(driver,5).until(
     EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Primeiro depósito')]"))
    ).click()
print('14.點擊header_Primeiro depósito \033[32mOK\033[0m')

# header_活動(Atividades_跳轉Primeiro depósito 首存20%)
try:
   Primeirodepósito = WebDriverWait(driver,5).until(
       EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'text-left w-full mb-1 leading-5 md:leading-7') and contains(text(), 'Detalhes do evento:')]"))
   ).click()
   print('14-1.跳轉首存20% \033[32mOK\033[0m')
except TimeoutException as e:
   print('\033[91m14-1.跳轉首存20% 失敗 \033[0m') 

# header_活動(Atividades_子選單_點選Recarregar Cashback 次存10%)
element = WebDriverWait(driver, 5).until( 
    EC.presence_of_element_located((By.XPATH,'//div[contains(text(), "Atividade")]')) #展開子選單
).click()
print("\033[35m展開 子選單 \033[0m")
RecarregarCashback_element=WebDriverWait(driver, 5).until(
   EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Recarregar Cashback')]"))
).click()
print('15.點擊header_Recarregar Cashback \033[32mOK\033[0m')  
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,'//img[@alt= "refresh"]')) #收合子選單
).click()
print("\033[36m收合 子選單 \033[0m")
# header_活動(Atividades_跳轉Recarregar Cashback 次存10%)
try:
    Primeirodepósito = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'text-2xl font-bold mb-4') and contains(text(), 'Recarga benefícios')]"))
    ).click()
    print('15-1.跳轉次存10% \033[32mOK\033[0m')
except TimeoutException as e:
    print('\033[91m15-1. 跳轉次存10% 失敗 \033[0m') 

# header_邀請(Convidar)
Convidar_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'Header__HeaderButtonText-sc-1kbky4o-2 bGMlmR') and text()='Convidar']"))
).click()
print('16.header點擊[Convidar] \033[32mOK\033[0m')
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,'//img[@alt= "refresh"]')) #收合子選單
).click()
print("\033[36m收合 子選單 \033[0m")

# header_邀請(Convidar_跳轉 邀請頁)
try:
    Convidar = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Como convidar usuários?']"))
    ).click()
    print('16-1.跳轉邀請頁 \033[32mOK\033[0m')
except TimeoutException as e:
    print('\033[91m15-1. 跳轉邀請頁 失敗 \033[0m') 

# header_VIP
VIP_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'Header__HeaderButtonText-sc-1kbky4o-2 bGMlmR') and text()='VIP']"))
).click()
print('17.header點擊[VIP] \033[32mOK\033[0m')
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,'//img[@alt= "refresh"]')) #收合子選單
).click()
print("\033[36m收合 子選單 \033[0m")

# header_(VIP_跳轉 邀請頁)
try:
    VIP = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'Header__HeaderButtonText-sc-1kbky4o-2 bGMlmR') and text()='VIP']"))
).click()
    print('17-1.跳轉VIP \033[32mOK\033[0m')
except TimeoutException as e:
    print('\033[91m17-1. 跳轉VIP 失敗 \033[0m') 

# header_Download
Download_element = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'Header__HeaderButtonText-sc-1kbky4o-2 bGMlmR') and text()='Download']"))
).click()
print('18.header點擊[Download] \033[32mOK\033[0m')

# header_(Download_彈出彈窗)
try:
    Download = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='jogos de cliente']"))
).click()
    print('18-1. DownLoad彈窗 彈出 \033[32mOK\033[0m')
except TimeoutException as e:
    print('\033[91m18-1. DownLoad彈窗 失敗 \033[0m') 

# header_邀請(Download_彈出彈窗>關閉)
close_Download_element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//img[@alt = "Close Icon"]'))
).click()
print('18-2. DownLoad彈窗關閉 \033[32mOK\033[0m')

# header_個人帳戶標籤 
Personal_account_element = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'flex gap-2 items-center')]"))
).click()
action = ActionChains(driver) ## 模擬鼠標
action.double_click(Convidar).perform() ## 双击鼠标左键 '''action.click(Convidar).perform() ## 單击鼠标左键''' 
print('19. header_個人帳戶icon 存在 \033[32mOK\033[0m')

# 個人帳戶視窗
try:
    Personal_account = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Total Da Conta']"))
)
    print('19-1. 個人帳戶彈出 \033[32mOK\033[0m')
except TimeoutException as e:
    print('\033[91m20-1. 個人帳戶彈出 失敗 \033[0m') 

# 個人帳戶標籤>關閉
Personal_account_element = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'flex gap-2 items-center')]"))
).click()
action = ActionChains(driver) ## 模擬鼠標
action.click(Convidar).perform() ## 双击鼠标左键 '''action.click(Convidar).perform() ## 單击鼠标左键''' 
print('19-2. 個人帳戶icon 關閉 \033[32mOK\033[0m')
'''
driver.refresh() ## 頁面刷新
print('頁面刷新(關閉帳戶視窗)')
sleep(1)
'''
# 回到首頁logo
try:
    logomenu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'logo-menu')]"))
).click()
    print('%%%. 回到首頁 \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"19.元素不存在"+ "\033[0m", e)

# header_點擊refresh icon
try:
    refresh_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'refresh')]"))
).click()
    print('22. header_點擊refresh icon \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"22. 元素不存在"+ "\033[0m", e)

# header_點擊充值icon[+] (判斷跳轉充值頁)
try: 
    充值icon_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'assets/u1/ic_add.png')]"))
).click()
    print('23. 跳轉充值頁 \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"23. 跳轉失敗(充值頁)"+ "\033[0m", e)
  
# 返回icon(Retornar)
try:
    back_button = WebDriverWait(driver, 5).until(
EC.element_to_be_clickable((By.XPATH, "//span[contains(@aria-label, 'left')]")) 
).click()
    print("\033[33m返回首頁 \033[0m")
except TimeoutException as e:
    print("\033[91m" +"返回 失敗"+ "\033[0m", e)

# header_點擊通知中心
notification_click = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'notification')]"))
).click()
print('24.header_點擊通知鈴icon \033[32mOK\033[0m')

# 通知中心列表
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

# 通知列表信件數量(未讀、已讀=總數量)
print("\033[44m\033[32m" + "25.通知列表信件數量" + "\033[0m")
notification_click = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, 'notification')]"))
).click()
try:
    ## 等待未讀信件元素出現
    unread_elements = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'NotificationItem__NotificationItemRedDot')]"))
    )
    ## 等待已讀信件元素出現(包含未讀元素存在=已讀總數量)
    read_elements = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'NotificationItem__NotificationItemTitle')]"))
    )

    ## 統計未讀信件數量(標記紅點)
    unread_count = len(unread_elements)
    print(f"25-1.未讀信件數量: \033[32m{unread_count}\033[0m")
    ## 統計已讀信件數量(未有紅點)
    read_count = len(read_elements) ##判斷已讀+未讀數量---顯示總數量
    read_counts = read_count - unread_count ##未有紅點 - 標記紅點
    print(f"25-2.已讀信件數量: \033[32m{read_counts}\033[0m")
    ## 計算總數量
    total_count = read_counts + unread_count
    print(f"25-3.總數量(未+已): \033[32m{total_count}\033[0m")

# 統計通知鈴的數量
    print("\033[44m\033[32m" + "26. 通知鈴數量" + "\033[0m")
    notification_icons = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'MessageCountBadge')]"))
        )
    bell_count = sum(int(icon.text) for icon in notification_icons)
    ## 通知鈴=通知列表數量
    print(f"26-1.通知鈴數量: \033[34m{bell_count}\033[0m")
# 判斷三項數量是否相等(總數量、通知鈴數量、未讀數量)
    if unread_count == bell_count != total_count:
        print("26-2.未讀數量、通知鈴數量皆相符，但不等於總數量\033[32m OK\033[0m")
    elif unread_count == bell_count == total_count:  ## 如果unread_count為False且bell_count為True，執行這裡的代碼
        print("26-2.未讀數量、通知鈴數量、總數量皆相符\033[32m OK\033[0m")
    else:
        print("26-2.\033[91m" +"三項皆不符"+ "\033[0m")
except Exception as e:
    print("\033[91m" +"出現異常"+ "\033[0m", e)
#關閉通知列表
notification_again_click = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Centro de Notificação']"))
).click()
print("\033[33m關閉帳戶視窗 \033[0m")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>C.[Header bar]完成
print("\033[102m\033[30m" + "C.[Header bar]完成" + "\033[0m")  

# D.[Account interface]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\033[107m\033[30m" + "D.[Account interface]" + "\033[0m")
#== 個人帳戶視窗 
Convidar = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'flex gap-2 items-center')]"))
)
action = ActionChains(driver) ## 模擬鼠標
action.double_click(Convidar).perform() ## 双击鼠标左键 
print('D.1.header_個人帳戶icon 存在 \033[32mOK\033[0m')

# 頭像區塊(尋找兩種元素增加準確性)
try:
    avatar = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//img[contains(@class,'rounded-[2px] w-[50px] h-[50px]') and @alt='avatar']"))
)
    print('D.2.展示頭像 \033[32mOK\033[0m')
except TimeoutException as e:
    print("\033[91m" +"D.2.找不到頭像元素"+ "\033[0m", e)

# 個人視窗ID Copy功能
Account_IDCopy = WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'active:opacity-50')]"))
).click()
print('D.3.點擊Copy \033[32mOK\033[0m')
try:
   IDCopy_message = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[(text() = 'Copiado!')]"))
)
   print('D.4.Copy文字訊息 \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"D.4.未跳文字訊息"+ "\033[0m")
try:
    Copy_content = pyperclip.paste() ##剪貼功能
    IDitems = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,'//div[@class="flex gap-2 text-lg items-center"]'))
            )
    Copy_text = IDitems.text
    number = re.search(r'\d+', Copy_text).group()
    if Copy_content == number:
        print('D.4-1.Copy成功訊息 \033[32mOK\033[0m') 
        print('複製的內容為: ' + Fore.BLUE +  Copy_content + Style.RESET_ALL)
    else:
        print("\033[91m" +"D.4.1.Copy功能失效"+ "\033[0m")
        print("\033[91m" +'複製的內容為: '+ "\033[0m" + Fore.YELLOW + Copy_content + Style.RESET_ALL) #針對此段文字調整色系[紅色標題+黃色複製內容]
except TimeoutException:
    print("\033[91m" +"D.4-1.未找到複製內容"+ "\033[0m")

# 個人帳戶_VIP區塊
VIPicon =  WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='currentVIP']"))
).click()
print('D.5.個人帳戶VIP區塊 點擊 \033[32mOK\033[0m')## 點擊VIP區塊
try: ## 檢查是否成功跳轉到 VIP 頁面
    VIP_element =  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Meu progresso VIP')]"))
)
    print('D.5-1.跳轉VIP頁 \033[32mOK\033[0m') 
except TimeoutException:
    print("\033[91m" +"D.5-1.跳轉失敗"+ "\033[0m")
#== 個人帳戶視窗
Convidar = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'flex gap-2 items-center')]"))
)
action = ActionChains(driver) ## 模擬鼠標
action.double_click(Convidar).perform() ## 双击鼠标左键 
print("\033[33m彈出個人帳戶視窗 \033[0m")

# 個人帳戶_充值區塊
BalançoTotal =  WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Depósito']"))
).click()
print('D.6.個人帳戶_充值 點擊 \033[32mOK\033[0m')
try: ## 檢查是否找到 充值 頁面元素
    VIP_element =  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Prezado usuário')]"))
)
    print('D.6-1.跳轉充值頁 \033[32mOK\033[0m') 
except TimeoutException:
    print("\033[91m" +"D.6-1.未找到包含元素"+ "\033[0m")
#== 個人帳戶視窗
Convidar = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'flex gap-2 items-center')]"))
)
action = ActionChains(driver) ## 模擬鼠標
action.double_click(Convidar).perform() ## 双击鼠标左键 
print("\033[33m彈出個人帳戶視窗 \033[0m")

# 個人帳戶_提現區塊
RetirávelTotal =  WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Retirar']"))
).click()
print('D.7.個人帳戶_提現 點擊 \033[32mOK\033[0m')
try: ## 檢查是否找到 提現 頁面元素
    VIP_element =  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Atualmente')]"))
)
    print('D.7-1.跳轉提現頁 \033[32mOK\033[0m') 
except TimeoutException:
    print("\033[91m" +"D.7-1.未找到包含元素"+ "\033[0m")
#== 個人帳戶視窗
Convidar = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'flex gap-2 items-center')]"))
)
action = ActionChains(driver) ## 模擬鼠標
action.double_click(Convidar).perform() ## 双击鼠标左键 
print("\033[33m彈出個人帳戶視窗 \033[0m")

# 個人帳戶_邀請區塊
ContaPromovida = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'rounded-t-xl')]"))
)
if ContaPromovida: #(針對相同元素判斷排序[value])
    ContaPromovida[1].click()
print('D.7.個人帳戶_邀請 點擊 \033[32mOK\033[0m')
try: ## 檢查是否找到 邀請 頁面元素
    VIP_element =  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Como convidar usuários?')]"))
)
    print('D.7-1.跳轉邀請頁 \033[32mOK\033[0m') 
except TimeoutException:
    print("\033[91m" +"D.7-1.未找到錯誤包含元素"+ "\033[0m")
#== 個人帳戶視窗
Convidar = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'flex gap-2 items-center')]"))
)
action = ActionChains(driver) ## 模擬鼠標
action.double_click(Convidar).perform() ## 双击鼠标左键 

# 個人帳戶_遊戲紀錄區塊
Registro =  WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Registro Do Jogo')]"))
).click()
print('D.8.個人帳戶_遊戲紀錄 點擊 \033[32mOK\033[0m')
try: ## 檢查是否找到 遊戲紀錄 頁面元素
    VIP_element =  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//th[contains(text(), 'Nome do jogo')]"))
)
    print('D.8-1.跳轉遊戲紀錄 \033[32mOK\033[0m') 
except TimeoutException:
    print("\033[91m" +"D.8-1.未找到包含元素"+ "\033[0m")
#== 個人帳戶視窗
Convidar = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'flex gap-2 items-center')]"))
)
action = ActionChains(driver) ## 模擬鼠標
action.double_click(Convidar).perform() ## 双击鼠标左键 

# 個人帳戶_修改個資區塊
Registro =  WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Modificar Dados')]"))
).click()
print('D.9.個人帳戶_修改個資 點擊 \033[32mOK\033[0m')
try: ## 檢查是否找到 遊戲紀錄 頁面元素
    VIP_element =  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Número de telefone')]"))
)
    print('D.9-1.跳轉修改個資 \033[32mOK\033[0m') 
except TimeoutException:
    print("\033[91m" +"D.9-1.未找到包含元素"+ "\033[0m")

##= 個人帳戶_修改個資頁
###手機號欄位
telefonetitle = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Número de telefone')]")))
print('D.10-1-1.修改個資頁_電話欄位  \033[32mOK\033[0m')
try:
    telefone = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '9999999888')]")))
    print('D.10-1-2.電話號碼:', Fore.GREEN + telefone.text + Style.RESET_ALL)
except TimeoutException:
    print("\033[91m" +"D.10-1-2.未找到包含元素"+ "\033[0m")

###暱稱(Nickname)
Apelido= WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Apelido')]")))
print('D.10-2-1.暱稱  \033[32mOK\033[0m')
try:
    Edit1 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Editar')]"))).click()
    print('D.10-2-2.暱稱 點擊 \033[32mOK\033[0m')

    Editconfirm = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Cancelar')]"))).click()
    print('D.10-2-3.[點擊] 取消頭像 \033[32mOK\033[0m')

    Edit2 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Editar')]"))).click()
    print('D.10-2-4.暱稱 點擊 \033[32mOK\033[0m')

    Editavatar = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'avatar1')]")))
    actions = ActionChains(driver) # 模擬滑鼠
    actions.move_to_element(Editavatar).click().perform()  # 将鼠标移动到元素上并点击
    print('D.10-2-5.[選擇] 頭像編輯  \033[32mOK\033[0m')

    Editconfirm = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Confirme')]"))).click()
    print('D.10-2-6.[點擊] 確認頭像 \033[32mOK\033[0m')

    Editdone =  WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Salvo com sucesso')]")))
    print('D.10-2-7.[完成] 編輯訊息  \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"D.10.2-x 未找到包含元素"+ "\033[0m")

###版本(View version)
versiontitle = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Verifique actualizações')]")))
print('D.10-3-1.修改個資頁_版本欄位  \033[32mOK\033[0m')
try:
    version = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '1.07.13')]")))
    print('D.10-3-2.版本:', Fore.YELLOW + version.text + Style.RESET_ALL)
except TimeoutException:
    print("\033[91m" +"D.10.2-x 版本錯誤"+ "\033[0m")

###隱私授權(Politica de Privacidade)
try:
    Politicatitle = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Politica de Privacidade')]"))).click()
    print('D.10-4-1.修改個資頁_隱私欄位  \033[32mOK\033[0m')
    
    Politica = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Privacy Policy and Personal Data Protection')]")))
    print('D.10-4-2.隱私授權頁 \033[32mOK\033[0m')
except TimeoutException:
    print("\033[91m" +"D.10.4-x 未找到包含元素"+ "\033[0m")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>C.[Header bar]完成
print("\033[102m\033[30m" + "D.[Account interface]完成" + "\033[0m") 

# 首頁logo
logomenu = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'logo-menu')]"))).click()
print('回首頁logo \033[32mOK\033[0m')

input('Press Enter to exit...')





