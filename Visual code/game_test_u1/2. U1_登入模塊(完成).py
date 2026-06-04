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
###VVVVVVVVVVV計算print出的錯誤率VVVVVVVVVVVVVVVVV###############
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
product_numbers = ['V37']
################確認帳號#######################################
phone1='9999999000' #for 登入
phone2='99999990000' #for 註冊
# 初始化Chrome浏览器
driver = webdriver.Chrome()

for product in product_numbers:
    url = config.get(ui_version, product)
    sys.stdout.reset_counts()
    driver.get(url)
    WebDriverWait(driver, 10)
    driver.maximize_window()

    print("\033[43m\033[30m" + "1. 切換表層" + "\033[0m")
    #-------------------------1.1 切換表層_註冊
    sleep(2)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Cadastre-Se")]'))
    ).click()

    try:
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Register agora")]'))
        )
        print("1.1 切換表層_註冊\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"1.1 切換表層_註冊失敗"+ "\033[0m")
    #-------------------------1.2 切換表層_登入
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Entrar")]'))
    ).click()

    try:
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Esqueça A Eenha?")]'))
        )
        print("1.2 切換表層_登入\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"1.2 切換表層_登入失敗"+ "\033[0m")
    #-------------------------1.3 切換表層_忘記密碼
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Esqueça A Eenha?")]'))
    ).click()

    try:
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Redefinir senha")]'))
        )
        print("1.3 切換表層_忘記密碼\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"1.3 切換表層_忘記密碼失敗"+ "\033[0m")
    #-------------------------1.4 切換表層_忘記密碼title
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Esqueça A Senha?")]'))
    ).click()

    try:
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Register agora")]'))
        )
        print("1.4 切換表層_忘記密碼title切換到註冊\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"1.4 切換表層_忘記密碼title切換到註冊失敗"+ "\033[0m")
    #-------------------------1.5 切換表層_X icon
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//img[@alt="Close Icon"]'))
    ).click()

    try:
        div_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Entrar")]'))
        )
        print("\033[91m" +"1.5 切換表層_X icon失敗"+ "\033[0m")
    except TimeoutException:
        print("1.5 切換表層_X icon\033[32mOK\033[0m")
    #-------------------------1.6 切換表層_Cadastre-Se
        element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "LoginButton")]'))
        ).click()

    try:
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Entrar")]'))
        )
        print("1.6 切換表層_Cadastre-Se\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"1.6 切換表層_Cadastre-Se失敗"+ "\033[0m")


    print("\033[48;5;22m\033[97m" + "1. 切換表層OK" + "\033[0m")

    print("\033[43m\033[30m" + "2.登入" + "\033[0m")
    #-------------------------2.1 登入_帳號空白
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('1111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,'//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        print("2.1 登入_帳號空白(無法登入)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"2.1 登入_帳號空白(登入成功)"+ "\033[0m")
    #-------------------------2.2 登入_帳號9碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys('999999900')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        div_element_2 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "O formato do")]'))
        )
        print("2.2 登入_帳號9碼(無法登入)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"2.2 登入_帳號9碼(登入成功)"+ "\033[0m")
    #-------------------------2.3 登入_帳號12碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys('000')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        div_element_2 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "O formato do")]'))
        )
        print("2.3 登入_帳號12碼(無法登入)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"2.3 登入_帳號12碼(登入成功)"+ "\033[0m")
    #-------------------------2.4 登入_帳號錯誤
    action_chains = ActionChains(driver)
    element = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 12).perform()
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys('9991999002')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Conta ou senha incorreta")]'))
            )
            print("2.4 登入_帳號錯誤(無法登入)\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"2.4 登入_帳號錯誤(登入成功)"+ "\033[0m")
    #-------------------------2.5 登入_帳號10碼/密碼正確(4碼)
    element = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 12).perform()
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys(phone1)
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Convide usuários limitados para compartilhar")]'))
            )
            print("2.5 登入_帳號10碼(登入成功)\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"2.5 登入_帳號10碼(登入失敗)"+ "\033[0m")
    #-------------------------2.6 登入_帳號11碼/密碼正確(4碼)
    element=WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH,'//a[@class="ant-notification-notice-close"]'))
        ).click()
    sleep(0.5)
    element=WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH,'//a[@class="ant-notification-notice-close"]'))
        ).click()
    sleep(1)
    element=WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'[alt="Close Icon"]'))
        ).click()
    sleep(0.5)
    element=WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'[alt="Close Icon"]'))
            ).click()
    sleep(0.5)
    element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//section[contains(@class,"flex gap-2 items-center")]'))
                )
    action_chains.double_click(element).perform()        
    element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//img[@src="assets/u1/ic_sign_out.png"]'))
                ).click()
    element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Confirme")]'))
            ).click()
    sleep(0.5)
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys(phone2)
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('1111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Convide usuários limitados para compartilhar")]'))
            )
            print("2.6 登入_帳號11碼(登入成功)\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"2.6 登入_帳號11碼(登入失敗)"+ "\033[0m")
    #-------------------------2.7 登入_密碼空白
    element=WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'[alt="Close Icon"]'))
        ).click()
    sleep(0.5)
    element=WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'[alt="Close Icon"]'))
            ).click()
    element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//section[contains(@class,"flex gap-2 items-center")]'))
                )
    ActionChains(driver).double_click(element).perform()            
    element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//img[@src="assets/u1/ic_sign_out.png"]'))
                ).click()
    element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Confirme")]'))
            ).click()
    sleep(0.5)
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys(phone1)
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Senha (4-12 letras e números)")]'))
            )
            print("2.7 登入_密碼空白(無法登入)\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"2.7 登入_密碼空白(登入成功)"+ "\033[0m")
    #-------------------------2.8 登入_密碼3碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Senha (4-12 letras e números)")]'))
            )
            print("2.8 登入_密碼3碼(無法登入)\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"2.8 登入_密碼3碼(登入成功)"+ "\033[0m")
    #-------------------------2.9 登入_密碼13碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('1111111111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Senha (4-12 letras e números)")]'))
            )
            print("2.9 登入_密碼13碼(無法登入)\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"2.9 登入_密碼13碼(登入成功)"+ "\033[0m")
    #-------------------------2.10 登入_密碼顯碼功能
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[alt="eye-close"]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[type="text"]'))
            )
            print("2.10 登入_密碼顯碼功能\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"2.10 登入_密碼顯碼功能失效"+ "\033[0m")
    #-------------------------2.11 登入_密碼隱碼功能
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[alt="eye-open"]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
            )
            print("2.11 登入_密碼隱碼功能\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"2.11 登入_密碼隱碼功能失效"+ "\033[0m")
    print("\033[48;5;22m\033[97m" + "2.登入OK" + "\033[0m")

    print("\033[43m\033[30m" + "3.註冊" + "\033[0m")
    #-------------------------3.1註冊_帳號空白
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Cadastre-Se")]'))
    ).click()
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@placeholder= "Confirme o número do celular"]'))
    ).send_keys(phone1)
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('1111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Os números de telefone estão inconsistentes.")]'))
        )
        print("3.1註冊_帳號空白(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"3.1註冊_帳號空白(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.2註冊_帳號9碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys('999999900')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Os números de telefone estão inconsistentes.")]'))
        )
        print("3.2註冊_帳號9碼(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"3.2註冊_帳號9碼(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.3註冊_帳號12碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys('000')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Os números de telefone estão inconsistentes.")]'))
        )
        print("3.3註冊_帳號12碼(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"3.3註冊_帳號12碼(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.4註冊_帳號10碼
    element = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 12).perform()
    action_chains.click(element).send_keys(Keys.BACKSPACE * 1).perform()
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys(phone1)
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        print("\033[91m" +"3.4註冊_帳號10碼(展現錯誤訊息)"+ "\033[0m")
    except TimeoutException:
        print("3.4註冊_帳號10碼(無錯誤訊息)\033[32mOK\033[0m")
    #-------------------------3.5註冊_帳號11碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys('0')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        print("\033[91m" +"3.5註冊_帳號11碼(展現錯誤訊息)"+ "\033[0m")
    except TimeoutException:
        print("3.5註冊_帳號11碼(無錯誤訊息)\033[32mOK\033[0m")
    #-------------------------3.6註冊_確認帳號空白
    element = driver.find_element(By.XPATH,'//*[@placeholder= "Confirme o número do celular"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 12).perform()
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Os números de telefone estão inconsistentes.")]'))
        )
        print("3.6註冊_確認帳號空白(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"3.6註冊_確認帳號空白(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.7註冊_確認帳號錯誤
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@placeholder= "Confirme o número do celular"]'))
    ).send_keys(phone1)
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Os números de telefone estão inconsistentes.")]'))
        )
        print("3.7註冊_確認帳號錯誤(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"3.7註冊_確認帳號錯誤(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.8註冊_確認帳號正確
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@placeholder= "Confirme o número do celular"]'))
    ).send_keys('0')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Os números de telefone estão inconsistentes.")]'))
        )
        print("\033[91m" +"3.8註冊_確認帳號正確(顯示錯誤訊息)"+ "\033[0m")
    except TimeoutException:
        print("3.8註冊_確認帳號正確(無展示錯誤訊息)\033[32mOK\033[0m") 
    #-------------------------3.9註冊_密碼空白
    element = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 4).perform()
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Senha (4-12 letras e números)")]'))
        )
        print("3.9註冊_密碼空白(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"3.9註冊_密碼空白(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.10註冊_密碼3碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Senha (4-12 letras e números)")]'))
        )
        print("3.10註冊_密碼3碼(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"3.10註冊_密碼3碼(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.11註冊_密碼13碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('1111111111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Senha (4-12 letras e números)")]'))
        )
        print("3.11註冊_密碼13碼(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"3.11註冊_密碼13碼(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.12註冊_密碼4碼
    element = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 9).perform()
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Senha (4-12 letras e números)")]'))
        )
        print("\033[91m" +"3.12註冊_密碼4碼(顯示錯誤訊息)"+ "\033[0m")
    except TimeoutException:
        print("3.12註冊_密碼4碼(無展示錯誤訊息)\033[32mOK\033[0m")
    #-------------------------3.13註冊_驗證碼空白
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "por favor insira o código de verificação")]'))
        )
        print("3.13註冊_驗證碼空白(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"3.13註冊_驗證碼空白(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.14註冊_驗證碼錯誤
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@placeholder= "Código de verificação"]'))
    ).send_keys("123")
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Código de verificação incorreto")]'))
        )
        print("3.14註冊_驗證碼錯誤(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"3.14註冊_驗證碼錯誤(錯誤訊息異常)"+ "\033[0m")
    #-------------------------3.15註冊_密碼顯碼扭
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[alt="eye-close"]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[type="text"]'))
            )
            print("3.15註冊_密碼顯碼扭功能\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"3.15註冊_密碼顯碼扭功能失效"+ "\033[0m")
    #-------------------------3.16註冊_密碼隱碼扭
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[alt="eye-open"]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
            )
            print("3.16註冊_密碼隱碼扭功能\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"3.16註冊_密碼隱碼扭功能失效"+ "\033[0m")
    #-------------------------3.17註冊_隱私勾選欄位
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[alt="Checked"]'))).click()
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "por favor insira o código de verificação")]'))
        )
        print("\033[91m" +"3.17註冊_隱私勾選欄位未選(確認扭可點擊)"+ "\033[0m")
    except TimeoutException:
            print("3.17註冊_隱私勾選欄位未選(確認扭無法點擊)\033[32mOK\033[0m")
    #-------------------------3.18註冊_隱私連結   
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Condições e condições, política de privacidade")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Privacy Policy and Personal Data Protection")]'))
        )
        element = WebDriverWait(driver, 5).until_not(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Condições e condições, política de privacidade")]'))
        )
        print("3.18註冊_隱私連結\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"3.18註冊_隱私連結失效"+ "\033[0m") 
    print("\033[48;5;22m\033[97m" + "3.註冊OK" + "\033[0m")

    print("\033[43m\033[30m" + "4.忘記密碼" + "\033[0m") 
    #-------------------------4.1忘記密碼_帳號空白 
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Entrar")]'))
    ).click()
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[contains(text(), "Esqueça A Eenha?")]'))
    ).click()
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@placeholder= "Código de verificação"]'))
    ).send_keys("123")
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('1111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        print("4.1忘記密碼_帳號空白(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.1忘記密碼_帳號空白(無錯誤訊息)"+ "\033[0m")
    #-------------------------4.2忘記密碼_帳號9碼 
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys('999999900')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "O formato do número do celular está errado, altere-o.")]'))
        )
        print("4.2忘記密碼_帳號9碼(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.2忘記密碼_帳號9碼(無錯誤訊息)"+ "\033[0m")   
    #-------------------------4.3忘記密碼_帳號12碼 
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys('000')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "O formato do número do celular está errado, altere-o.")]'))
        )
        print("4.3忘記密碼_帳號12碼 (展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.3忘記密碼_帳號12碼 (無錯誤訊息)"+ "\033[0m")   
    #-------------------------4.4忘記密碼_帳號10碼 
    element = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 12).perform() 
    action_chains.click(element).send_keys(Keys.BACKSPACE * 12).perform() 
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys(phone1)
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Código de verificação incorreto")]'))
        )
        print("4.4忘記密碼_帳號10碼(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.4忘記密碼_帳號10碼(無錯誤訊息)"+ "\033[0m")
    #-------------------------4.5忘記密碼_帳號11碼   
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys('0')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Código de verificação incorreto")]'))
        )
        print("4.5忘記密碼_帳號11碼(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.5忘記密碼_帳號11碼(無錯誤訊息)"+ "\033[0m")
    #-------------------------4.6忘記密碼_驗證碼錯誤
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Código de verificação incorreto")]'))
        )
        print("4.6忘記密碼_驗證碼錯誤(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.6忘記密碼_驗證碼錯誤(無錯誤訊息)"+ "\033[0m")    
    #-------------------------4.7忘記密碼_驗證碼空白 
    element = driver.find_element(By.XPATH,'//*[@placeholder= "Código de verificação"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 5).perform() 
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "por favor insira o código de verificação")]'))
        )
        print("4.7忘記密碼_驗證碼空白(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.7忘記密碼_驗證碼空白(無錯誤訊息)"+ "\033[0m")  
    #-------------------------4.8忘記密碼_驗證碼按鈕(無輸入帳號)
    element = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 12).perform() 
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "SendSMSCodeButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Número de celular de 10 ou 11 dígitos")]'))
        )
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Enviar")]'))
        )
        print("4.8忘記密碼_驗證碼按鈕(無輸入帳號)不可點擊\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.8忘記密碼_驗證碼按鈕(無輸入帳號)可點擊"+ "\033[0m") 
    #-------------------------4.9忘記密碼_驗證碼按鈕(有輸入帳號) 
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys(phone1)
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "SendSMSCodeButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until_not(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Enviar")]'))
        )
        print("4.9忘記密碼_驗證碼按鈕(有輸入帳號)可點擊\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.9忘記密碼_驗證碼按鈕(有輸入帳號)不可點擊"+ "\033[0m")    
    #-------------------------4.10忘記密碼_驗證碼時間內重複送 
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[contains(text(), "Esqueça A Senha?")]'))
    ).click() 
    div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Entrar")]'))
        ).click()
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[contains(text(), "Esqueça A Eenha?")]'))
    ).click() 
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys(phone1)
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "SendSMSCodeButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Enviar")]'))
        )
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Seu código de verificação foi enviado, por favor verifique.")]'))
        )
        print("4.10忘記密碼_驗證碼時間內不可重複送\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.10忘記密碼_驗證碼時間內可重複送"+ "\033[0m")
    #-------------------------4.11忘記密碼_密碼空白 
    element = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    action_chains.click(element).send_keys(Keys.BACKSPACE * 5).perform() 
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@placeholder= "Código de verificação"]'))
    ).send_keys("123")
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Senha (4-12 letras e números)")]'))
        )
        print("4.11忘記密碼_密碼空白 (展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.11忘記密碼_密碼空白(無錯誤訊息)"+ "\033[0m")
    #-------------------------4.12忘記密碼_密碼3碼 
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Senha (4-12 letras e números)")]'))
        )
        print("4.12忘記密碼_密碼3碼(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.12忘記密碼_密碼3碼(無錯誤訊息)"+ "\033[0m")
    #-------------------------4.13忘記密碼_密碼13碼
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys('1111111111')
    button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
    try:
        div_element_1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Senha (4-12 letras e números)")]'))
        )
        print("4.13忘記密碼_密碼13碼(展現錯誤訊息)\033[32mOK\033[0m")
    except TimeoutException:
        print("\033[91m" +"4.13忘記密碼_密碼13碼(無錯誤訊息)"+ "\033[0m")
    #-------------------------4.14忘記密碼_密碼顯碼扭 
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[alt="eye-close"]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[type="text"]'))
            )
            print("4.14忘記密碼_密碼顯碼扭功能\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"4.14忘記密碼_密碼顯碼扭功能失效"+ "\033[0m")
    #-------------------------4.15忘記密碼_密碼隱碼扭
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[alt="eye-open"]'))
        ).click()
    try:
            div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
            )
            print("4.15忘記密碼_密碼隱碼扭功能\033[32mOK\033[0m")
    except TimeoutException:
            print("\033[91m" +"4.15忘記密碼_密碼隱碼扭功能失效"+ "\033[0m")
    print("\033[48;5;22m\033[97m" + "4.忘記密碼OK" + "\033[0m")
    total_percentage = sys.stdout.total_count / sys.stdout.total_count * 100
    green_percentage = sys.stdout.green_count / sys.stdout.total_count * 100
    red_percentage = sys.stdout.red_count / sys.stdout.total_count * 100
    print("測試項目"+ "\033[93m"f"{ui_version}{product}"+"\033[0m")
    print(f"總測試筆數: {sys.stdout.total_count} ({total_percentage:.2f}%)")
    print(f"\033[32m測試成功筆數: {sys.stdout.green_count} ({green_percentage:.2f}%)\033[0m")
    print(f"\033[91m測試失敗筆數: {sys.stdout.red_count} ({red_percentage:.2f}%)\033[0m")
driver.quit()