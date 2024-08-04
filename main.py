from selenium import webdriver

# chrome driver 可對瀏覽器做操作
# 下載chrome driver 解壓縮後，將資料夾中chromedriver.exe之路徑記錄下來
# 路徑的 反斜線 要改回 斜線，且要加上檔案名稱
# PATH = "C:/Users/tamy8/Desktop/learning/coding/python/selenium 網頁自動化/chromedriver.exe"
# driver = webdriver.Chrome(PATH)

# PATH = "C:/Users/tamy8/Desktop/learning/coding/python/selenium 網頁自動化/chromedriver.exe"
# driver = webdriver.Chrome(PATH)

# 版本新的selenium不需要設置driver的路徑，selenium可以自己處理瀏覽器和驅動程序
wd = webdriver.Chrome()