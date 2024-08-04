# Action Chains 模擬滑鼠行為 自動玩網頁遊戲(口交惡徒)

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://tsj.tw/")

blow = driver.find_element(By.ID, "click")
blow_count =  driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]') # 注意雙引號中不能再有雙引號
# 裝 購買按鈕 的陣列
items = []
items.append(driver)
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))
# 裝 價格 的陣列
prices = []
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))

# 創建action chains物件
# 參數傳入要操作的瀏覽器
actions = ActionChains(driver)
# 點擊「吹」按鈕
actions.click(blow)

for i in range(100):
    # 執行actions chains物件上的一連串動作
    actions.perform()
    count = int(blow_count.text.replace("您目前擁有", "").replace("技術點", "")) # 轉成數字才能在後續作比較
    # 檢查3個品項價格
    for j in range(3):
        price = int(prices[j].text.replace("技術點", ""))
        # 價格低於技術點時 按下購買按鈕
        if price <= count:
            # 再建立一個action chains物件
            upgrade_actions = ActionChains(driver)
            # 移動到第j個購買按鈕上
            upgrade_actions.move_to_element(items[j])
            upgrade_actions.click()
            upgrade_actions.perform()
            break