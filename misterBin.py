import base64
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup as bs

def enc(s):
	return quote(base64.b64encode(bytes(s, 'utf-8')))

u = r'https://www.tmbc.gov.uk/do-it-online/miscellaneous-forms/refuse-and-recycling-collection-dates'

# parse preloaded html
soup = bs(open('refuse-and-recycling-collection-dates').read(), features='lxml')

# OR load html (not working for some reason ATM)
#soup = bs(requests.get(u, allow_redirects=True).content)

token = soup.find('input', attrs={'data-tmbc-token': 'csrf'}).attrs['value']

postcode = 'tn92fb'
#uprn = '010013923281'
uprn = '010013923098'

sget_addresses = f'https://www.tmbc.gov.uk/utils/pclu.php?postcode={enc(postcode)}&csrf={enc(token)}'
sget_dates = f'https://www.tmbc.gov.uk/utils/tmbc_waste_services/handler.php?adr_uprn={enc(uprn)}&valid_address=MQ%3D%3D&csrf={enc(token)}&sqss='
# with fresh token from line 17 use these ^^^ links in browser, line #28-30 will work but only with right headers added

# not working, need to tweak headers to make it work
addresses = requests.get(sget_addresses, allow_redirects=True, headers={"Sec-Fetch-Mode":"cors"})
dates = requests.get(sget_dates, allow_redirects=True, headers={"Sec-Fetch-Mode":"cors"})
