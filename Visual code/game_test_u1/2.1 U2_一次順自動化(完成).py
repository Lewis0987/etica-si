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
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
import time
import sys
from Method import TestHelper,handle_popups#TestHelper是class
import threading
###VVVVVVVVVVV計算print出的錯誤率VVVVVVVVVVVVVVVVV##############
sys.stdout = TestHelper.ColorPrintCounter()
###^^^^^^^^^^^^計算print出的錯誤率^^^^^^^^^^^^^^^^^^#############
config = configparser.ConfigParser()
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
config_keyfile = os.path.join(current_dir, 'game.ini')
# 讀取配置文件
config.read(config_keyfile, encoding='utf-8')
################確認遊戲模板(請輸入 'U1、U2.../V1、V2...')###########################
ui_version = 'U2'
product_numbers = ['VV']
################確認帳號#######################################
phone1='9999999123' #for 登入
def main():
    driver = webdriver.Chrome()

    for product in product_numbers:
        url = config.get(ui_version, product)
        sys.stdout.reset_counts()

        # 打开网页
        driver.get(url)
        WebDriverWait(driver, 10)
        driver.maximize_window()        
#-------------------------1.登入模塊
        print("\033[107m\033[30m" + "1.登入模塊" + "\033[0m")
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
                EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "rounded-lg shadow")]'))
            ).click()
            # 尋找彈窗元素判斷是否登入
        try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Bônus de primeira recarga para usuários convidados")]'))
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
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Bônus de primeira recarga para usuários convidados")]'))
                )
                print("2.1 邀請popup顯示\033[32mOK\033[0m")
        except TimeoutException:
                print("\033[91m" +"2.1 邀請popup未顯示"+ "\033[0m")
        sleep(0.5)
        element=WebDriverWait(driver,5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'[alt="XCircle"]'))
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
                EC.presence_of_element_located((By.CSS_SELECTOR,'[alt="close"]'))
                ).click()        
    #<<<<<<<<<<<<<<<<<<<<<背景偵測popup，開始>>>>>>>>>>>>>>>>>>>>>>
        exit_event = threading.Event()
        popup_thread = threading.Thread(target=handle_popups, args=(driver,))
        popup_thread.start()
    #<<<<<<<<<<<<<<<<<<<<<背景偵測popup，開始>>>>>>>>>>>>>>>>>>>>>>
#-------------------------3.Side menu模塊
        print("\033[43m\033[30m" + "3.Side menu模塊" + "\033[0m")
#3.1/3.2 首充20%、充值10%
        try:
            TestHelper.Recharge(driver, "3.1 首充20%", "Primeira recarga", "Bônus de ")
            sleep(1)
            TestHelper.Recharge(driver, "3.2 充值10%", "Cashback", "A partir de")
            sleep(1)
#3.3/3.4/3.5/3.6 邀请、VIP、报道、关于我们            
            TestHelper.Normal(driver, "3.3 邀请", "Recomendar", "Copie o link para seus amigos!")
            sleep(1)
            TestHelper.Normal(driver, "3.4 VIP", "Regras VIP", "Limite máximo de retirada única")
            sleep(1)
            TestHelper.Normal(driver, "3.5 报道", "Check-In", "Regras de recompensa ")
            sleep(1)
            TestHelper.Normal(driver, "3.6 关于我们", "Sobre Nós", "Turismo e Jogos para uma Nova Geração")
            sleep(1)
            TestHelper.Normal(driver, "3.7 活動", "Eventos", "Reg de Coletas")
            sleep(1)
#3.8 电报               
            TestHelper.Normal(driver, "3.8 电报", "Adicionar Telegrama", "Junte-se ao telegram")    
            TestHelper.Net(driver, "3.8.2 Junte-se按鈕", "text-white shadow","", "tgme_logo")
            element=WebDriverWait(driver,5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'[alt="Close Icon"]'))
            ).click() 
