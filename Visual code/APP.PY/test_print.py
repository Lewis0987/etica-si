from colorama import Fore,Style
name = "DJ"
age = 30
height = 188
weight = 80

print( Fore.GREEN + "This is a success message!" + Style.RESET_ALL)
print( Fore.BLUE +'複製的內容為: ' + 'DJ', Style.RESET_ALL)    # 複製及DJ皆藍色
print('複製的內容為: ' + Fore.BLUE + 'DJ' + Style.RESET_ALL)# 複製不調色+DJ藍色
print( Fore.BLUE + '複製的內容為:' + Style.RESET_ALL + ' DJ') # 複製藍色+DJ不調色
print("\033[91m" +'複製的內容為: '+ "\033[0m" + Fore.BLUE + 'DJ' + Style.RESET_ALL) # 複製紅色+複製內容顏色
print("\033[33m回到首頁 \033[0m")
print( f"\033[32mMy name is {name} and I am {age} years old then my {height} and {weight}.\033[0m")
print('D.4-1.Copy成功訊息 \033[32mOK\033[0m') 
print("\033[91m" +"D.4.Copy功能失效"+ "\033[0m")
print("\033[107m\033[30m" + "A.[登入/註冊]" + "\033[0m")
print("\033[107m\033[30m" + "D.[Account interface]" + "\033[0m")
print("\033[44m\033[32m" + "2. 通知列表信件數量" + "\033[0m")


'''
print('15.點擊header_Recarregar Cashback \033[32mOK\033[0m')  
print("\033[33m子選單收合 \033[0m")


#Print 表現風格
print("\033[103m\033[30m" + "[登入/註冊]" + "\033[0m")

#C.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Header bar]完成
print("\033[107m\033[30m" + "C.[Header bar]" + "\033[0m")

print("\033[102m\033[30m" + "C.[Header bar]完成" + "\033[0m")

def greet(name):
    print("Hello, " + name + "!")
'''