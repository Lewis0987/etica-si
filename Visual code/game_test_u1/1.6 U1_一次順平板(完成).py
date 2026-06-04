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
from selenium.common.exceptions import TimeoutException, NoSuchWindowException,ElementClickInterceptedException
import time
import sys
import threading
import pyperclip
import re
#<<<<<<<<<<<<<<<<<<<<<背景偵測popup，並關閉>>>>>>>>>>>>>>>>>>>>>>
exit_event = threading.Event()
def handle_popups(driver):
    while not exit_event.is_set():
        try:
            # 在这里执行查找弹窗的操作
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Equilíbrio insuficiente!") or contains(text(), "Convide usuários limitados para compartilhar")]')))
            sleep(1)
            # 找到弹窗后执行关闭的操作
            close_button = driver.find_element(By.CSS_SELECTOR, '[alt="Close Icon"]')
            ActionChains(driver).move_to_element(close_button).click().perform()
            sleep(1)    
        except TimeoutException:
            # 超时异常，表示未找到弹窗，不输出错误信息
            pass
        except NoSuchWindowException:
            # 窗口已經被關閉，結束循環
            break
#<<<<<<<<<<<<<<<<<<<<<背景偵測popup，並關閉>>>>>>>>>>>>>>>>>>>>>>
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
product_numbers = ['V60']
################確認帳號#######################################
phone1='9999999000' #for 登入
def main():
    ###更換成mobile
    mobileEmulation = {'deviceName': 'iPad Mini'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # 請更換成你的 Chrome 安裝路徑
    driver = webdriver.Chrome(options=options)


    for product in product_numbers:
        url = config.get(ui_version, product)
        sys.stdout.reset_counts()

        # 打开网页
        driver.get(url)
        WebDriverWait(driver, 10)
#-------------------------1.登入模塊
        print("\033[107m\033[30m" + "1.登入模塊" + "\033[0m")
        #登入頁面
        element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Entrar")]'))
                ).click()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
            ).send_keys(phone1)
        element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
            ).send_keys('1111')
        sleep(0.5)
        button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
            ).click()
            # 尋找彈窗元素判斷是否登入
        try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Convide usuários limitados para compartilhar")]'))
                )
                # 如果找到了元素，表示登录成功
                print("1. 登入成功\033[32mOK\033[0m")
                
        except TimeoutException:
                # 如果超时，表示登录失败
                print("\033[91m" +"1. 登录失败"+ "\033[0m")
            #-------------------------2.popup模塊
        print("\033[107m\033[30m" + "2.popup模塊" + "\033[0m")
        try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Convide usuários limitados para compartilhar")]'))
                )
                print("2.1 邀請popup顯示\033[32mOK\033[0m")
        except TimeoutException:
                print("\033[91m" +"2.1 邀請popup未顯示"+ "\033[0m")
        sleep(0.5)
        element=WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'[alt="Close Icon"]'))
            ).click()
        try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Equilíbrio insuficiente!")]'))
                )
                print("2.2 充值popup顯示\033[32mOK\033[0m")
        except TimeoutException:
                print("\033[91m" +"2.2 充值popup不顯示"+ "\033[0m")
        sleep(0.5)
        element=WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'[alt="Close Icon"]'))
                ).click()
        
    #<<<<<<<<<<<<<<<<<<<<<背景偵測popup，開始>>>>>>>>>>>>>>>>>>>>>>
        popup_thread = threading.Thread(target=handle_popups, args=(driver,))
        popup_thread.start()
    #<<<<<<<<<<<<<<<<<<<<<背景偵測popup，開始>>>>>>>>>>>>>>>>>>>>>>
#-------------------------3.Side menu模塊
        print("\033[43m\033[30m" + "3.Side menu模塊" + "\033[0m")
#3.1 複製ID按鈕
        try:   
            print("\033[107m\033[30m" + "3.1 複製ID按鈕" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@data-icon= "copy"]'))
                        ).click()
            try:
                element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[text()="Copiado!"]')))
                print("3.1.1 複製ID按鈕 \033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.1.1 複製ID按鈕失效"+ "\033[0m")
            try:
                clipboard_content = pyperclip.paste()
                element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"user-code")]'))
                        )
                element_text = element.text
                number = re.search(r'\d+', element_text).group()
                if clipboard_content == number:
                    print("3.1.2 複製功能 \033[32mOK\033[0m")
                else:
                    print("\033[91m" +"3.1.2 複製功能失效"+ "\033[0m")
            except TimeoutException:
                print("未找到複製內容\033[0m")
