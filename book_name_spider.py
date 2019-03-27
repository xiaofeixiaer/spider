#xiaofeixia
import requests
import re
from bs4 import BeautifulSoup
import os

'''
# 获取所有tag的url
url="https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")   # 解析网页信息
tabs=soup.select("#content > div > div.article > div > div > table > tbody > tr > td > a")
# 存储每个图书标签的链接
tag_urls=[]
for tab in tabs:
    url="https://book.douban.com/tag/"+tab.string
    tag_urls.append(url)
print(tag_urls)
'''

# html='<a href="/tag/小说?start=40&amp;type=T">3</a>'
tag_content=requests.get("https://book.douban.com/tag/小说")
soup=BeautifulSoup(tag_content.text,"lxml")

# print(soup)
# # titles=soup.select("#subject_list > ul > li> div.info > h2 > a")
pages=re.findall(r'<a href="(.*?)(\d+)&amp;type=T"',soup.decode("utf-8"))
end_num=int(pages[-2][1])
part_path=pages[1][0]
page_urls=[]
# 暂时爬取几页的数据
for n in range(20,101,20):
    page_url="https://book.douban.com"+part_path+str(n)+"&type=T"
    page_urls.append(page_url)
print(page_urls)
save_titles=[]
for page_url in page_urls:
    page_content=requests.get(page_url)
    page_soup=BeautifulSoup(page_content.text,"lxml")
    titles = page_soup.select("#subject_list > ul > li> div.info > h2 > a")
    for title in titles:
        # print(title.string)
        save_titles.append(title.string)
print(save_titles)
with open("book.txt","w",encoding="utf-8") as f:
    for value in save_titles:
        f.write(str(value).strip())
        f.write("\n")








