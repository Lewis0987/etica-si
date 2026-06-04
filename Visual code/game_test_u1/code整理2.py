#CSS、xpath比对
driver.find_element(By.CSS_SELECTOR, '.123')
driver.find_element(By.XPATH, "//*[@class='123']")
#-----------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR, 'a#123')
driver.find_element(By.XPATH, "//a[@id='123']")
#-----------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR,"input[autocomplete=off]")
driver.find_element(By.XPATH,"//input[@autocomplete='off']")
#-----------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR,'button:contains("Mostrar")')
driver.find_element(By.XPATH,'//button[text()="Mostrar"]')
#选择第三个元素-----------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR,"input[autocomplete=off]")[2]
driver.find_element(By.XPATH,"//input[@autocomplete='off']")[2]
#包含(class及各元素)-----------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR, 'div[class*="Primeira recarga"]')
driver.find_element(By.XPATH, '//div[contains(@class, "Primeira recarga")]')
#包含(text)-----------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR, 'div:contains("Balanço Total")')
driver.find_element(By.XPATH, '//div[contains(text(),"Balanço Total")]')
#开头包含-----------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR, 'input[value^="登"]' )
driver.find_element(By.XPATH, '//input[starts-with(@value, "登")]')
#结尾包含-----------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR, 'input[value$="录"] ' )
driver.find_element(By.XPATH, '//input[contains(@value, "录") and substring(@value, string-length(@value) - 0) = "录"]')
#--上下層---------------------------------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR,'div[class*="ImageTab"] span[alt="Cards"]')
driver.find_element(By.XPATH, '//div[contains(@class, "ImageTab")]//span[text()= "Cards"]')       
#--同層---------------------------------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR,'div[alt="+55"] + input[type="text"]')
driver.find_element(By.XPATH, '//div[@alt="+55"]/following-sibling::input[@type="text"]')
#--或者---------------------------------------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR, 'div:contains("Equilíbrio insuficiente!"), div:contains("Convide usuários limitados para compartilhar")')
driver.find_element(By.XPATH, '//div[contains(text(), "Equilíbrio insuficiente!") or contains(text(), "Convide usuários limitados para compartilhar")]')

#-----------------------------------------------------------------------------------------------------------
# 创建 ChromeOptions 对象
chrome_options = webdriver.ChromeOptions()
# 指定模拟的设备名称，例如 'iPhone X'
device_name = 'iPad Mini'
chrome_options.add_experimental_option('mobileEmulation', {'deviceName': device_name})
#-----------------------------------------------------------------------------------------------------------
ui_version = 'U1'
product_numbers = ['V2', 'V3', 'V4']

# 初始化Chrome浏览器
driver = webdriver.Chrome()

for product in product_numbers:
    url = config.get(ui_version, product)

    # 打开网页
    driver.get(url)
    WebDriverWait(driver, 10)
    driver.maximize_window()

driver.quit()
#模拟鼠标----------------------------------------------------------------------------
aa = driver.find_element(By.XPATH, '//div[@id="your_element_id"]')
bb = driver.find_element(By.XPATH, '//div[@id="your_element_id2"]')
# 使用 ActionChains 模拟鼠标点击
action = ActionChains(driver)
action.click(aa).perform()#单击鼠标左键
action.double_click(aa).perform()#双击鼠标左键
action.click_and_hold(aa).perform()#单击鼠标左键，不松开
action.context_click(aa).perform()#点击鼠标右键
action.drag_and_drop(aa,bb).perform()#aa拖拽到bb然后松开

#模拟键盘----------------------------------------------------------------------------
driver.find_element(By.XPATH, '//div[@id="11"]').send_keys(keys.BACKSPACE)
driver.find_element(By.XPATH, '//div[@id="11"]').send_keys(keys.ENTER)
driver.find_element(By.XPATH, '//div[@id="11"]').send_keys(keys.ESCAPE)
driver.find_element(By.XPATH, '//div[@id="11"]').send_keys(keys.SPACE)
driver.find_element(By.XPATH, '//div[@id="11"]').send_keys(keys.DELETE)
#driver用法-----------------------------------------------------------------------------
driver.get(url)#跳转网页
driver.back()#上一页
driver.forward()#下一页
driver.refresh()#刷新页面
driver.close()#关闭当前页面
driver.quit()#关闭所有打开的页面 
driver.set_window_size(200, 200)#设置浏览器的宽高
driver.set_window_position(300, 300)#设置浏览器相对window页面的位置
driver.get_window_position()#可获取浏览器相对window页面的位置
driver.get_window_size()#可获取浏览器的宽高
driver.maximize_window()#页面放到最大
driver.current_url#可获得页面的当前url地址
driver.title#获得当前页面的标题
driver.name#获取当前浏览器是哪一个
driver.page_source#获取当前页面的前端源码