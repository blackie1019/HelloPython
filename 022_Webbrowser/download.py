import requests

res = requests.get('http://natasha.pixnet.net/blog/post/43626142-%5B%E5%B7%A5%E5%95%86%5D-sodastream.power-source%E6%B0%A3%E6%B3%A1%E6%B0%B4%E6%A9%9F')
print(res.status_code)
print(res.content)

downloadFile = open('web.txt','wb')
for chunk in res.iter_content(50000):
    downloadFile.write(chunk)

downloadFile.close()