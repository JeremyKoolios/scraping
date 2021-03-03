import requests
from bs4 import BeautifulSoup



#soup = BeautifulSoup(src, 'html.parser')

def scrape(category = ''):
    BASE_URL = 'https://www.nzdirectory.co.nz/'

    full_url = BASE_URL + category + '.html'
    result = requests.get(full_url)
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')

    leads = []
    leads = soup.find_all("p", {"class": "address"})
    for lead in leads:
        print(lead.text)




scrape('automotives')