import pyautogui
import time
import json

# 讀取配置文件
with open('config.json', 'r') as f:
    config = json.load(f)

account = config['account']
password = config['password']
coords = config['coordinates']

def switch_to_english_input():
    # 切換輸入法到英語（模擬按下 Shift）
    pyautogui.press('shift')
    time.sleep(1)  # 等待1秒以確保切換完成

def create_account():
    # 切換輸入法到英語
    switch_to_english_input()
    
    # 點擊登入按鈕
    pyautogui.click(*coords['login'])
    time.sleep(1)  # 根據需要調整等待時間

    # 點擊創帳號按鈕
    pyautogui.click(*coords['register'])
    time.sleep(1)

    # 在acc創建帳號欄位輸入account的內容
    pyautogui.click(*coords['acc_create'])
    pyautogui.typewrite(account[0], interval=0.1)
    time.sleep(1)

    # 點擊acc創建確認按鈕
    pyautogui.click(*coords['acc_confirm'])
    time.sleep(1)

def enter_promo_codes():
    # 優惠碼列表
    promo_codes = ["KFGKUJC5R6", "477MQL98YA", "WP6YN23J96", "QGTBR4M4B3", "EZCHE6BAGS", "5VQVYE2NJY", "HTYXCTYY8B", "HN4PDR52VY", "NXAXZERBU5", "K4RQAK6AJ7", "HCNM9VHANB"]

    # 點擊系統按鈕
    pyautogui.click(*coords['system'])
    time.sleep(1)
    
    # 點擊序號兌換按鈕
    pyautogui.click(*coords['serial_exchange'])
    time.sleep(1)

    # 迭代輸入每個優惠碼
    for promo_code in promo_codes:
        # 移動滑鼠到輸入框位置並點擊
        pyautogui.click(*coords['promo_input'])
        
        # 清空輸入框
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')

        # 輸入優惠碼
        pyautogui.typewrite(promo_code, interval=0.1)

        # 點擊確定按鈕
        pyautogui.click(*coords['promo_confirm'])

        # 等待一段時間以確保操作完成（根據需要調整時間）
        time.sleep(1)

def delete_account():
    
    
    # 點擊系統按鈕
    pyautogui.click(*coords['system'])
    time.sleep(1)

    # 點擊刪除帳號按鈕
    pyautogui.click(*coords['delete_account'])
    time.sleep(1)

    # 點擊輸入密碼欄位並輸入密碼
    pyautogui.click(*coords['password_input'])
    pyautogui.typewrite(password[0], interval=0.1)
    time.sleep(1)

    # 點擊確認密碼欄位並輸入密碼
    pyautogui.click(*coords['confirm_password_input'])
    pyautogui.typewrite(password[0], interval=0.1)
    time.sleep(1)

    # 點擊刪除確認按鈕
    pyautogui.click(*coords['confirm_deletion'])
    time.sleep(1)
    
    # 點擊確認刪除
    pyautogui.click(*coords['final_confirm_deletion'])
    time.sleep(1)
    
    # 點擊刪除後確認返回登入頁
    pyautogui.click(*coords['return_to_login'])
    time.sleep(1)
    
    # 點擊清除快取
    pyautogui.click(*coords['clear_cache'])
    time.sleep(1)
    
    # 點擊確認清除快取
    pyautogui.click(*coords['confirm_clear_cache'])
    time.sleep(1)

# 主程式
if __name__ == "__main__":
    print("選擇功能：")
    print("1. 創建帳號")
    print("2. 輸入優惠碼")
    print("3. 刪除帳號")
    choice = input("請輸入選擇的功能號碼：")

    if choice == "1":
        create_account()
    elif choice == "2":
        enter_promo_codes()
    elif choice == "3":
        delete_account()
    else:
        print("無效的選擇")
