from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(driver_path=ChromeDriverManager().install(), options=options)  # ✅ 修正 `driver_path`