#3.2. Telegram
            print("\033[107m\033[30m" + "3.2. Telegram" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[text()= "Canal De Telegram"]'))
                        ).click()
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Canal De")]'))
                )
                print("3.2.1 Telegram\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.2.1跳轉Telegram失敗"+ "\033[0m")
            # 记录初始窗口句柄
            initial_window_handle = driver.current_window_handle
            elements = driver.find_elements(By.XPATH, "//*[contains(@class,'TelegramPage')]")
            if elements:
                elements[0].click()
            # 等待新窗口打开
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            # 获取所有窗口句柄
            all_window_handles = driver.window_handles
            # 找到新窗口句柄
            new_window_handle = [handle for handle in all_window_handles if handle != initial_window_handle][0]
            # 切换到新窗口
            driver.switch_to.window(new_window_handle)
            # 这里可以进行新窗口中的操作
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.tgme_logo'))
                )
                print("3.2.2 Junte-se按鈕\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.2.2 Junte-se按鈕失效"+ "\033[0m")
            # 关闭新窗口
            driver.close()
            driver.switch_to.window(initial_window_handle)
            element=WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'[alt="Close Icon"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("3.2.3 Telegram返回鍵\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.2.3 Telegram返回鍵失效"+ "\033[0m")
#3.3 Primeiro depósito 20%
            print("\033[107m\033[30m" + "3.3 Primeiro depósito 20%" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[text()= "Primeiro depósito +20%"]'))
                        ).click()
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Primeira recarga")]'))
                )
                print("3.3.1 Primeiro depósito 20%\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.3.1 跳轉Primeiro depósito 20%失敗"+ "\033[0m")
            sleep(2)
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'ChargeButton')]"))
            ).click()
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"Balanço Total")]'))
                )
                print("3.3.2 引導至儲值頁\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.3.2 引導至儲值頁失敗"+ "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[text()= "Primeiro depósito +20%"]'))
                        ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("3.3.3 Primeiro depósito 20%返回鍵\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.3.3 Primeiro depósito 20%返回鍵失效"+ "\033[0m")
#3.4 Recarregar Cashback 10%
            print("\033[107m\033[30m" + "3.4 Recarregar Cashback 10%" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[text()= "Recarregar Cashback +10%"]'))
                        ).click()
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Recarga benefícios")]'))
                )
                print("3.4.1 Recarregar Cashback 10%\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.4.1 跳轉Recarregar Cashback 10%失敗"+ "\033[0m")
            sleep(1)
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'ChargeButton')]"))
            ).click()
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"Balanço Total")]'))
                )
                print("3.4.2 引導至儲值頁\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.4.2 引導至儲值頁失敗"+ "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[text()= "Recarregar Cashback +10%"]'))
                        ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("3.4.3 Recarregar Cashback 10%返回鍵\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.4.3 Recarregar Cashback 10%返回鍵失效"+ "\033[0m")
#3.5 Eventos
            print("\033[107m\033[30m" + "3.5 Eventos" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[contains(text(), "Eventos populares")]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Explorar Todas as Atividades")]'))
                )
                print("3.5.1 Eventos\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.5.1 跳轉Eventos失敗"+ "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("3.5.2 Sobre Nós返回鍵\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.5.2 Sobre Nós返回鍵失效"+ "\033[0m")
#3.6 Convidar模塊
            print("\033[107m\033[30m" + "3.6 Convidar模塊" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[contains(text(), "Bónus de Convite")]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
            # 检查第一个元素是否存在
                div_element_invite = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Instruções diárias de recompensa de comissão")]'))
            )
                print("3.6.1 Convidar模塊\033[32mOK\033[0m")
                print("\033[44m\033[97m" + "3.6 無接上寶箱" + "\033[0m")    
            except TimeoutException:
                try:
                # 检查第二个元素是否存在
                    div_element_link = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Link exclusivo")]'))
                )
                    print("3.6.1 Convidar模塊\033[32mOK\033[0m")
                    print("\033[44m\033[97m" + "3.6 無接上邀請" + "\033[0m")
                except TimeoutException:
                # 两个元素都不存在的情况
                    print("\033[91m" +"3.6 跳轉Convidar模塊失敗"+ "\033[0m")
#3.7 VIP模塊                    
            print("\033[107m\033[30m" + "3.7 VIP模塊" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//span[contains(text(), "Jogos")]'))
                ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[contains(text(), "Introdução ao nível VIP")]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Meu progresso VIP")]'))
                )
                print("3.7 VIP模塊\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.7 跳轉VIP模塊失敗"+ "\033[0m")
#3.8 複製網址鍵
            print("\033[107m\033[30m" + "3.8 複製網址鍵" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//span[contains(text(), "Jogos")]'))
                ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH,'//button[text()= "Cópia"]'))
                            ).click()
                try:
                    element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[text()="Copiado!"]')))
                    print("3.8.1 複製網址鍵 \033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"3.8.1 複製網址鍵失效"+ "\033[0m")
                try:
                    clipboard_content = pyperclip.paste()
                    element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH,'//*[contains(@class,"text-sm sm:text-base")]'))
                            )
                    element_text = element.text
                    if clipboard_content == element_text:
                        print("3.8.2 複製功能 \033[32mOK\033[0m")
                    else:
                        print("\033[91m" +"3.8.2 複製功能失效"+ "\033[0m")
                except TimeoutException:
                    print("未找到複製網址\033[0m")
            except TimeoutException:
                print("\033[44m\033[97m" + "未開通" + "\033[0m")