#3.9 执照页
            TestHelper.Normal(driver, "3.9 执照页", "Gaming Curaçao", "Licença De Curaçao")   
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@class= "anticon anticon-left relative z-10"]'))
            )
            driver.execute_script("arguments[0].click();", element)
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("3.9.2 执照页返回键\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.9.2 执照页返回键失败"+ "\033[0m")      
#3.10 各游戏filter   
            sleep(0.5)        
            TestHelper.GameFilter(driver, "3.10 游戏filter_Slots","3.9 游戏filter_Slots", "Slots", "-Slots")
            TestHelper.GameFilter(driver, "3.11 游戏filter_Cards","3.10 游戏filter_Cards", "Cards", "-Cards")
            TestHelper.GameFilter(driver, "3.12 游戏filter_Fishing","3.11 游戏filter_Fishing", "Fishing", "-Fishing")
            TestHelper.GameFilter(driver, "3.13 游戏filter_Arcades","3.12 游戏filter_Arcades", "Arcades", "-Arcade")
            TestHelper.GameFilter(driver, "3.14 游戏filter_Bingo","3.13 游戏filter_Bingo", "Bingo", "-Bingo")
            TestHelper.GameFilter(driver, "3.15 游戏filter_Tables", "3.14 游戏filter_Tables", "Tables", "-Tables")
            TestHelper.GameFilter(driver, "3.16 游戏filter_Viver", "3.15 游戏filter_Viver", "Viver", "-Viver")
            TestHelper.GameFilter(driver, "3.17 游戏filter_Others", "3.16 游戏filter_Others", "Others", "-Others")
            TestHelper.GameFilter(driver, "3.18 游戏filter_Favoritos", "3.17 游戏filter_Favoritos", "Favoritos", "Favoritos")
            TestHelper.Normal(driver, "3.19.1 下载", "DownloadSimple", "Ao digitalizar o código QR")
            sleep(0.5)
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//img[@alt='Close Icon']"))
                ).click()
            try:
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Todos')]"))
                )
                print("3.19.2 下载 x icon\033[32mOK\033[0m")
            except TimeoutException:
                print("\033[91m" +"3.19.2 下载x icon失败"+ "\033[0m") 
            print("\033[48;5;22m\033[97m" + "3.Side menu模塊 OK" + "\033[0m") 
#4.HEADER模塊 --------------------------------------          
            print("\033[43m\033[30m" + "4. HEADER模塊" + "\033[0m")
            TestHelper.Normal(driver, "4.1 重刷按钮", "refresh", "icon-loading")
            TestHelper.Normal(driver, "4.2 引導至儲值頁", "add", "Balanço Total")
            TestHelper.Normal(driver, "4.3 個人資訊頁", "Header__DirectionIcon", "Modificar informações")
            TestHelper.Normal(driver, "4.5 通知中心", "notification", "Centro de Notificação")
            TestHelper.Normal(driver, "4.6 遊戲logo", "logo-menu", "Slots")
            print("\033[48;5;22m\033[97m" + "4. HEADER模塊 OK" + "\033[0m")
