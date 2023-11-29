from bs4 import BeautifulSoup #匯入BS套件
import urllib.request as req #匯入urllib 套件

file=open("ptt_title.txt",mode="w",encoding="utf-8") #開啟一個文檔
url="https://www.ptt.cc/bbs/Baseball/index.html" #設置要爬蟲的第一頁

def getContent(url):
    #讓網頁覺得我們是正常瀏覽器，所以附加Request Headers
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8") #中文編碼

    #解析原始碼，取的每篇文章的標題以及內文連結
    root=BeautifulSoup(data, "html.parser")
    titles=root.find_all("div",class_="title") #尋找class="title"的div標籤
    
    for title in titles:
        if title.a != None: #如果標題包含a標籤(沒有被刪除)，印出來
            file.write("<<" + title.a.string + ">>" + "\n") #寫入標題
            
            
    nextLink= root.find("a",string="‹ 上頁") #找到上頁標籤
    return "https://www.ptt.cc/" + nextLink["href"]

count = 0 #設定翻頁
while count<10: #抓取300頁
    file.write("-------------------------------------第" + str(count+1) + "頁-------------------------------------" + "\n")
    #進行翻頁
    url = getContent(url)
    count += 1

file.close()