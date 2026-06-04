from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

# 获取当前日期
current_date = datetime.now()
# 获取当前年份和第几周
current_year = current_date.year
current_week = current_date.isocalendar()[1]
# 下一周
next_week = current_week + 1
# 计算下周一日期
next_monday = current_date + timedelta(days=((7 - current_date.weekday()) + 7) % 7)
# 将日期格式化为 yy-mm-dd 形式
formatted_next_monday1 = next_monday.strftime("%y/%m/%d")
# 自定义月份字典
month_dict = {
    1: "一月",
    2: "二月",
    3: "三月",
    4: "四月",
    5: "五月",
    6: "六月",
    7: "七月",
    8: "八月",
    9: "九月",
    10: "十月",
    11: "十一月",
    12: "十二月"
}
# 获取当前日期和时间
current_date = datetime.now()
# 计算下周一的日期
next_monday = current_date + timedelta(days=((7 - current_date.weekday()) + 7) % 7)
# 获取日期的年、月和日
year = next_monday.strftime("%y")
month = month_dict[int(next_monday.strftime("%m"))]
day = next_monday.strftime("%d")
# 格式化日期和时间为 dd/mm/yy 09:00 上午
formatted_next_monday = f"{day}/{month}/{year} 09:00 上午"
# 计算直到下一个周五的天数（0代表周一，4代表周五）
days_until_friday = (4 - current_date.weekday() + 7) % 7

# 如果今天是周五，天数将为0，因此我们要添加7天
if days_until_friday == 0:
    days_until_friday = 7

next_friday = current_date + timedelta(days=days_until_friday)

# 获取日期的年、月和日
year = next_friday.strftime("%y")
month = month_dict[int(next_friday.strftime("%m"))]
day = next_friday.strftime("%d")

# 格式化日期和时间为 dd/mm/yy 09:00 上午
formatted_next_friday = f"{day}/{month}/{year} 09:00 上午"


# 启动 Chromedriver
driver = webdriver.Chrome()
# 打开网页
driver.get('http://jira.he-x-tech.com:8080/secure/RapidBoard.jspa?rapidView=13&projectKey=QA&view=planning&selectedIssue=QA-10517&issueLimit=100')
WebDriverWait(driver, 10)
##帳號
driver.find_element(By.CSS_SELECTOR,"#login-form-username").send_keys('roger')
##密碼
driver.find_element(By.CSS_SELECTOR,"#login-form-password").send_keys('1qaz234%')
##登入
driver.find_element(By.XPATH, "//*[contains(@value, '登录')]").click()

sleep(2)
##创建冲刺
driver.find_element(By.CSS_SELECTOR,".js-add-sprint.aui-button").click()
sleep(2)
#打title
driver.find_element(By.CSS_SELECTOR, "#ghx-sprint-name.text").clear()
driver.find_element(By.CSS_SELECTOR, "#ghx-sprint-name.text").send_keys('QA- 2023 -w'+str(next_week) + ' -'+formatted_next_monday1)
#開始結束日期
driver.find_element(By.CSS_SELECTOR, "#ghx-sprint-start-date.text.medium-field").send_keys(formatted_next_monday)
driver.find_element(By.CSS_SELECTOR, "#ghx-sprint-end-date.text.medium-field").send_keys(formatted_next_friday)
#送出
driver.find_element(By.CSS_SELECTOR,".aui-button.aui-button-primary.ghx-add-sprint-button").click()
driver.find_element(By.CSS_SELECTOR,".aui-button.aui-button-primary.ghx-add-sprint-button").click()
sleep(2)
##########################################################################################################################
#創建問題(IN)
driver.find_element(By.XPATH, "//span[text()='创建问题']").click()
driver.find_element(By.CSS_SELECTOR,".iic-widget__summary").send_keys('[IN] API 2.0 W'+ str(next_week)+ '測試進度')
driver.find_element(By.XPATH, "//button[text()='在对话框中打开']").click()
sleep(2)
# 切换文本
driver.find_element(By.XPATH, "//button[contains(text(), '文本')]").click()
# 輸入內容
text_to_input = """h1. *IND API 2.0 issue 連結*

*Android*  
 [https://docs.google.com/spreadsheets/d/1_qvaytTbRtkVByscQh7A7HknsU623lsACCeB8naHVBM/edit#gid=1225489601]

*IOS* 
 [https://docs.google.com/spreadsheets/d/1wQRVOZQM8nnIRihOCZaCFXGNhuDtu7pXHurBrtOvmDM/edit#gid=0] 

*H5*
 [https://docs.google.com/spreadsheets/d/1WDD4jJyS_08dznc2UBvV0-k9yDufkSSJfgigxRM4sjA/edit#gid=0]

 
----
*本周進度:*
 *預計交付:*
*更新包 :*


 

 

 

 

*待測試:*

 *尚無待測產品*"""
