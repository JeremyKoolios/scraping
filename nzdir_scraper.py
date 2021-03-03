import requests
from bs4 import BeautifulSoup



#soup = BeautifulSoup(src, 'html.parser')

def scrape(category = ''):
    BASE_URL = 'https://www.nzdirectory.co.nz/'

    #send request and gather src code
    full_url = BASE_URL + category + '.html'
    result = requests.get(full_url)
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')

    leads = []

    total_pages = len(soup.find_all('div', {'class': 'pages'}))
    current_page = 1
    while current_page <= total_pages:
        leads.extend(soup.find_all('p', {'class': 'address'}))
        current_page += 1

        #send request and gather src code
        full_url = BASE_URL + category + '-' + str(current_page) + '.html'
        result = requests.get(full_url)
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')

    for lead in leads:
        print(lead.text)




scrape('automotives')