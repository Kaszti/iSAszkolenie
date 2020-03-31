import requests
import bs4
olx_html = requests.get('https://www.olx.pl/motoryzacja/samochody/')
parser = bs4.BeautifulSoup(olx_html.text, 'html.parser')
pictures = parser.find_all('img')
print(parser.title)
print(parser.title.string)
i = 0
for picture in pictures:
    name = picture.get('alt')
    adres = picture.get('src')
    print(name)
    print(adres)
    picture = requests.get(adres).content
    with open(f'pictures/picture_{i}.jpg', 'wb') as file:
        file.write(picture)
        i += 1