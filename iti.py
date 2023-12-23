from bs4 import BeautifulSoup #匯入BS套件
import urllib.request as req #匯入urllib 套件

file=open("school.txt",mode="w",encoding="utf-8") #開啟一個文檔
url="https://www.com.tw/cross/university_002_112.html" #設置要爬蟲的第一頁

request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8") #中文編碼

#解析原始碼，取的每篇文章的標題以及內文連結
root=BeautifulSoup(data, "html.parser")
titles=root.find_all("div",id_="university_dep_row_height") #尋找class="title"的div標籤

for title in titles:
    if title.a != None: #如果標題包含a標籤(沒有被刪除)，印出來
        file.write(title.a.string + "\n") #寫入標題
        
        ct = title.a["href"] #抓取每則文章的超連結
        request2=req.Request(ct,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        })
        with req.urlopen(request2) as response:
            contents=response.read().decode("utf-8") #中文編碼
        
        content = BeautifulSoup(contents, "html.parser").find("a", title_ = "點擊看看==>這試場同學,他們推上哪些校系") #找出內文
        file.write(content.text + "\n")

file.close()