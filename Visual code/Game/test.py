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
from colorama import Fore,Style
import time
import sys
import threading
import os
import configparser
import pyperclip
import re


print(f"\033[32m✅ 下載完成：\033[0m")
print(f"\033[31m🗑️ 已刪除：\033[0m")

'''
print('\033[33mA-1.首頁[Subscribe] 訂閱 \033[0m')
print("\033[94m" + "A-1.未偵測到已領取文字，繼續流程..." + "\033[0m")
print("telegram >>>> \033[91m" + "元素不存在" + "\033[0m")
'''

'''
download_dir = os.path.abspath("downloads")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
})
'''

