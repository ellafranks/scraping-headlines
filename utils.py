import re


def url_to_headline(url):
    return re.findall('([^\/]+)(?=.html)', url)[0].replace('-', ' ')


def format_url(url):
    return 'dailymail.co.uk' + url
