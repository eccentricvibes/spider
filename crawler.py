import requests
from bs4 import BeautifulSoup
import json
from requests.exceptions import RequestException

def parse(html):
    soup = BeautifulSoup(html, "lxml")
    page_list = soup.select(".site .site-content .content-area"
                            " .site-main .section .row "
                            " .site-main .posts-wrapper .col-12")
    if page_list:
        for pg in page_list:
            page = pg.select(".entry-wrapper .entry-title a")[0]
            title = page.string
            link = page.get("href")
            article_description = pg.select(".entry-wrapper .entry-excerpt")[0].string
            yield {
                "title": title,
                "article link": link,
                "article description": article_description,
            }




            # print(page_list.string)
            # print(page_list.get("href"))
            # print({title: link})
    # title = page_list.string
    # link = page_list.get("href")
    # return {title:link}


def save(content):
    with open("crawledarticles.txt", "a+", encoding="utf8") as f:
        f.write(str(content) + "\n")


def spider(url):
    try:
        html = requests.get(url)
        if html.status_code == 200:
            return html.text
    except RequestException as e:
        return e




def build_url():
    BASE_URL = "https://www.aiyc.top/page/{}"
    for i in range(1, 53):
        yield BASE_URL.format(i)


def main():
    for url in build_url():
        print(url)
        html = spider(url)
        r = parse(html)
        for content in r:
            save(content)



if __name__ == "__main__":
    main()
