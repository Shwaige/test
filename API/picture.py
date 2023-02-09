import re
import requests


for i in range(2,65):
    base_url = "https://pic.netbian.com"
    url = f"https://pic.netbian.com/4kmeinv/index_{i}.html"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

    response = requests.get(url, headers)
    response.encoding = response.apparent_encoding  # 编码 html 网页
    # print(response.text)
    date_url = re.findall('<img src="(.*?)" alt="(.*?)"', str(response.text))  # 使用正则匹配链接地址
    # title = re.findall('alt="(.*?)"', str(response.text))
    # print(date_url)
    # # print(title)
        #
    #    url_list = [base_url + x for x in date_url]  # 拼接网站地址 和 获取的链接地址
    # print(url_list)

    for url_id,title in date_url :
        picture_url = f'https://pic.netbian.com{url_id}'
        picture_content = requests.get(url=picture_url, headers=headers).content
        with open("O:\picture\\" + title + ".jpg", mode="wb") as f:
            f.write(picture_content)
