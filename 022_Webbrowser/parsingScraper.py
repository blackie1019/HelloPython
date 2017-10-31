import bs4, requests

def getAWSBookCover(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    cover = soup.select('#imgBlkFront')[0]
    return cover

print(getAWSBookCover('https://www.amazon.com/Wicked-Cool-Ruby-Scripts-Difficult/dp/1593271824/ref=sr_1_1?ie=UTF8&qid=1352196496&sr=8-1&keywords=Wicked+Cool+Ruby+Scripts'))