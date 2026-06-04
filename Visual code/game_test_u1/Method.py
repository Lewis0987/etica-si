from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from time import sleep
import threading
import sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestHelper:
    #一般判斷法----------------------------------------------------
    @staticmethod
    def Normal(driver, category_name, button_text, filter_text): 
        print(f"\033[107m\033[30m{category_name}\033[0m")
        sleep(1)
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//*[contains(text(), "{button_text}")] | //img[@alt="{button_text}"] | //*[contains(@class,"{button_text}")] | //*[@fill="{button_text}"]')
        )).click()                
        try:
            div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{filter_text}")] | //*[contains(@class, "{filter_text}")] | //*[contains(text(), "{filter_text}")]'))) 
            print(f"{category_name}\033[32mOK\033[0m")
        except TimeoutException:
            print(f"\033[91m{category_name}失败\033[0m")
    #首充、次充----------------------------------------------------------
    @staticmethod
    def Recharge(driver, category_name, button_text, filter_text): 
        
        print(f"\033[107m\033[30m{category_name}\033[0m")
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{button_text}")]'))
            ).click()                
        try:
            div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{filter_text}")]'))
            )
            print(f"{category_name}\033[32mOK\033[0m")
        except TimeoutException:
            print(f"\033[91m{category_name}失败\033[0m")
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Recarrague agora")]'))
            ).click()
        try:
            div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Balanço Total")]'))
            )
            print(f"{category_name}跳转充值页\033[32mOK\033[0m")
        except TimeoutException:
            print(f"\033[91m{category_name}跳转充值页\033[0m")

    #外網測試方法----------------------------------------------
    @staticmethod
    def Net(driver,title1,element1,button_text,webwords):
        print(f"\033[107m\033[30m{title1}\033[0m")
        initial_window_handle = driver.current_window_handle
        try:
            element_list = WebDriverWait(driver, 1).until(
                EC.presence_of_all_elements_located((By.XPATH, f"//img[@alt='{element1}']"))
            )
            if element_list and len(element_list) > int(button_text):
                element_list[int(button_text)].click()
        except TimeoutException:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(@class,'{element1}')]"))
            ).click()
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
                EC.presence_of_element_located((By.XPATH, f'//img[@alt= "{webwords}"] | //a[@title= "{webwords}"] | //*[@class="{webwords}"]'))
            )
            print(f"{title1}\033[32mOK\033[0m")
        except TimeoutException:
            print(f"\033[91m{title1}失效\033[0m")
            # 打印错误消息后，继续执行，直接跳过
        pass
        # 关闭新窗口
        driver.close()
        # 切换回原始窗口
        driver.switch_to.window(initial_window_handle)
    #遊戲filter測試方法---------------------------------------------------------
    @staticmethod
    def GameFilter(driver, category_name, category_name2, button_text, filter_text):
        if category_name:
            print(f"\033[107m\033[30m{category_name}\033[0m")
        try:
            # 點擊具體的遊戲按鈕
            element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{button_text}")] | //img[@src="{button_text}"]'))
            ).click()            
            try:
                # 檢查遊戲類別 filter 是否正確
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{filter_text}")]'))
                )
                print(f"{category_name2} \033[32mOK\033[0m")
            except TimeoutException:
                print(f"\033[91m{category_name2} 失效\033[0m")
        except TimeoutException:
            print(f"\033[44m\033[97m{category_name2} 無接上\033[0m")
    #多個元素----------------------------------------------------------------
    @staticmethod
    def ManyElements(driver, category_name, category_name2, button_text, filter_text):
        try:
            driver.find_elements(By.XPATH, f'//img[@src="{category_name2}"] | //*[contains(@class,"{category_name2}")]')[int(button_text)].click()
            try:
                # 檢查遊戲類別 filter 是否正確
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[contains(text(), "{filter_text}")]'))
                )
                print(f"{category_name} \033[32mOK\033[0m")
            except TimeoutException:
                print(f"\033[91m{category_name}失效\033[0m")
        except TimeoutException:
            print(f"\033[44m\033[97m{category_name}無接上\033[0m")
    #測試footer置頂方法-------------------------------------------------
    @staticmethod
    def Footer(driver, category_name, button_text, filter_text,Top,Topy): 
        print(f"\033[107m\033[30m{category_name}\033[0m")
        try:
            # 點擊具體的遊戲按鈕
            element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//button[contains(text(), "{button_text}")]')
            )).click() 
                       
            try:
                div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{filter_text}")] | //div[text()= "Retornar"] | //div[text()= "Valor total da recarga"]'))) 
                print(f"{category_name}\033[32mOK\033[0m")
            except TimeoutException:
                print(f"\033[91m{category_name}失败\033[0m")
            sleep(1)
            target_element = driver.find_element(By.XPATH, f'//div[contains(text(), "{Top}")] ')
                # 获取目标元素的Y坐标
            element_y = target_element.location['y']
            if element_y == Topy:
                print(f"{category_name}置頂功能\033[32mOK\033[0m")
            else:
                print(f"\033[91m{category_name}置頂功能失败\033[0m")
        except TimeoutException:
            print(f"\033[44m\033[97m{category_name}無接上\033[0m")
    #計算錯誤率-------------------------------------------------------------------
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
#查找彈窗方法---------------------------------------------------------------------------
exit_event = threading.Event()
def handle_popups(driver):
    while not exit_event.is_set():
        try:
            # 在这里执行查找弹窗的操作
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Equilíbrio insuficiente!") or contains(text(), "Bônus de primeira recarga para usuários convidados")]')))
            # 找到弹窗后执行关闭的操作
            close_button = driver.find_element(By.CSS_SELECTOR, '[alt="XCircle"], [alt="close"]')
            close_button.click()
        except TimeoutException:
            # 超时异常，表示未找到弹窗，不输出错误信息
            pass
        except NoSuchWindowException:
            # 窗口已經被關閉，結束循環
            break
    
    