#3.9 Sobre Nós
            print("\033[107m\033[30m" + "3.9 Sobre Nós" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[contains(text(), "Sobre nós")]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Sobre Nós")]'))
                )
                print("3.9.1 Sobre Nós\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.9.1 跳轉Sobre Nós失敗"+ "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("3.9.2 Sobre Nós返回鍵\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.9.2 Sobre Nós返回鍵失效"+ "\033[0m")
#3.10 Gaming Curaçao
            print("\033[107m\033[30m" + "3.10 Gaming Curaçao" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//img[@alt= "menu"]'))
            ).click()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//p[contains(text(), "Gaming Curaçao")]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Licença De Curaçao")]'))
                )
                print("3.10.1 Gaming Curaçao\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.10.1 跳轉Gaming Curaçao失敗"+ "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("3.10.2 Sobre Nós返回鍵\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.10.2 Sobre Nós返回鍵失效"+ "\033[0m")
            print("\033[48;5;22m\033[97m" + "3.Side menu模塊OK" + "\033[0m")
#4.HEADER模塊 --------------------------------------          
            print("\033[43m\033[30m" + "4. HEADER模塊" + "\033[0m")
#4.1 餘額欄位
            print("\033[107m\033[30m" + "4.1 餘額欄位" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="refresh"]'))
                    )
            driver.execute_script("arguments[0].click();", element)
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "icon-loading")]'))
                )
                print("4.1.1 重刷按鈕\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"4.1.1 重刷按鈕失效"+ "\033[0m")
            element = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="add"]'))
                    )
            driver.execute_script("arguments[0].click();", element)
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"Balanço Total")]'))
                )
                print("4.1.2 引導至儲值頁\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"4.1.2 引導至儲值頁失敗"+ "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("4.1.3 儲值頁返回鍵\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"4.1.3 儲值頁返回鍵失效"+ "\033[0m")
#-------------------------4.2 通知中心
            print("\033[107m\033[30m" + "4.2 通知中心" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='notification']"))
                    )
            driver.execute_script("arguments[0].click();", element)
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"Centro de Notificação")]'))
                )
                print("4.2.1 通知中心\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"4.2.1  跳轉通知中心失敗"+ "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("4.2.2 通知中心返回鍵\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"4.2.2 通知中心返回鍵失效"+ "\033[0m")
            print("\033[48;5;22m\033[97m" + "4. HEADER模塊 OK" + "\033[0m")
#5.廣告banner模塊 --------------------------------------              
            print("\033[43m\033[30m" + "5.廣告banner模塊" + "\033[0m")
#5.1 首充20%banner
            '''
            print("\033[107m\033[30m" + "5.1 首充20%banner" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 1']"))
                    ).click()
            sleep(0.5)
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='h5_banner_2']"))
                    )
            actions = ActionChains(driver)
            actions.click(element).perform() 
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Primeira recarga")]'))
                )
                print("5.1 首充20%banner\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"5.1 點擊首充20%banner 失效"+ "\033[0m")
            
#5.2 充值10%banner
            print("\033[107m\033[30m" + "5.2 充值10%banner" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 2']"))
                    ).click()
            sleep(0.5)
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='h5_banner_1']"))
                    )
            actions = ActionChains(driver)
            actions.click(element).perform() 
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Recarga benefícios")]'))
                )
                print("5.2 充值10%banner\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"5.2 點擊充值10%banner 失效"+ "\033[0m")
#5.3 邀請banner
            print("\033[107m\033[30m" + "5.3 邀請banner" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 3']"))
                    ).click()
            sleep(0.5)
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='h5_banner_3']"))
                    )
            actions = ActionChains(driver)
            actions.click(element).perform() 
            try:
            # 检查第一个元素是否存在
                div_element_invite = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Como convidar usuários?")]'))
            )
                print("5.3 邀請banner模塊\033[32mOK\033[0m")
                print("\033[44m\033[97m" + "5.3 無接上寶箱" + "\033[0m")
            except TimeoutException:
                try:
                # 检查第二个元素是否存在
                    div_element_link = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Link exclusivo")]'))
                )
                    print("5.3 邀請banner模塊\033[32mOK\033[0m")
                    print("\033[44m\033[97m" + "5.3 無接上邀請" + "\033[0m")
                except TimeoutException:
                # 两个元素都不存在的情况
                    print("\033[91m" +"3.邀請banner模塊失敗"+ "\033[0m")
            '''
#5.4 VIP banner
            '''
            print("\033[107m\033[30m" + "5.4 VIP banner" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Jogos")]'))
                ).click()
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 4']"))
                    ).click()
            sleep(0.5)
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='h5_banner_4']"))
                    )
            actions = ActionChains(driver)
            actions.click(element).perform() 
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Meu progresso VIP")]'))
                )
                print("5.4 VIP banner\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"5.4 VIP banner 失效"+ "\033[0m")
            '''    
#5.5 報到banner
            '''
            print("\033[107m\033[30m" + "5.5 報到banner" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Jogos")]'))
                ).click()
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to slide 5']"))
                    ).click()
            sleep(0.5)
            element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='h5_banner_5']"))
                    )
            actions = ActionChains(driver)
            actions.click(element).perform() 
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Colete cupons")]'))
                )
                print("5.5 報到banner\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"5.5 報到banner 失效"+ "\033[0m")
            '''
            print("\033[48;5;22m\033[97m" + "5.廣告banner模塊 OK" + "\033[0m")
#6.Game_Filter --------------------------------------              
            print("\033[43m\033[30m" + "6.Game_Filter" + "\033[0m")
#6.1 Filter_slot
            print("\033[107m\033[30m" + "6.1 Filter_slot" + "\033[0m")
            element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//span[contains(text(), "Jogos")]'))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "ImageTab")]//span[contains(text(), "Slots")]'))
                )
                driver.execute_script("arguments[0].click();", element)
                # 在点击后，尝试查找下一个元素，找到则执行相应的操作
                try:
                    div_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "-Slots")]'))
                    )
                    print("6.1 Filter_slot\033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"6.1 點擊Filter_slot失敗"+ "\033[0m")

            except TimeoutException:
                # 找不到第一个元素的处理
                print("\033[44m\033[97m" + "6.1 無接上slot" + "\033[0m")
#6.2 Filter_Fishing
            print("\033[107m\033[30m" + "6.2 Filter_Fishing" + "\033[0m")
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ImageTab")]//span[contains(text(), "Fishing")]'))
                )
                driver.execute_script("arguments[0].click();", element)
                
                # 在点击后，尝试查找下一个元素，找到则执行相应的操作
                try:
                    div_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "-Fishing")]'))
                    )
                    print("6.2 Filter_Fishing\033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"6.2  點擊Filter_Fishing失敗"+ "\033[0m")

            except TimeoutException:
                # 找不到第一个元素的处理
                print("\033[44m\033[97m" + "6.2 無接上Fishing" + "\033[0m")
#6.3 Filter_Viver
            print("\033[107m\033[30m" + "6.3 Filter_Viver" + "\033[0m")
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ImageTab")]//span[contains(text(), "Viver")]'))
                )
                driver.execute_script("arguments[0].click();", element)
                # 在点击后，尝试查找下一个元素，找到则执行相应的操作
                try:
                    div_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "-Viver")]'))
                    )
                    print("6.3 Filter_Viver\033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"6.3  點擊Filter_Viver失敗"+ "\033[0m")

            except TimeoutException:
                # 找不到第一个元素的处理
                print("\033[44m\033[97m" + "6.3 無接上Viver" + "\033[0m")
#6.4 Filter_Arcades
            print("\033[107m\033[30m" + "6.4 Filter_Arcades" + "\033[0m")
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "ImageTab")]//span[contains(text(), "Arcades")]'))
                )
                # 使用 execute_script 方法点击元素
                driver.execute_script("arguments[0].click();", element)
                # 在点击后，尝试查找下一个元素，找到则执行相应的操作
                try:
                    div_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "-Arcade")]'))
                    )
                    print("6.4 Filter_Arcades\033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"6.4  點擊Filter_Arcades失敗"+ "\033[0m")

            except TimeoutException:
                # 找不到第一个元素的处理
                print("\033[44m\033[97m" + "6.4 無接上Arcades" + "\033[0m")
#6.5 Filter_Tables
            print("\033[107m\033[30m" + "6.5 Filter_Tables" + "\033[0m")
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "ImageTab")]//span[contains(text(), "Tables")]'))
                )
                # 使用 execute_script 方法点击元素
                driver.execute_script("arguments[0].click();", element)
                # 在点击后，尝试查找下一个元素，找到则执行相应的操作
                try:
                    div_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "-Tables")]'))
                    )
                    print("6.5 Filter_Tables\033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"6.5 點擊Filter_Tables失敗"+ "\033[0m")

            except TimeoutException:
                # 找不到第一个元素的处理
                print("\033[44m\033[97m" + "6.5 無接上Tables" + "\033[0m")
#6.6 Filter_Cards
            print("\033[107m\033[30m" + "6.6 Filter_Cards" + "\033[0m")
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "ImageTab")]//span[contains(text(), "Cards")]'))
                )
                # 使用 execute_script 方法点击元素
                driver.execute_script("arguments[0].click();", element)
                
                # 在点击后，尝试查找下一个元素，找到则执行相应的操作
                try:
                    div_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "-Cards")]'))
                    )
                    print("6.6 Filter_Cards\033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"6.6 點擊Filter_Cards失敗"+ "\033[0m")

            except TimeoutException:
                # 找不到第一个元素的处理
                print("\033[44m\033[97m" + "6.6 無接上Cards" + "\033[0m")
#6.7 Filter_Bingo
            print("\033[107m\033[30m" + "6.7 Filter_Bingo" + "\033[0m")
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "ImageTab")]//span[contains(text(), "Bingo")]'))
                )
                # 使用 execute_script 方法点击元素
                driver.execute_script("arguments[0].click();", element)


                # 在点击后，尝试查找下一个元素，找到则执行相应的操作
                try:
                    div_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "-Bingo")]'))
                    )
                    print("6.7 Filter_Bingo\033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"6.7 點擊Filter_Bingo失敗"+ "\033[0m")

            except TimeoutException:
                # 找不到第一个元素的处理
                print("\033[44m\033[97m" + "6.7 無接上Bingo" + "\033[0m")
#6.8 Filter_Others
            print("\033[107m\033[30m" + "6.8 Filter_Others" + "\033[0m")
            try:
                element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "ImageTab")]//span[contains(text(), "Others")]'))
                )
                driver.execute_script("arguments[0].click();", element)

                # 在点击后，尝试查找下一个元素，找到则执行相应的操作
                try:
                    div_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "-Others")]'))
                    )
                    print("6.8 Filter_Others\033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"6.8 點擊Filter_Others失敗"+ "\033[0m")
            except TimeoutException:
                # 找不到第一个元素的处理
                print("\033[44m\033[97m" + "6.8 無接上Bingo" + "\033[0m")
#6.9.Filter_Todos
            print("\033[107m\033[30m" + "6.9.Filter_Todos" + "\033[0m")
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ImageTab")]//span[text()= "Todos"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Slots")]'))
                )
                print("6.9 Filter_Todos\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"6.9 點擊Filter_Todos失敗"+ "\033[0m")
#6.10 Filter_Favoritos
            print("\033[107m\033[30m" + "6.10 Filter_Favoritos" + "\033[0m")            
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ImageTab")]//span[contains(text(), "Favoritos")]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Favoritos")]'))
                )
                print("6.10 Filter_Favoritos\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"6.10 點擊Filter_Favoritos失敗"+ "\033[0m")
#6.11 搜尋欄位
            print("\033[107m\033[30m" + "6.11 搜尋欄位" + "\033[0m")
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "InputSection")]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[text()= "Procurar"]'))
                )
                print("6.11.1 搜尋欄位\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"6.11.1 點擊搜尋欄位失敗"+ "\033[0m")
            sleep(0.5)
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Close Icon']"))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("6.11.2 Telegram返回鍵\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"6.11.2 Telegram返回鍵失效"+ "\033[0m")
            print("\033[48;5;22m\033[97m" + "6.Game_Filter OK" + "\033[0m")
#7.footer --------------------------------------              
            print("\033[43m\033[30m" + "7.footer" + "\033[0m")
            # Click on Jogo
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Jogo']"))
            )
            driver.execute_script("arguments[0].click();", element)
            def Footer(driver, category_name, button_text, filter_text):     
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print(f"\033[107m\033[30m{category_name}\033[0m")
                try:
                    #判斷是否接上Slots
                    element = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located(
                            (By.XPATH, f'//button[contains(text(), "{button_text}")]')
                        ))
                    driver.execute_script("arguments[0].click();", element)
                    sleep(1) 
                    #判斷是否檢查到BANNER下方的點，以判斷是否置頂
                    try:
                        # 尝试点击第一个元素
                        div_element = WebDriverWait(driver, 2).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Go to slide 1']"))
                        ).click()
                        print(f"\033[91m{category_name}置頂失效\033[0m")
                    except (TimeoutException, ElementClickInterceptedException):
                        # 如果点击第一个元素超时，则尝试点击第二个元素
                        try:
                            element = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "InputSection")]'))
                            )
                            element.click()
                            print(f"{category_name}置頂\033[32mOK\033[0m")

                        except (TimeoutException, ElementClickInterceptedException):
                            # 如果点击第二个元素超时，则表示两个元素都无法点击
                            print(f"\033[91m{category_name}置頂失效\033[0m")
                    try:
                        WebDriverWait(driver, 2).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Close Icon']"))
                            ).click()             
                    except (TimeoutException, ElementClickInterceptedException):
                        pass   
                    #判斷Slots_filter功能
                    try:
                            div_element = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{filter_text}")] | //div[contains(text(), "{filter_text}")]'))) 
                            print(f"{category_name}filter \033[32mOK\033[0m")
                    except TimeoutException:
                            print(f"\033[91m{category_name}失效\033[0m")
                except TimeoutException:
                    # 元素未出现
                    print(f"\033[44m\033[97m{category_name}無接上\033[0m")
            Footer(driver, "7.1 Jogo_Slots", "Slots", "-Slots")
            Footer(driver, "7.2 Jogo_Fishing", "Fishing", "-Fishing")
            Footer(driver, "7.3 Jogo_Cards", "Cards", "-Cards")
            Footer(driver, "7.4 Jogo_Arcades", "Arcades", "-Arcade")
            Footer(driver, "7.5 Jogo_Bingo", "Bingo", "-Bingo")
            Footer(driver, "7.6 Jogo_Tables", "Tables", "-Table")
            Footer(driver, "7.7 Jogo_Viver", "Viver", "-Viver")
            Footer(driver, "7.8 Jogo_Others", "Others", "-Others")
            Footer(driver, "7.9 Jogo_Salão", "Salão", "Slots")
