from bs4 import BeautifulSoup
import requests

def parse_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    return soup.prettify()

url = 'https://www.example.com'
print(parse_html(url))
