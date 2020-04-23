import requests
import bs4
def picture_download(adress):
    adress_html = requests.get(adress)
    parser = bs4.BeautifulSoup(adress_html.text, 'html.parser')
    pictures = parser.find_all('img')
    return pictures
    # print(parser.title)
    # print(parser.title.string)
    # i = 0
    # for picture in pictures:
    #     name = picture.get('alt')
    #     adres = picture.get('src')
    #     print(name)
    #     print(adres)
    #     picture = requests.get(adres).content
    #     with open(f'pictures/picture_{i}.jpg', 'wb') as file:
    #         file.write(picture)
    #         i += 1

def documents_download(adress):
    adress_html = requests.get(adress)
    parser = bs4.BeautifulSoup(adress_html, 'html.parser')
    documents = parser.find_all('a')
    return documents