from bs4 import BeautifulSoup #匯入BS套件
import urllib.request as req #匯入urllib 套件

file=open("dcard.txt",mode="w",encoding="utf-8") #開啟一個文檔
url="https://www.dcard.tw/f" #設置要爬蟲的第一頁

request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })

with req.urlopen(request) as response:
    data=response.read().decode("utf-8") #中文編碼

#解析原始碼，取的每篇文章的標題以及內文連結
root=BeautifulSoup(data, "html.parser")
titles=root.find_all("div",class_="atm_9s_1txwivl atm_h_1h6ojuz atm_vv_1q9ccgz atm_sq_1l2sidv atm_ks_15vqwwr atm_7l_oumlfv atm_1u2fww4_af0gpl lwxksid") #尋找class="title"的div標籤

for title in titles:
    if title.div != None: #如果標題包含a標籤(沒有被刪除)，印出來
        file.write(title.div.string +"\n") #寫入標題

file.close()