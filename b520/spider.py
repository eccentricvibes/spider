"""
1. Get the link to the story on the website, for this one it's http://www.b520.cc/0_7/
2. Scrape the story's title and link, and save it into a txt file, directory.txt/story_information.txt
3. Crawl the story's content, and store it into a folder called "content", in the format of story_title: content
"""
import time
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}


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
    page_list = soup.select("#list dl dd a")[9:]
    for page in page_list:
        chapter_link = page.get("href")
        chapter_title = page.string
        yield {"story title": story_title, "chapter title": chapter_title, "chapter_link": chapter_link}
        # print(f"Story title: {story_title}")
        # print(f"Chapter title: {chapter_title}")
        # print(f"Chapter link: {chapter_link}")

    # if page_list:
    #     for link in page_list:
    #         embed = link.select("#list dd a")
    #         embed_link = link.find("a", href=True)
    #         embed_title = link.select("#list dd")[0].string
    #         print(title)
    #         print(embed_link)
    #         print(embed_title)


def save(content, filename):
    with open(filename, "a+", encoding="utf-8") as file:
        file.write(content)


def parse_detail_content(htmls):
    for html in htmls:
        detail_content_url = html.get("chapter_link", "None")
        time.sleep(1)
        html = crawler(detail_content_url)
        soup = BeautifulSoup(html, "lxml")
        detail_content_title = soup.select(".box_con .bookname h1")
        contents = soup.select("#content p")[0].select("p")
        # print(detail_content_title)
        # print(detail_content_url)
        print(contents)


def main():
    base_url = "http://www.b520.cc/0_7/"
    html = crawler(base_url)
    content = list(parse_directory(html))
    # print(story_title)
    # for i in content:
    #     save(str(i) + "\n", "story_information{}.txt".format(story_title))
    parse_detail_content(content)


if __name__ == "__main__":
    main()
