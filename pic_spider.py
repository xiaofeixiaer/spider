#xiaofeixia
import requests
import re


r=requests.get("https://book.douban.com/tag/小说?start=80&type=T")
print(r.text)
msg=r'img class="" src="(.*?)"'
name=r'title="(.*?)"'
pic_url=re.findall(msg,r.text)
book_name=re.findall(name,r.text)
print(book_name)
for url in pic_url:
    pic=requests.get(url)
    num=pic_url.index(url)
    root=r"pic_all/"
    path=root+book_name[num]+".jpg"
    with open(path,"wb") as f:
        f.write(pic.content)

