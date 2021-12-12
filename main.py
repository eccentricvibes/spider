import requests
from bs4 import BeautifulSoup


# def parse(html):
#     soup = BeautifulSoup(html, "lxml")
#     # print(soup.title)
#     page_list = soup.select(".site .site-content .content-area"
#                             " .site-main .section .row "
#                             " .site-main .posts-wrapper .col-12")
#     if page_list:
#         for pg in page_list:
#             page = pg.select(".entry-wrapper .entry-title a")[0]
#             title = page.string
#             link = page.get("href")
#             article_description = pg.select(".entry-wrapper ")
#             yield {
#                 "title": title,
#                 "article link": link,
#             }
#             # print(page_list.string)
#             # print(page_list.get("href"))
#             # print({title: link})
#     # title = page_list.string
#     # link = page_list.get("href")
#     # return {title:link}
#
#
# def spider(url):
#     html = requests.get(url)
#     if html.status_code == 200:
#         return html
#     else:
#         return "error!"
#
#
# def main():
#     url = "https://www.aiyc.top/"
#     html = spider(url).text
#     r = parse(html)
#     for i in r:
#         print(i)


# if __name__ == "__main__":
#     main()

# html = requests.get("https://aiyc.top/")
# soup = BeautifulSoup(html, "lxml")
# # print(soup.title)
# page_list = soup.select(".site .site-content .content-area"
#                         " .site-main .section .row "
#                         " .site-main .posts-wrapper .col-12")
# if page_list:
#     for pg in page_list:
#         page = pg.select(".entry-wrapper .entry-title a")[0]
#         title = page.string
#         link = page.get("href")
#         article_description = pg.select(".entry-wrapper .entry-excerpt u-text-format div")[0]
#         print(article_description)





