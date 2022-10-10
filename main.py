import requests, bs4, re


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
BASE_URL = 'https://habr.com'
HEADERS = {
    'Cookie': '_ym_d=1651947694; _ym_uid=1651947694891732970; habr_web_home_feed=/all/; hl=ru; fl=ru; __gads=ID=3e69dbc8ed5e1105:T=1665138040:S=ALNI_MZW_Cj5pVZ6_ItAbac5wV2erTugHA; _gid=GA1.2.1265475952.1665293700; _ym_isad=2; __gpi=UID=00000b627401fb21:T=1665138040:RT=1665293701:S=ALNI_MZhyFgWhTifk6VRRzcDAeiFjiaiLA; _ga=GA1.1.175892151.1651947694; _ga_34B604LFFQ=GS1.1.1665293714.2.1.1665295411.60.0.0',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'sec-ch-ua-mobile': '?0'
}

responce = requests.get(BASE_URL + '/ru/all/', headers=HEADERS).text
soup = bs4.BeautifulSoup(responce, features='html.parser')

articles = soup.find_all(class_="tm-article-snippet")
i = 0
for article in articles:
    body = article.find(class_=re.compile("article-formatted-body"))
    for word in KEYWORDS:
        if word in body.text:
            i += 1
            time = article.find('time').attrs['title']
            title = article.find('h2').text
            link = BASE_URL + article.find(class_="tm-article-snippet__readmore").attrs['href']
            print(f'{i}. {time} - {title} - {link}')
            break
