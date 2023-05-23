import requests
from bs4 import BeautifulSoup
import json

total_data = []
k = 0

# 크롤링 실행 (50개까지 크롤링)


#-------------^^^기사내용^^^--------------

base_url = "http://www.cine21.com/news/issue/list/"
mag_id = 2402
for page in range(1, 21):
    url = base_url + f"?p={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    news_list = soup.select("#content > div > ul > li")
    
    content_url = "http://www.cine21.com/news/issue/view/?mag_id="

    for index, news in enumerate(news_list, start=1):
        # 5번째 게시글은 기사가 아니므로 제외
        if index == 5:
            continue

        url = content_url + str(mag_id)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        article_content = soup.select_one("#news_content").__str__()
    
        data = {
            'model': 'community.editorarticle',
            'pk': k,
            'fields': {
                'title': news.select_one("a > span.tit").text.strip(),
                'thumbnail': news.select_one("a > span.thumb > img")["src"],
                'rawHTML': article_content
            }
        }

        total_data.append(data)

        mag_id -= 1
        k += 1
        print(k)

        print(mag_id)

with open("rawHTML_data.json", "w", encoding="utf-8") as w:
    json.dump(total_data, w, indent="\t", ensure_ascii=False)