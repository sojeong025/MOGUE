import requests
from bs4 import BeautifulSoup
import json

total_data = []
k = 0

base_url = "http://www.cine21.com/news/issue/list/"

for page in range(1, 3):
    url = base_url + f"?page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    news_list = soup.select("#content > div > ul > li")

    for index, news in enumerate(news_list, start=1):
        if index == 5:
            continue

        mag_id = int(news.select_one("a")["href"].split("=")[-1])
        content_url = f"http://www.cine21.com/news/issue/view/?mag_id={mag_id}"

        response = requests.get(content_url)
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
        k += 1
        print(k)

with open("rawHTML_data.json", "w", encoding="utf-8") as w:
    json.dump(total_data, w, indent="\t", ensure_ascii=False)
