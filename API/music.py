import re
import requests

url = "https://music.163.com/discover/toplist?id=3778678"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

repones = requests.get(url=url, headers=headers)

# print(str(repones.text))


html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', str(repones.text))
print(html_data)

for num_id, title in html_data:
    music_url = f'http://music.163.com/song/media/outer/url?id={num_id}.mp3'
    music_content = requests.get(url=music_url, headers=headers).content
    with open("O:\music\\" + title + ".mp3", mode="wb") as f:
        f.write(music_content)
print(num_id, title)

# http://music.163.com/song/media/outer/url?id=1974443814