import pyautogui
import time

def switch_to_english_input():
    # 切換輸入法到英語（模擬按下 Alt + Shift）
    pyautogui.hotkey('alt', 'shift')
    time.sleep(1)  # 等待1秒以確保切換完成

def create_account():
    # 切換輸入法到英語
    switch_to_english_input()
    
    # 點擊登入按鈕
    pyautogui.click(login_x, login_y)
    time.sleep(1)  # 根據需要調整等待時間

    # 點擊創帳號按鈕
    pyautogui.click(register_x, register_y)
    time.sleep(1)

    # 在acc創建帳號欄位輸入account的內容
    pyautogui.click(acc_x, acc_y)
    pyautogui.typewrite(account[0], interval=0.1)
    time.sleep(1)

    # 點擊acc創建確認按鈕
    pyautogui.click(acclick_x, acclick_y)
    time.sleep(1)

def enter_promo_codes():
    # 優惠碼列表
    promo_codes = ["KFGKUJC5R6", "477MQL98YA", "WP6YN23J96", "QGTBR4M4B3", "EZCHE6BAGS", "5VQVYE2NJY", "HTYXCTYY8B", "HN4PDR52VY", "NXAXZERBU5", "K4RQAK6AJ7", "HCNM9VHANB"]

    # 點擊系統按鈕
    pyautogui.click(system_x, system_y)
    time.sleep(1)
    
    # 點擊序號兌換按鈕
    pyautogui.click(serial_exchange_x, serial_exchange_y)
    time.sleep(1)

    # 輸入框位置
    x, y = 1521, 1000  # 替換為你的輸入框的實際位置
    # 確定按鈕位置
    confirm_x, confirm_y = 1560, 1135  # 替換為你的“確定”按鈕的實際位置
    
    # 迭代輸入每個優惠碼
    for promo_code in promo_codes:
        # 移動滑鼠到輸入框位置並點擊
        pyautogui.click(x, y)
        
        # 清空輸入框
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')

        # 輸入優惠碼
        pyautogui.typewrite(promo_code, interval=0.1)

        # 點擊確定按鈕
        pyautogui.click(confirm_x, confirm_y)

        # 等待一段時間以確保操作完成（根據需要調整時間）
        time.sleep(1)

def delete_account():
    # 切換輸入法到英語
    switch_to_english_input()
    
    # 點擊系統按鈕
    pyautogui.click(system_x, system_y)
    time.sleep(1)

    # 點擊刪除帳號按鈕
    pyautogui.click(delete_account_x, delete_account_y)
    time.sleep(1)

    # 點擊輸入密碼欄位並輸入密碼
    pyautogui.click(password_input_x, password_input_y)
    pyautogui.typewrite(password[0], interval=0.1)
    time.sleep(1)

    # 點擊確認密碼欄位並輸入密碼
    pyautogui.click(confirm_password_input_x, confirm_password_input_y)
    pyautogui.typewrite(password[0], interval=0.1)
    time.sleep(1)

    # 點擊刪除確認按鈕
    pyautogui.click(confirm_deletion_x, confirm_deletion_y)
    time.sleep(1)
    
    # 點擊確認刪除
    pyautogui.click(final_confirm_deletion_x, final_confirm_deletion_y)
    time.sleep(1)
    
    # 點擊刪除後確認返回登入頁
    pyautogui.click(return_to_login_x, return_to_login_y)
    time.sleep(1)
    
    # 點擊清除快取
    pyautogui.click(clear_cache_x, clear_cache_y)
    time.sleep(1)
    
    # 點擊確認清除快取
    pyautogui.click(confirm_clear_cache_x, confirm_clear_cache_y)
    time.sleep(1)

# 主程式
if __name__ == "__main__":
    print("選擇功能：")
    print("1. 創建帳號")
    print("2. 輸入優惠碼")
    print("3. 刪除帳號")
    choice = input("請輸入選擇的功能號碼：")

    # 登入按鈕位置
    login_x, login_y = 2286, 1404
    # 創帳號按鈕位置
    register_x, register_y = 1509, 1222
    # 輸入帳號
    account = ["joyjoyj"]
    # acc創建欄位位置
    acc_x, acc_y = 1640, 852
    # acc創建確認按鈕位置
    acclick_x, acclick_y = 1539, 1159

    # 系統按鈕位置
    system_x, system_y = 2397, 1414
    # 序號兌換按鈕位置
    serial_exchange_x, serial_exchange_y = 1050, 1343
    # 刪除帳號按鈕位置
    delete_account_x, delete_account_y = 1989, 799
    # 輸入密碼欄位位置
    password_input_x, password_input_y = 1629, 868
    # 確認密碼欄位位置
    confirm_password_input_x, confirm_password_input_y = 1627, 988
    # 刪除確認按鈕位置
    confirm_deletion_x, confirm_deletion_y = 1361, 1104
    # 確認刪除
    final_confirm_deletion_x, final_confirm_deletion_y = 1343, 1083
    # 刪除後確認返回登入頁
    return_to_login_x, return_to_login_y = 1512, 731
    # 清除快取
    clear_cache_x, clear_cache_y = 723, 1263
    # 確認清除快取
    confirm_clear_cache_x, confirm_clear_cache_y = 1412, 740
    # 密碼
    password = ["joyjoy"]

    if choice == "1":
        create_account()
    elif choice == "2":
        enter_promo_codes()
    elif choice == "3":
        delete_account()
    else:
        print("無效的選擇")
