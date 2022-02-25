import requests  # 网页请求
from bs4 import BeautifulSoup  # 美化及解析

from my_fake_useragent import UserAgent
# 伪装成浏览器
ua = UserAgent(family="chrome", os_family='windows')
ua = ua.random()


def ask_url(url_):
    # 抓取网页内容
    header = {
        "User-Agent": ua
    }
    response = requests.get(url=url_, headers=header)
    response_status = response.status_code
    if response_status == 200:
        response.encoding = "utf-8"
        response_text = response.text
        return response_text
    if response_status == 404:
        print("服务器未找到资源")


url = "https://www.baidu.com"
url_text = ask_url(url_=url)
print(url_text)

soup_text = BeautifulSoup(url_text, "html")
print(soup_text.prettify())