#7.10 Ajuda_Politica de Privacidade
            def Footer1(driver, category_name, button_text, filter_text): 
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print(f"\033[107m\033[30m{category_name}\033[0m")
                
                # 點擊具體的遊戲按鈕
                element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located(
                    (By.XPATH, f'//button[contains(text(), "{button_text}")]')
                ))
                driver.execute_script("arguments[0].click();", element)
                sleep(1)    
                try:
                    div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{filter_text}")] | //div[contains(text(), "{filter_text}")]'))) 
                    print(f"{category_name}\033[32mOK\033[0m")
                except TimeoutException:
                    print(f"\033[91m{category_name}失败\033[0m")
                sleep(1)
                current_scroll_position = driver.execute_script("return window.pageYOffset;")
                if current_scroll_position == 0:
                    print(f"{category_name}置頂功能\033[32mOK\033[0m")
                else:
                    print(f"\033[91m{category_name}置頂功能失败\033[0m")
                    
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Ajuda']"))
            )
            driver.execute_script("arguments[0].click();", element)
            Footer1(driver, "7.10.1 Politica de Privacidade", "Politica de Privacidade", "Privacy Policy")
#7.11 Termos de Servico
            Footer1(driver, "7.11.1 Termos de Servico", "Termos de Servico", "ALL USERS OF")
            driver.back() 
            sleep(1.5)
