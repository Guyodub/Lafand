import requests
from bs4 import BeautifulSoup

links = []
url = "https://sw.globalvoices.org/"
url2 = "https://sw.globalvoices.org/page/10/"
def scrap_text(url):
    r1 = requests.get(url)
    mypage = r1.content

    soup1 = BeautifulSoup(mypage, "html.parser")
    article = soup1.find_all('div', class_='post-summary-content')

    txt=article[0].get_text()
    sw_links = open("links.sw","a")

    for div in article:
        links = div.findAll('a')
        for a in links:
            link = a['href']
            print (link)
            sw_links.write(link + "\n")


scrap_text(url2)

