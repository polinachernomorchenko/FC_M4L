import requests
from lxml import html


main_list = []
counter = 0
url = input('Вставьте ссылку на стартовую страницу: ')
d = 2


def get_parsed_page(url):
    response = requests.get(url)
    parsed_page = html.fromstring(response.content)
    return parsed_page


def get_page_urls(page):
    urls = page.xpath('//p/a[@title]/@href')
    titles = page.xpath('//p/a/text()')

    for i in range(len(urls)):
        urls[i] = 'https://ru.wikipedia.org/' + urls[i]

    di = {}
    for i in range(len(urls)):
        if len(titles) > i:
            di[titles[i]] = urls[i]

    return di


def rec(di, counter, d):
    big_list = []
    if counter < d:
        for i in di:
            page = get_parsed_page(di[i])
            dic = get_page_urls(page)
            big_list.extend([i for i in dic])
        counter += 1
        if counter < d:
            a = rec(dic, counter, d)
            big_list.extend(a)

    return big_list


page = get_parsed_page(url)
di = get_page_urls(page)
big_list = rec(di, counter, d)
big_list.insert(0, [i for i in di])
print(big_list)