#7.12 Descrico do nivel VIP
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Ajuda']"))
            )
            driver.execute_script("arguments[0].click();", element)
            Footer1(driver, "7.12.1 Descrico do nivel VIP", "Descrico do nivel VIP", "Meu progresso VIP")
#7.13 外網連結_Skrill            
            print("\033[107m\033[30m" + "7.13 外網連結_Skrill  " + "\033[0m")
            element = driver.find_element(By.XPATH,'//span[contains(text(), "Jogos")]')
            driver.execute_script("arguments[0].click();", element)
            element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//span[contains(text(), "Jogos")]'))
                )
            driver.execute_script("arguments[0].click();", element)
            # Click on Jogo
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            initial_window_handle = driver.current_window_handle
            element=WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'footer3')]"))
                )
            driver.execute_script("arguments[0].click();", element)
            all_window_handles = driver.window_handles
            new_window_handle = [handle for handle in all_window_handles if handle != initial_window_handle][0]
            driver.switch_to.window(new_window_handle)
            # 等待新窗口的标题元素出现
            new_window_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "title"))
            )
            # 获取新窗口的标题
            new_window_title_text = new_window_title.get_attribute("textContent")
            if "Carteira online" in new_window_title_text:
                print("7.13 外網連結_Skrill 頁面 \033[32mOK\033[0m")
            else:
                print("\033[91m" +"7.13 跳轉外網連結_Skrill失效"+ "\033[0m")
            # 关闭新窗口
            driver.close()
            # 切换回原始窗口
            driver.switch_to.window(initial_window_handle)
