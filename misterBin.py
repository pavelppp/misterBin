from html import parser
import pandas as pd
import requests
from urllib.parse import quote
import base64
from bs4 import BeautifulSoup as bs
import urllib

u = r'https://www.tmbc.gov.uk/do-it-online/miscellaneous-forms/refuse-and-recycling-collection-dates'

fp = 'refuse-and-recycling-collection-dates'
page = open(fp)
soup = bs(page.read(), features='lxml')
#soup = bs(requests.get(u, allow_redirects=True).content)

token = soup.find('input', attrs={'data-tmbc-token': 'csrf'}).attrs['value']

def enc(s):
	return quote(base64.b64encode(bytes(s, 'utf-8')))


postcode = 'tn92fb'
#uprn = '010013923281'
uprn = '010013923098'

req = f'https://www.tmbc.gov.uk/utils/pclu.php?postcode={enc(postcode)}&csrf={enc(token)}'
req2 = f'https://www.tmbc.gov.uk/utils/tmbc_waste_services/handler.php?adr_uprn={enc(uprn)}&valid_address=MQ%3D%3D&csrf={enc(token)}&sqss='

a = requests.get(req2, allow_redirects=True, headers={"Sec-Fetch-Mode":"cors"})
print(a.text)