import urllib.request

url = "http://www.baidu.com"
url_text = urllib.request.urlopen(url=url).read().decode('utf-8')
print(url_text)

