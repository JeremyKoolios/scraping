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
        for i in range(len(soup.find_all('p', {'class': 'address'}))):
            lead = soup.find_all('p', {'class': 'address'})[i].text

            #get individual items from lead string
            try:
                name = lead[0: lead.index(',')]
                try:
                    address = lead[lead.index(',') + 2: lead.index('+') - 1]
                except:
                    try:
                        address = lead[lead.index(',') + 2: lead.index('(') - 1]
                    except:
                        continue
                try:
                    telephone = lead[lead.index('+'): len(lead)]
                except:
                    try:
                        telephone = lead[lead.index('('): len(lead)]
                    except:
                        continue
            except:
                continue

            leads.extend([[name, address, telephone]])

        current_page += 1

        #send request and gather src code
        full_url = BASE_URL + category + '-' + str(current_page) + '.html'
        result = requests.get(full_url)
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')

    return leads




print(scrape('automotives'))