#7.14 外網連結_BeGambleAware           
            print("\033[107m\033[30m" + "7.14 外網連結_BeGambleAware" + "\033[0m")
            # Click on Jogo
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            initial_window_handle = driver.current_window_handle
            element=WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'footer5')]"))
                )
            driver.execute_script("arguments[0].click();", element)
            all_window_handles = driver.window_handles
            new_window_handle = [handle for handle in all_window_handles if handle != initial_window_handle][0]
            driver.switch_to.window(new_window_handle)
            # 等待新窗口的标题元素出现
            new_window_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "title"))
            )
            # 获取新窗口的标题
            new_window_title_text = new_window_title.get_attribute("textContent")
            if "GambleAware®" in new_window_title_text:
                print("7.14 外網連結_BeGambleAware頁面 \033[32mOK\033[0m")
            else:
                print("\033[91m" +"7.14 外網連結_BeGambleAware失效"+ "\033[0m")
            # 关闭新窗口
            driver.close()
            # 切换回原始窗口
            driver.switch_to.window(initial_window_handle)
#7.15 外網連結_Interac          
            print("\033[107m\033[30m" + "7.15 外網連結_Interac " + "\033[0m")
            # Click on Jogo
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            initial_window_handle = driver.current_window_handle
            element=WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'footer6')]"))
                )
            driver.execute_script("arguments[0].click();", element)
            all_window_handles = driver.window_handles
            new_window_handle = [handle for handle in all_window_handles if handle != initial_window_handle][0]
            driver.switch_to.window(new_window_handle)
            # 等待新窗口的标题元素出现
            new_window_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "title"))
            )
            # 获取新窗口的标题
            new_window_title_text = new_window_title.get_attribute("textContent")
            if "Home - Interac" in new_window_title_text:
                print("7.15  外網連結_Interac 頁面 \033[32mOK\033[0m")
            else:
                print("\033[91m" +"7.15  跳轉外網連結_Interac失效"+ "\033[0m")
            # 关闭新窗口
            driver.close()
            # 切换回原始窗口
            driver.switch_to.window(initial_window_handle)
