from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.com.tw/cross/university_002_112.html"

chrome_options = Options()
chrome_options.add_argument("--headless")  # 這使得瀏覽器在後台運行，無顯示窗口
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(url)
    time.sleep(5)  # 增加等待時間以確保頁面完全加載

    # 取得網頁內容
    data = driver.page_source

    with open("school.txt", mode="w", encoding="utf-8") as file:
        root = BeautifulSoup(data, "html.parser")
        titles = root.find_all("div", id_="university_dep_row_height")

        for title in titles:
            if title.a is not None:
                file.write(title.a.string + "\n")

                content_url = title.a["href"]
                time.sleep(2)  # 給予一些時間給 Cloudflare JavaScript 加載
                driver.get(content_url)
                time.sleep(5)  # 增加等待時間以確保頁面完全加載
                contents = driver.page_source

                content_root = BeautifulSoup(contents, "html.parser")
                content = content_root.find("a", title_="點擊看看==>這試場同學,他們推上哪些校系")
                file.write(content.text + "\n")

except Exception as e:
    print(f"發生錯誤：{e}")

finally:
    driver.quit()
