from selenium import webdriver
from selenium.webdriver.common.by import By
# Keys 可模擬鍵盤
from selenium.webdriver.common.keys import Keys
import time
# Explicit Waits
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome driver 可對瀏覽器做操作
# 下載chrome driver 解壓縮後，將資料夾中chromedriver.exe之路徑記錄下來
# 路徑的 反斜線 要改回 斜線，且要加上檔案名稱
# PATH = "C:/Users/tamy8/Desktop/learning/coding/python/selenium 網頁自動化/chromedriver.exe"
# driver = webdriver.Chrome(PATH)

# PATH = "C:/Users/tamy8/Desktop/learning/coding/python/selenium 網頁自動化/chromedriver.exe"
# driver = webdriver.Chrome(PATH)

# 版本新的selenium不需要設置driver的路徑，selenium可以自己處理瀏覽器和驅動程序
driver = webdriver.Chrome()

# 設定瀏覽器要開啟的網頁
driver.get("https://www.dcard.tw/f")

# 取得網頁標題
# print(driver.title)

# 以name屬性取得html元素
search = driver.find_element(By.NAME, "query")
# 於html輸入框中輸入指定文字
search.send_keys("何冰嬌")
# 按下ENTER
search.send_keys(Keys.RETURN)

# 等待瀏覽器 最多10秒 直到某個html元素出現(用以等待搜尋結果出現)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "d_kw_1x"))
)

# 以class屬性取得多個html元素
titles = driver.find_elements(By.CLASS_NAME, "d_d7_1hcvtr6")
# titles資料型態 為 列表
for title in titles:
    print(title.text)
    # 取得title存放的標籤們內的文字


# 指定運行時間
time.sleep(5)

# 關閉瀏覽器
driver.quit()
