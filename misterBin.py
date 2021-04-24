import pandas as pd
import requests as r
from urllib.parse import quote
import base64

def enc(s):
	return quote(base64.b64encode(bytes(s, 'utf-8')))

u = r'https://www.tmbc.gov.uk/do-it-online/miscellaneous-forms/refuse-and-recycling-collection-dates'
u2 = r'https://www.tmbc.gov.uk/utils/tmbc_waste_services/handler.php?adr_uprn=MDEwMDEzOTIzMDk4&valid_address=MQ%3D%3D&csrf=ZWQxYzJlYjBjZWJiMjQxNTRkYzgwYjlmOTNkOWU4MTJkMDBmYzhkNA%3D%3D&sqss='

token = 'ed1c2eb0cebb24154dc80b9f93d9e812d00fc8d4'
postcode = 'tn91fx'
uprn = '010013923281'

req = f'https://www.tmbc.gov.uk/utils/pclu.php?postcode={enc(postcode)}&csrf={enc(token)}'

req2 = f'https://www.tmbc.gov.uk/utils/tmbc_waste_services/handler.php?adr_uprn={enc(uprn)}&valid_address=MQ%3D%3D&csrf={enc(token)}&sqss='

a = r.get(req)
print(a.text)