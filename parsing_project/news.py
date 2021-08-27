import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


last_page_number = 27

BASE_URL = 'https://kaktus.media/'

def get_page(url):
    '''Принимает адрес страницы, делает на неё запрос и возвращает содержимое ответа'''
    response = requests.get(url)
    return response.text


def analyze_page_content(page_content):
    '''Принимает содержимое страницы и анализирует для последующего обращения к любому элементу на странице'''
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup


def get_product_cards(soup):
    '''Принимает объект soup(обработанная страница) и вытаскивает карточки товаров
    
    find() - получает один элемент
    find_all() - получает несколько однотипных элементов
    get() - получает значение атрибута
    text - получает вложенный текст
    <a href="...">Google!</a>'''
    products_list = soup.find('a',class_="Header--tag-link")
    product_cards = products_list.find_all('div',class_="Tag--article")
    return product_cards


def get_news(news):
    '''Принимает карточку товара и отбирает из неё нужную информацию'''
    title_element = news.find('div', class_='pull-right').find('div', class_='product_text').find('div', class_='listbox_title').find('a')
    title = title_element.text
    details_link = title_element.get('href')

    price_element = news.find('a',class_="ArticleItem--name").find('img',src).find('div', class_='listbox_price')
    price = price_element.text

    image_element = news.find('div', class_='listbox_img').find('a').find('img')
    image_link = image_element.get('src')

    info = {
        'title': title, 
        'price': price,
        'image': image_link,
        'details': details_link
    }

    return info


def write_to_json(data):
    '''Принимает данные и записывает их в json файл'''
    import json
    with open('products.json', 'w') as file:
        json.dump(data, file)


def write_to_csv(data):
    '''Принимает данные и записывает их в csv файл'''
    import csv
    with open('products.csv', 'w') as file:
        fieldnames = ['title', 'price', 'image', 'details']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
    products = [] #список, в который сохраняется инфа по всем товарам со всех страниц
    for num in tqdm(range(1, last_page_number + 1), 'Проходим по страницам'):#проходим по очереди по каждой странице
        page_url = f'{BASE_URL}?page={num}'#делаем адрес для конкретной страницы
        page_content = get_page(page_url) #получаем содержимое страницы
        page_soup = analyze_page_content(page_content)#анализируем содержимое страницы
        product_cards = get_product_cards(page_soup)#получаем карточки товаров со страницы
        page_products = [] #собираем информацию по товарам на странице
        for card in tqdm(product_cards, f'Проходим по карточкам страницы {num}'):#проходим по каждой карточке товара и собираем информацию по товару
            prod = get_news(card)
            page_products.append(prod)
        products.extend(page_products)#товары со страницы закидываем в общий список
    write_to_csv(products) #записываем полученные продукты в csv файл


main()