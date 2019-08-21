import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)
        with open('output.txt', 'w') as f:
            for tag in sp.find_all('ul', class_='List'):
                url = tag.get('li')
                if url and 'html' in url:
                    print('\n' + url)
                    f.write(url + '\n')

web = 'https://www.asahi.com/news/'
Scraper(web).scrape()
