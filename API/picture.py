import re
import requests


base_url = "https://pic.netbian.com/"
url = "https://pic.netbian.com/4kmeinv/index_2.html"
heders = {"user-agent:":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}


response= requests.get(url,heders)
response.encoding = response.apparent_encoding   # 编码 html 网页
# print(response.text)



date_url = re.findall('<img src="(.*?)"',str(response.text)) #使用正则匹配链接地址
title = re.findall('alt="(.*?)"',str(response.text))
# print(date_url)
# print(title)

url_list = [base_url + x for x in date_url]  #拼接网站地址 和 获取的链接地址
print(url_list)

for i in url_list:
    print(i)
    url = i
    k_content = requests.get(url = i,headers= heders).content
    with open("/Users/zhangyong/Desktop/111\\ " + "title"+".jpg" ,mode="wb") as f :
        f.write(k_content)


