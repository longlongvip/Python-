from my_fake_useragent import UserAgent

ua = UserAgent(family="chrome", os_family="windows")
ua = ua.random()
print(ua)
