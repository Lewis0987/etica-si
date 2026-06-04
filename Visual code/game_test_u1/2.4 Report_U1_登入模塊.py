from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import time
from time import sleep

class LoginTest(unittest.TestCase):
    """登录模块"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

    # 用例每次执行时运行
    def setUp(self):
        self.driver.get("https://ttgroup-dev.vip/")
        self.driver.maximize_window()
    # 用例每次结束时执行
    def tearDown(self):
        # 清空cookie
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    #判斷登入狀態的text
    def get_login_message(self):
        msg = self.driver.find_element(By.XPATH, "//div[@class='ext-white text-3xl mt-5 font-extrabold']").text
        return msg

    def get_error_message_username(self):
        msg = self.driver.find_element(By.XPATH, "//*[@class='ant-notification-notice-message']").text
        return msg

    def get_error_message_password(self):
        msg = self.driver.find_element(By.XPATH, "//*[@class='text-left text-[var(--input-invalidation-text-color)] text-sm leading-5 pt-1']").text
        return msg

    # 登录函数
    def login(self, username, password):
        # 點擊登入頁
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.XPATH,'//span[contains(text(), "Entrar")]'))
        ).click()
        # 输入用户名
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="number"]'))
        ).send_keys(username)
        # 输入密码
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))
        ).send_keys(password)
        # 点击确认按钮
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "ConfirmButton")]'))
        ).click()
        sleep(0.5)

    

    def test_01(self):
        """登录-用户名正确，密碼錯誤"""
        self.login("9999999000", "1")
        # 通过断言方法判断是否登录成功
        self.assertTrue(self.get_error_message_password() == 'Senha (4-12 letras e números)')
    def test_02(self):
        """登录-用户名错误 密码正确"""
        self.login("99999990","1111")
        # 通过断言方法判断是否登录成功
        self.assertTrue(self.get_error_message_username() == ' formato do número do celular está errado, altere-o.')
        
    def test_03(self):
        """登录-用户名和密码都输入正确"""
        self.login("9999999125", "1111")
        # 通过断言方法判断是否登录成功
        self.assertTrue(self.get_login_message() == 'Equilíbrio insuficiente!')
        
if __name__ == '__main__':
        ##添加测试单元
    suite = unittest.TestSuite()
    #添加测试用例
    suite.addTest(LoginTest("test_01"))
    suite.addTest(LoginTest("test_02"))
    suite.addTest(LoginTest("test_03"))

    file_prefix = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    file_path = r"."+os.sep+file_prefix+"_result.html"

    ##得到文件句柄
    fp = open(file_path, "wb")
    runner = HTMLTestRunner(stream=fp, title="User Test Report", description="TestCase")
   # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="User Test Report", description="TestCase")
    runner.run(suite)
    fp.close()