description_element = driver.find_element(By.CSS_SELECTOR, "#description")
description_element.send_keys(text_to_input)
# 切换可视化
driver.find_element(By.XPATH, "//button[contains(text(), '可视化')]").click()
#送出
driver.find_element(By.CSS_SELECTOR,"#qf-create-another").click()
driver.find_element(By.CSS_SELECTOR,"#create-issue-submit").click()
sleep(2)
##########################################################################################################################
#創建問題(PK)
driver.find_element(By.CSS_SELECTOR,"#summary.text.long-field").send_keys('[PK] API 2.0 W'+ str(next_week)+ '測試進度')
# 切换文本
driver.find_element(By.XPATH, "//button[contains(text(), '文本')]").click()
# 輸入內容
text_to_input = """h1. *PK Api 2.0 issue 連結*

[https://docs.google.com/spreadsheets/d/1_SQ8vCXr-OVhm3YVe-sUKH-0KC0kvCgVTlNw_K8F5bw/edit#gid=1402793923]

 
----
*本周進度:*
*預計交付:*
*暫無需求交付*

 

 

 

*待測試:*


尚無待測產品"""
description_element = driver.find_element(By.CSS_SELECTOR, "#description")
description_element.send_keys(text_to_input)

# 切换可视化
driver.find_element(By.XPATH, "//button[contains(text(), '可视化')]").click()
#送出
driver.find_element(By.CSS_SELECTOR,"#create-issue-submit").click()
sleep(2)
##########################################################################################################################
#創建問題(MEX)
driver.find_element(By.CSS_SELECTOR,"#summary.text.long-field").send_keys('[MEX] API 2.0 W'+ str(next_week)+ '測試進度')
# 切换文本
driver.find_element(By.XPATH, "//button[contains(text(), '文本')]").click()
# 輸入內容
text_to_input = """h1. *MEX API 2.0 issue 連結*

[https://docs.google.com/spreadsheets/d/1hx6_1E9vcpGndxUNG04VCZhFm39htAqVW0zgpFPdNQY/edit#gid=691874283]

 
----
*本周進度:*
*預計交付:*
*待確認*

 

 

 

*待測試:*
*尚無待測產品*"""
description_element = driver.find_element(By.CSS_SELECTOR, "#description")
description_element.send_keys(text_to_input)

# 切换可视化
driver.find_element(By.XPATH, "//button[contains(text(), '可视化')]").click()
#送出
driver.find_element(By.CSS_SELECTOR,"#create-issue-submit").click()
sleep(2)
##########################################################################################################################
#創建問題(PHL)
driver.find_element(By.CSS_SELECTOR,"#summary.text.long-field").send_keys('[PHL] API 2.0 W'+ str(next_week)+ '測試進度')
sleep(2)
# 切换文本
driver.find_element(By.XPATH, "//button[contains(text(), '文本')]").click()
# 輸入內容
text_to_input = """h1. *PHL API 2.0 issue 連結*

[https://docs.google.com/spreadsheets/d/1e7-7Qu8O62UFfH5T9txvV9j1a5xOsEOu2e9T1DMn8zg/edit#gid=0]

 
----
*本周進度:*
*待確認*

 

 

 

*待測試:*
*尚無待測產品*"""
description_element = driver.find_element(By.CSS_SELECTOR, "#description")
description_element.send_keys(text_to_input)

# 切换可视化
driver.find_element(By.XPATH, "//button[contains(text(), '可视化')]").click()
#送出
driver.find_element(By.CSS_SELECTOR,"#create-issue-submit").click()
sleep(2)
##########################################################################################################################
#創建問題(EMI)
driver.find_element(By.CSS_SELECTOR,"#summary.text.long-field").send_keys('[EMI] EMI APP W'+ str(next_week)+ '測試進度')
sleep(2)
# 切换文本
driver.find_element(By.XPATH, "//button[contains(text(), '文本')]").click()
# 輸入內容
text_to_input = """h1. *EMI issue 連結*

*Android*  
[https://docs.google.com/spreadsheets/d/1cDs3W7-wi8Ef9Q5580kxmSvtBLpGG8syiZ6do-zZ07w/edit#gid=1352519080https://docs.google.com/spreadsheets/d/1_qvaytTbRtkVByscQh7A7HknsU623lsACCeB8naHVBM/edit#gid=1225489601|https://docs.google.com/spreadsheets/d/1_qvaytTbRtkVByscQh7A7HknsU623lsACCeB8naHVBM/edit#gid=1225489601]

 

 
----
*本周進度:*
*待確認*
 

 

 

*待測試:*
*尚無待測產品*"""
description_element = driver.find_element(By.CSS_SELECTOR, "#description")
description_element.send_keys(text_to_input)

# 切换可视化
driver.find_element(By.XPATH, "//button[contains(text(), '可视化')]").click()
#送出
driver.find_element(By.CSS_SELECTOR,"#create-issue-submit").click()
sleep(2)
##########################################################################################################################
#創建問題(BR)
driver.find_element(By.CSS_SELECTOR,"#summary.text.long-field").send_keys('[BR] Gaming platform W'+ str(next_week)+ '測試進度')
sleep(2)
# 切换文本
driver.find_element(By.XPATH, "//button[contains(text(), '文本')]").click()
# 輸入內容
text_to_input = """h1. Gaming platform 連結

[https://docs.google.com/spreadsheets/d/1ZAeMGHhjJ9lAGLCr_aOr9Myt5XVqOvfF7SxOCqQ4aRM/edit#gid=0]

 

 
----
*本周進度:*
*尚無待測產品*"""
description_element = driver.find_element(By.CSS_SELECTOR, "#description")
description_element.send_keys(text_to_input)

# 切换可视化
driver.find_element(By.XPATH, "//button[contains(text(), '可视化')]").click()
#送出
driver.find_element(By.CSS_SELECTOR,"#qf-create-another").click()
driver.find_element(By.CSS_SELECTOR,"#create-issue-submit").click()
sleep(10)
