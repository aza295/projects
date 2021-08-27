import requests
from bs4 import BeautifulSoup


last_page_number = 27

BASE_URL = 'https://www.kivano.kg/mobilnye-telefony'

def get_page(url):
      response = requests.get(url)
      return response.text


def analyze_page_things(page_things):
      soup = BeautifulSoup(page_things, 'html.parser')
      return soup


def get_product_cards(soup):
      products_list = soup.find('div', class_='list-view')
      product_cards = products_list.find_all('div', class_='item')
      return product_cards


def get_product_info(product_card):
      title_element = product_card.find('div', class_='pull-right').find('div', class_='product_text').find('div', class_='listbox_title').find('a')
      title = title_element.text
      details_link = title_element.get('href')

      price_element = product_card.find('div', class_='pull-right').find('div', class_='motive_box').find('div', class_='listbox_price')
      price = price_element.text

      image_element = product_card.find('div', class_='listbox_img').find('a').find('img')
      image_link = image_element.get('src')

      info = {
      'title': title, 
      'price': price,
      'details': f'https://www.kivano.kg{details_link}\n',
      'image': f'https://www.kivano.kg{image_link}\n'
      }

      return info


def write_to_csv(data):
      import csv
      with open('products.csv', 'w') as file:
            fieldnames = ['title', 'price', 'image', 'details']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


def main():
      products = []
      for num in range(1, last_page_number + 1):
            print(1)
            page_url = f'{BASE_URL}?page={num}'
            page_things = get_page(page_url)
            page_soup = analyze_page_things(page_things)
            product_cards = get_product_cards(page_soup)
            page_products = []
      for card in product_cards:
            print(1)
            prod = get_product_info(card)
            page_products.append(prod)
            products.extend(page_products)
            write_to_csv(products)



main()












