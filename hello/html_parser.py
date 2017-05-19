from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.html
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm')) # 不是html
        for link in links:
            new_url = link['href']
            # 让 new_url 以 page_url 为模板拼接成一个全新的 url
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            print(new_url) # /view/10812319.htm
            print(new_full_url) # http://baike.baidu.com/view/10812319.htm
            new_urls.add(new_full_url)
        return new_urls