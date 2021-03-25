from lxml import html

import time
import json

import requests
from datetime import date, timedelta


def generate_urls(path):
    main_url = "http://www.dailymail.co.uk/home/sitemaparchive/"
    start_date = date(2021, 1, 1)
    end_date = date.today()
    delta = end_date - start_date
    print(str(delta) + " days of news to be collected")
    for i in range(delta.days + 1):
        day = (start_date + timedelta(i)).strftime('%Y%m%d')
        print(day)
        url = main_url + "day_" + day + ".html"
        print(url)
        r = requests.get(url, timeout=30)
        time.sleep(3)
        html_tree = html.fromstring(r.text)
        article_links = html_tree.xpath('//ul[@class="archive-articles debate link-box"]/*/a/@href')
        articles = {}
        for i, article in enumerate(article_links):
            d = {'date': day, 'url': article}
            articles[i] = d
        with open(path + 'dailymail_day{}.json'.format(day), 'w') as f:
            json.dump(articles, f)
    return articles