#7.16 外網連結_GamCare       
            print("\033[107m\033[30m" + "7.16 外網連結_GamCare " + "\033[0m")
            # Click on Jogo
            
            initial_window_handle = driver.current_window_handle
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt,'footer4')]"))
            )
            driver.execute_script("arguments[0].click();", element)
            all_window_handles = driver.window_handles
            new_window_handle = [handle for handle in all_window_handles if handle != initial_window_handle][0]
            driver.switch_to.window(new_window_handle)

            # 等待新窗口的标题元素出现
            new_window_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "title"))
            )
            # 获取新窗口的标题
            new_window_title_text = new_window_title.get_attribute("textContent")
            if "GamCare" in new_window_title_text:
                print("7.16 外網連結_GamCare 頁面 \033[32mOK\033[0m")
            else:
                print("\033[91m" + "7.16 跳轉外網連結_GamCare 頁面失效" + "\033[0m")

            # 关闭新窗口
            driver.close()
            # 切换回原始窗口
            driver.switch_to.window(initial_window_handle)
#7.17 Footer_icon_Gaming Curaçao
            print("\033[107m\033[30m" + "7.17 Footer_icon_Gaming Curaçao" + "\033[0m")
            element=WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "img[src='/license.06fdfd1ababef6ef.png']"))
                )
            driver.execute_script("arguments[0].click();", element)
            sleep(1)
            scroll_position = driver.execute_script("return window.scrollY;")

            # 判斷滾動位置是否為 0（頁面頂部）
            if scroll_position == 0:
                print("7.17.1 Footer_icon_Gaming Curaçao置頂\033[32mOK\033[0m")
            else:
                print("\033[91m" +"7.17.1 Footer_icon_Gaming Curaçao置頂失效"+ "\033[0m")
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Gaming Curaçao')]"))
                )
                print("7.17.2 Footer_icon_Gaming Curaçao\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"7.17.2 Footer_icon_Gaming Curaçao失效"+ "\033[0m")
            driver.back()
            sleep(3)      
#7.18 Footer文案收合
            print("\033[107m\033[30m" + "7.18 Footer文案收合" + "\033[0m")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            element=WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Mostrar']"))
                )
            driver.execute_script("arguments[0].click();", element) 
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Colocar fora")]'))
                )
                print("7.18 Footer文案收合\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"7.18 Footer文案收合失效"+ "\033[0m")
            print("\033[48;5;22m\033[97m" + "7. Footer模塊OK" + "\033[0m")
#8. 浮動按鈕模塊 --------------------------------------          
            print("\033[43m\033[30m" + "8. 浮動按鈕模塊" + "\033[0m")
#8.1 添加桌面按鈕
            print("\033[107m\033[30m" + "8.1 添加桌面按鈕" + "\033[0m")
            try:
                element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Clique em Adicionar ao ecrã principal']"))
                )
                driver.execute_script("arguments[0].click();", element) 
                try:
                    div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Adicione à tela inicial")]'))
                )
                    print("8.1 添加桌面按鈕引導說明頁\033[32mOK\033[0m")
                except TimeoutException:
                    print("\033[91m" +"8.1.1 添加桌面按鈕引導說明頁失敗"+ "\033[0m")
            except TimeoutException:
                print("\033[91m" +"8.1.1 添加桌面按鈕未顯示"+ "\033[0m")
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Jogos")]'))
                )
            action = ActionChains(driver)
            action.click(element).perform()
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='close']"))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                    div_element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Clique em Adicionar ao ecrã principal")]'))
                )
                    print("\033[91m" +"8.1.2 添加桌面按鈕x icon失敗"+ "\033[0m")
            except TimeoutException:
                    print("8.1.2 添加桌面按鈕x icon\033[32mOK\033[0m")
#8.2 Download按鈕
            print("\033[107m\033[30m" + "8.2 Download按鈕" + "\033[0m")
            element=WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='download']"))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Baixar Android")]'))
                )
                print("8.2.1 Download按鈕\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"8.2.1 Download按鈕失效"+ "\033[0m")
            element=WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='Close Icon']"))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Baixar Android")]'))
                )
                print("\033[91m" +"8.2.2 Download按鈕 X icon失效"+ "\033[0m")
            except TimeoutException:
                print("8.2.2 Download按鈕 X icon\033[32mOK\033[0m")
