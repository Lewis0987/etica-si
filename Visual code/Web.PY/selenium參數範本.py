#@@元素@@
#[#]=>尋找ID   
#[.]=>className
#By.XPATH, "//*[contains(@xx, 'xx')
#input('Press Enter to exit...') 暫停操作
#driver.refresh() 刷新
#driver.back() 返回
#pip install pyperclip
#

#========================================================================================================
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"Balanço Total")]'))
    )
    print("8.2引導至儲值頁\033[32mOK\033[0m")
except TimeoutException:
    print("\033[91m" +"8.2 引導至儲值頁失敗"+ "\033[0m")

#========================================================================================================  
# 循环点击刷新按钮N次
for _ in range(1000):
    driver.find_element(By.XPATH, "//img[contains(@alt, 'refresh')]").click()
sleep(60)
print('7.連續刷新_Balance \033[32mOK\033[0m')

#========================================================================================================
#尋找較焦距元素
element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "ImageTab")]//span[text()= "Cards"]'))
        ).click()


#========================================================================================================
target_element = driver.find_element(By.XPATH,'//*[contains(text(), "A partir de agora,")]')
 # 使用 ActionChains 模拟鼠标点击
action = ActionChains(driver)
action.click(target_element).perform()

#========================================================================================================
# 單一網址開啟
''' 
################新安卓單(請輸入)###########################
url = "https://www.natal777bet.com/"
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
#========================================================================================================
 #格式字符串變量插入
name = "DJ"
age = 30
height = 188
weight = 80
print( f"\033[32mMy name is {name} and I am {age} years old then my {height} and {weight}.\033[0m")
#========================================================================================================
# 統計通知鈴的數量
print("\033[44m\033[32m" + "26. 通知鈴數量" + "\033[0m")
try:
    notification_icons = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class,'MessageCountBadge')]"))
        )
    bell_count = sum(int(icon.text) for icon in notification_icons)
    #通知鈴=通知列表數量
    print(f"26-1.通知鈴數量: \033[34m{bell_count}\033[0m")
# 判斷三項數量是否相等(總數量、通知鈴數量、未讀數量)
    if unread_count != bell_count != total_count:
        print("26-2.未讀數量、通知鈴數量皆相符，但不等於總數量\033[32m OK\033[0m")
    elif unread_count == bell_count == total_count:  ## 如果unread_count為False且bell_count為True，執行這裡的代碼
        print("26-2.未讀數量、通知鈴數量、總數量皆相符\033[32m OK\033[0m")
    else:  
        print("26-2.\033[91m" +"三項皆不符"+ "\033[0m")
except Exception as e:
    print("\033[91m" +"出現異常"+ "\033[0m", e)
#========================================================================================================
#輪播次數
counter = 0
while True:
    print("This is an infinite loop!")

    counter += 1
    if counter >= 3:
        break  # 10次​​迭代後跳出循環 Break out of the loop after 10 iterations
#========================================================================================================
# 個人視窗ID Copy功能
Account_IDCopy = WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'active:opacity-50')]"))
).click()
print('D.3.點擊Copy \033[32mOK\033[0m')
try:
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[text()="Copiado!"]')))
    print("1.1.1 複製ID按鈕 \033[32mOK\033[0m")
except TimeoutException:
    print("\033[91m" +"1.1.1 複製ID按鈕失效"+ "\033[0m")
try:
    clipboard_content = pyperclip.paste()
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,'//div[@class="flex gap-2 text-lg items-center"]'))
            )
    element_text = element.text
    number = re.search(r'\d+', element_text).group()
    if clipboard_content == number:
        print("1.1.2 複製功能 \033[32mOK\033[0m")
        print('複製的內容為:'+ clipboard_content)
    else:
        print("\033[91m" +"1.1.2 複製功能失效"+ "\033[0m")
        print('複製的內容為: '+ clipboard_content)
except TimeoutException:
    print("未找到複製內容\033[0m")

#========================================================================================================
#同層多種元素
IDCopy_message = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class = 'ant-notification-notice-message']//span[contains(@class,'ant-notification-notice-message-single-line-auto-margin')]"))
)
#EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Copiado!')]")) # 單層內針對尋找文字
#EC.presence_of_element_located((By.XPATH, "//*[(text() = 'Copiado!')]")) # 針對唯一尋找文字(不可有重複)
#========================================================================================================

## 檢查是否成功跳轉到 VIP 頁面
try: 
    VIP_element = EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Meu progresso VIP')]"))
    WebDriverWait(driver, 5).until(VIP_element)
    print('D.5-1.跳轉VIP頁 \033[32mOK\033[0m') 
except TimeoutException:
    print("\033[91m" +"D.5-1.跳轉失敗"+ "\033[0m")
#========================================================================================================

# 個人帳戶_邀請區塊
ContaPromovida = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'rounded-t-xl')]"))
)
if ContaPromovida: #(針對相同元素判斷排序[value])
    ContaPromovida[1].click()
#========================================================================================================