#5.页面游戏filter模块 --------------------------------------          
            print("\033[43m\033[30m" + "5.页面游戏filter模块" + "\033[0m")
            elements = driver.find_elements(By.XPATH, "//img[@alt='close']")
            if elements:
                elements[1].click()
                elements[0].click()
            sleep(0.5)    
            TestHelper.GameFilter(driver,"5.1 页面游戏filter_Slots", "5.1 页面游戏filter_Slots", "Slots", "-Slots")
            TestHelper.GameFilter(driver, "5.2 页面游戏filter_Cards","5.2 页面游戏filter_Cards", "Cards", "-Cards")
            TestHelper.GameFilter(driver, "5.3 页面游戏filter_Fishing","5.3 页面游戏filter_Fishing", "Fishing", "-Fishing")
            TestHelper.GameFilter(driver, "5.4 页面游戏filter_Arcade","5.4 页面游戏filter_Arcade", "Arcade", "-Arcade")
            TestHelper.GameFilter(driver, "5.5 页面游戏filter_Bingo","5.5 页面游戏filter_Bingo", "Bingo", "-Bingo")
            TestHelper.GameFilter(driver, "5.6 页面游戏filter_Table","5.6 页面游戏filter_Table", "Table", "-Table")
            TestHelper.GameFilter(driver, "5.7 页面游戏filter_Viver","5.7 页面游戏filter_Viver", "Viver", "-Viver")
            TestHelper.GameFilter(driver, "5.8 页面游戏filter_Others","5.8 页面游戏filter_Others", "Others", "-Others")
            TestHelper.GameFilter(driver, "5.9 页面游戏filter_Favoritos","5.9 页面游戏filter_Favoritos", "Favoritos", "Favoritos")
            TestHelper.Normal(driver, "5.10 搜寻游戏", "InputSection", "Insira pelo menos")
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//img[@alt='Close Icon']"))
                ).click()
            print("\033[48;5;22m\033[97m" + "5.页面游戏filter模块 OK" + "\033[0m")
#6.浮动扭模块 --------------------------------------          
            print("\033[43m\033[30m" + "6.浮动扭模块" + "\033[0m")
            TestHelper.ManyElements(driver, "6.1 下載","FixedToolContainer", 0, "Baixar Android")
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//img[@alt='Close Icon']"))
                ).click()
            TestHelper.ManyElements(driver, "6.2 客服","FixedToolContainer", 1, "Clique no botão para pular")
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//img[@alt='close']"))
                ).click()
            print("\033[48;5;22m\033[97m" + "6.浮动扭模块 OK" + "\033[0m")
#7.footer區塊 --------------------------------------          
            print("\033[43m\033[30m" + "7.footer區塊" + "\033[0m")
            TestHelper.Footer(driver, "7.1.1 filter_Slots", "Slots", "-Slots")
            TestHelper.Footer(driver, "7.2.1 filter_Cards", "Cards", "-Cards")
            TestHelper.Footer(driver, "7.3.1 filter_Fishing", "Fishing", "-Fishing")
            TestHelper.Footer(driver, "7.4.1 filter_Arcades", "Arcades", "-Arcade")
            TestHelper.Footer(driver, "7.5.1 filter_Bingo", "Bingo", "-Bingo")
            TestHelper.Footer(driver, "7.6.1 filter_Tables", "Tables", "-Tables")
            TestHelper.Footer(driver, "7.7.1 filter_Viver", "Viver", "-Viver")
            TestHelper.Footer(driver, "7.8.1 filter_Others", "Others", "-Others")
            TestHelper.Footer(driver, "7.9.1 filter_Salão", "Salão", "Slots")
            TestHelper.Footer(driver, "7.10.1 Politica de Privacidade", "Politica de Privacidade", "Privacy Policy")
            TestHelper.Normal(driver, "7.10.2 Politica返回鍵", "currentColor", "Ver tudos")
            TestHelper.Footer(driver, "7.11.1 Termos de Servico", "Termos de Servico", "ALL USERS OF")
            TestHelper.Normal(driver, "7.11.3 Termos返回鍵", "currentColor", "Ver tudos")
            TestHelper.Footer(driver, "7.12.1 Descrico do nivel VIP", "Descrico do nivel VIP", "Valor total da recarga")
            TestHelper.Normal(driver, "7.13 文案收合鍵", "Mostrar", "Colocar fora")            
            TestHelper.Net(driver, "7.14 外網連結_Skrill", "footer1",2, "Skrill Logo")
            TestHelper.Net(driver, "7.15 外網連結_BeGambleAware", "footer1", 3,"Logo for \'BeGambleAware\'")
            TestHelper.Net(driver, "7.16 外網連結_Interac", "footer1",4, "Interac")
            TestHelper.Net(driver, "7.17 外網連結_GamCare", "footer1",5, "GamCare logo")
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
