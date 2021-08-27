import csv
import requests
from bs4 import BeautifulSoup



def get_html(url):
      headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
      response = requests.get(url,headers=headers)
      return response.text


def get_total_pages(html):
      soup=BeautifulSoup(html,'lxml')
      pages_ul = soup.find(id="search-filter").find('nav')
      last_page = pages_ul.find_all('li')[-1]
      total_pages = last_page.find('a').get('href').split('=')[-1]
      return (int(total_pages))

def get_page_data(html):
      soup = BeautifulSoup(html,'lxml')
      product_list = soup.find('div',class_="table-view-list image-view clr label-view").find('div',class_="search-results-table")
      products = product_list.find_all('div',class_="list-item list-label new-line")
      print(product_list)
      
      


def main():
      URL = 'https://www.mashina.kg/search/all/'
      pages = '?page='
      get_total_pages(get_html(URL))

main()
