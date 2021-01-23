from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = 'https://www.vegetables.co.nz/vegetable-classification/fruits/'
response = http.request('GET', url)
soup = BeautifulSoup(response.data)
teste
print(soup)