import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import time

story_title = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", }


def crawler(url):
    try:
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            return html.text
        else:
            return "None"
    except RequestException as e:
        return e


def parse_directory(html):
    global story_title
    soup = BeautifulSoup(html, "lxml")
    story_title = soup.select("#info h1")[0].string
    directorys = soup.select("#list dl dd a")[9:]
    # print(directory)
    for dir in directorys:
        href = dir.get("href")
        chapter_title = dir.string
        yield {
            "href": href,
            "chapter_title": chapter_title
        }


def parse_detail_content(htmls):
    for html in htmls:
        detail_content_url = html.get("href", "https://www.aiyc.top")
        time.sleep(1)
        # print(detail_content_url)
        html = crawler(detail_content_url)
        soup = BeautifulSoup(html, "lxml")
        detail_content_title_list = soup.select(".box_con .bookname h1")
        if detail_content_title_list:
            detail_content_title = detail_content_title_list[0].string.strip()
        # contents = soup.select("#content")[0].select("p")
        contents = soup.select("#content")[0].select("p")
        # print(contents, end="\n\n\n\n")
        content_text = ""
        for content in contents:
            content = content.string.strip()
            content_text += content
        yield {
            "detailed content title": detail_content_title,
            "content": content_text
        }
        # print(content_text)

    # for content in contents:
    # 	# print(list(content.stripped_strings))
    # 	yield {
    # 		"detail_content_title": detail_content_title,
    # 		"content": content.string
    #
    # 	# print(content.text)


def save(content, filename):
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(content)


def main():
    home_url = "http://www.b520.cc/0_7/"
    html = crawler(home_url)
    content = list(parse_directory(html))
    # print(story_title)
    for i in content:
        save(str(i) + "\n", "../b520/data/story_information{}.txt".format(story_title))
    r = parse_detail_content(content)
    for index, i in enumerate(r):
        content_old = i.get("content", "default_content")
        content = content_old.split("。")
        for con in content:
            save(con + "。\n", f"data/content/{f'{index+1}' + i.get('detailed content title', 'default_name')}.md")


if __name__ == '__main__':
    main()