class TestHelper1:
    #一般判斷法----------------------------------------------------
    @staticmethod
    def Normal(driver, category_name,Menu, button_text, filter_text): 
        print(f"\033[107m\033[30m{category_name}\033[0m")
        try:
            WebDriverWait(driver,1).until(
                EC.presence_of_element_located((By.XPATH,f'//*[text()="{Menu}"]'))
            ).click() 
        except TimeoutException:
            pass
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'//*[contains(text(), "{button_text}")] | //img[@alt="{button_text}"] | //*[contains(@class,"{button_text}")] | //*[@fill="{button_text}"]')
        )).click()                
        try:
            div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{filter_text}")] | //*[contains(@class, "{filter_text}")] | //*[contains(text(), "{filter_text}")]'))) 
            print(f"{category_name}\033[32mOK\033[0m")
        except TimeoutException:
            print(f"\033[91m{category_name}失败\033[0m")
    #首充、次充----------------------------------------------------------
    @staticmethod
    def Recharge(driver, category_name, button_text, filter_text): 
        WebDriverWait(driver,5).until(
                EC.presence_of_element_located((By.XPATH,'//*[text()="Menu"]'))
            ).click() 
        sleep(0.5)
        print(f"\033[107m\033[30m{category_name}\033[0m")
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{button_text}")] | //*[@id="{button_text}"]'))
            ).click()                
        try:
            div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{filter_text}")]'))
            )
            print(f"{category_name}\033[32mOK\033[0m")
        except TimeoutException:
            print(f"\033[91m{category_name}失败\033[0m")
        element = driver.find_element(By.XPATH, "//*[contains(text(), 'Recarrague agora')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(1)    
        div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Recarrague agora")]'))
            ).click()
        try:
            div_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Balanço Total")]'))
            )
            print(f"{category_name}跳转充值页\033[32mOK\033[0m")
        except TimeoutException:
            print(f"\033[91m{category_name}跳转充值页\033[0m")


    #外網測試方法----------------------------------------------
    @staticmethod
    def Net(driver,title1,element1,button_text,webwords):
        print(f"\033[107m\033[30m{title1}\033[0m")
        initial_window_handle = driver.current_window_handle
        try:
            elements = WebDriverWait(driver, 1).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), '@ ')]"))
            )
            if elements:
                element = elements[0]
                driver.execute_script("arguments[0].scrollIntoView();", element)
                sleep(1)
        except TimeoutException:
            pass
        try:
            element_list = WebDriverWait(driver, 1).until(
                EC.presence_of_all_elements_located((By.XPATH, f"//img[@alt='{element1}']"))
            )
            if element_list and len(element_list) > int(button_text):
                element_list[int(button_text)].click()
        except TimeoutException:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(@class,'{element1}')]"))
            ).click()
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
                EC.presence_of_element_located((By.XPATH, f'//img[@alt= "{webwords}"] | //a[@title= "{webwords}"] | //*[@class="{webwords}"]'))
            )
            print(f"{title1}\033[32mOK\033[0m")
        except TimeoutException:
            print(f"\033[91m{title1}失效\033[0m")
            # 打印错误消息后，继续执行，直接跳过
        pass
        # 关闭新窗口
        driver.close()
        # 切换回原始窗口
        driver.switch_to.window(initial_window_handle)
    #遊戲filter測試方法---------------------------------------------------------
    @staticmethod
    def GameFilter1(driver, category_name, category_name2, button_text, filter_text):
        WebDriverWait(driver,5).until(
                EC.presence_of_element_located((By.XPATH,'//*[text()="Menu"]'))
            ).click() 
        if category_name:
            print(f"\033[107m\033[30m{category_name}\033[0m")
        try:
            # 點擊具體的遊戲按鈕
            element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{button_text}")] | //img[@src="{button_text}"]'))
            ).click()            
            try:
                # 檢查遊戲類別 filter 是否正確
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{filter_text}")]'))
                )
                print(f"{category_name2} \033[32mOK\033[0m")
            except TimeoutException:
                print(f"\033[91m{category_name2} 失效\033[0m")
        except TimeoutException:
            print(f"\033[44m\033[97m{category_name2} 無接上\033[0m")
        #遊戲filter測試方法---------------------------------------------------------
    @staticmethod
    def GameFilter(driver, category_name, category_name2, button_text, filter_text):
        if category_name:
            print(f"\033[107m\033[30m{category_name}\033[0m")
        try:
            # 點擊具體的遊戲按鈕
            element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{button_text}")] | //img[@src="{button_text}"]'))
            ).click()            
            try:
                # 檢查遊戲類別 filter 是否正確
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{filter_text}")]'))
                )
                print(f"{category_name2} \033[32mOK\033[0m")
            except TimeoutException:
                print(f"\033[91m{category_name2} 失效\033[0m")
        except TimeoutException:
            print(f"\033[44m\033[97m{category_name2} 無接上\033[0m")
    #多個元素----------------------------------------------------------------
    @staticmethod
    def ManyElements(driver, category_name, category_name2, button_text, filter_text):
        try:
            driver.find_elements(By.XPATH, f'//img[@src="{category_name2}"] | //*[contains(@class,"{category_name2}")]')[int(button_text)].click()
            try:
                # 檢查遊戲類別 filter 是否正確
                div_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[contains(text(), "{filter_text}")]'))
                )
                print(f"{category_name} \033[32mOK\033[0m")
            except TimeoutException:
                print(f"\033[91m{category_name}失效\033[0m")
        except TimeoutException:
            print(f"\033[44m\033[97m{category_name}無接上\033[0m")
    #測試footer置頂方法-------------------------------------------------
    @staticmethod
    def Footer(driver, category_name, button_text, filter_text,Top,Topy): 
        print(f"\033[107m\033[30m{category_name}\033[0m")
        elements = driver.find_elements(By.XPATH, "//div[contains(text(), 'Ver tudos')]")
        if elements:
    # 选择最后一个元素
            last_element = elements[-1]
            driver.execute_script("arguments[0].scrollIntoView();", last_element)
        sleep(1)
        try:
            element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//button[contains(text(), "{button_text}")]')
            )).click()                
            try:
                div_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{filter_text}")] | //div[text()= "Retornar"] | //div[text()= "Valor total da recarga"]'))) 
                print(f"{category_name}\033[32mOK\033[0m")
            except TimeoutException:
                print(f"\033[91m{category_name}失败\033[0m")
            sleep(1)
            target_element = driver.find_element(By.XPATH, f"//div[contains(text(), '{Top}')]")
                # 获取目标元素的Y坐标
            element_y = target_element.location['y']
            if element_y == Topy:
                print(f"{category_name}置頂功能\033[32mOK\033[0m")
            else:
                print(f"\033[91m{category_name}置頂功能失败\033[0m")
        except TimeoutException:
            print(f"\033[44m\033[97m{category_name}無接上\033[0m")
    #計算錯誤率-------------------------------------------------------------------
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