#8.3 Telegram按鈕
            print("\033[107m\033[30m" + "8.3 Telegram按鈕" + "\033[0m")
            # 记录初始窗口句柄
            initial_window_handle = driver.current_window_handle
            element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//img[@alt='telegram']"))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Clique no ícone para pular")]'))
                )
                print("8.3.1 Telegram按鈕\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"8.3.1 Telegram按鈕"+ "\033[0m")
            elements = driver.find_elements(By.XPATH, "//span[@class='anticon anticon-right']")
            if elements:
                elements[0].click()
            # 等待新窗口打开
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            # 获取所有窗口句柄
            all_window_handles = driver.window_handles
            # 找到新窗口句柄
            new_window_handle = [handle for handle in all_window_handles if handle != initial_window_handle][0]
            # 切换到新窗口
            driver.switch_to.window(new_window_handle)
            # 这里可以进行新窗口中的操作
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.tgme_logo'))
                )
                print("8.3.2 Telegram_Serviço按鈕\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"8.3.2 Telegram_Serviço按鈕失效"+ "\033[0m")
            # 关闭新窗口
            driver.close()
            # 切换回原始窗口
            driver.switch_to.window(initial_window_handle)
            # 记录初始窗口句柄
            initial_window_handle = driver.current_window_handle
            element = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//img[@alt='telegram']"))
                )
            driver.execute_script("arguments[0].click();", element)
            elements = driver.find_elements(By.XPATH, "//span[@class='anticon anticon-right']")
            if elements:
                elements[1].click()
            # 等待新窗口打开
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            # 获取所有窗口句柄
            all_window_handles = driver.window_handles
            # 找到新窗口句柄
            new_window_handle = [handle for handle in all_window_handles if handle != initial_window_handle][0]
            # 切换到新窗口
            driver.switch_to.window(new_window_handle)
            # 这里可以进行新窗口中的操作
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.tgme_logo'))
                )
                print("8.3.3 Telegram_Gerente按鈕\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"8.3.3 Telegram_Gerente按鈕失效"+ "\033[0m")
            # 关闭新窗口
            driver.close()
            # 切换回原始窗口
            driver.switch_to.window(initial_window_handle)
            element = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//img[@alt='telegram']"))
                )
            driver.execute_script("arguments[0].click();", element)
            element = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//img[@alt='Close Icon']"))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 1).until_not(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Clique no ícone para pular")]'))
                )
                print("8.3.4 Telegram按鈕 x icon\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"8.3.4 Telegram按鈕 x icon失效"+ "\033[0m")
            print("\033[48;5;22m\033[97m" + "8. 浮動按鈕模塊OK" + "\033[0m")
#9. 導航bar --------------------------------------          
            print("\033[43m\033[30m" + "9. 導航bar " + "\033[0m")
#9.1 導航bar_Convidar
            print("\033[107m\033[30m" + "9.1 導航bar_Convidar" + "\033[0m")            
            element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//span[contains(text(), "Convidar")]'))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Instruções diárias de recompensa de comissão")]'))
                )
                print("9.1 導航bar_Convidar\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"9.1 導航bar_Convidar失敗"+ "\033[0m")
#9.2 導航bar_VIP
            print("\033[107m\033[30m" + "9.2 導航bar_VIP" + "\033[0m")            
            element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//span[contains(text(), "VIP")]'))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Meu progresso VIP")]'))
                )
                print("9.2 導航bar_VIP\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"9.2 導航bar_VIP失敗"+ "\033[0m")
#9.3 導航bar_Minha
            print("\033[107m\033[30m" + "9.3 導航bar_Minha" + "\033[0m")            
            element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//span[contains(text(), "Minha")]'))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Outras funções")]'))
                )
                print("9.3 導航bar_Minha\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"9.3 導航bar_Minha失敗"+ "\033[0m")
#9.4 導航bar_Jogos
            print("\033[107m\033[30m" + "9.4 導航bar_Jogos" + "\033[0m")            
            element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//span[contains(text(), "Jogos")]'))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Todos")]'))
                )
                print("9.4 導航bar_Jogos\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"9.4 導航bar_Jogos失敗"+ "\033[0m")
#9.5 導航bar_Eventos
            print("\033[107m\033[30m" + "9.4 導航bar_Eventos" + "\033[0m")            
            element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//span[contains(text(), "Eventos")]'))
                )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Explorar Todas as Atividades")]'))
                )
                print("9.5 導航bar_Eventos\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"9.5 導航bar_Eventos失敗"+ "\033[0m")
            print("\033[48;5;22m\033[97m" + "9. 導航bar OK" + "\033[0m")            
            # 打印统计结果和带颜色的百分比
            total_percentage = sys.stdout.total_count / sys.stdout.total_count * 100
            green_percentage = sys.stdout.green_count / sys.stdout.total_count * 100
            red_percentage = sys.stdout.red_count / sys.stdout.total_count * 100
            print("測試項目"+ "\033[93m"f"{ui_version}{product}"+"\033[0m")
            print(f"總測試筆數: {sys.stdout.total_count} ({total_percentage:.2f}%)")
            print(f"\033[32m測試成功筆數: {sys.stdout.green_count} ({green_percentage:.2f}%)\033[0m")
            print(f"\033[91m測試失敗筆數: {sys.stdout.red_count} ({red_percentage:.2f}%)\033[0m")
    #<<<<<<<<<<<<<<<<<<<<<背景偵測popup，結束>>>>>>>>>>>>>>>>>>>>>>
        except TimeoutException:
                pass
        finally:
                exit_event.set()
                popup_thread.join() 
#<<<<<<<<<<<<<<<<<<<<<背景偵測popup，結束>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    main()
