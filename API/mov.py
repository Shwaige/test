import re

import requests

url = "http://www.szycjbs.com/player/58147-1-1.html"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

response = requests.get(url, headers)
response.encoding = response.apparent_encoding  # 编码 html 网页
# print(response.text)

r = re.findall('data-vid="(.*?)index.m3u8" data-gf',response.text)
print(r)


for mov_url in r:
    url  = f'{mov_url}1100kb/hls/index.m3u8'
    response = requests.get(url, headers)
    print(response.text)