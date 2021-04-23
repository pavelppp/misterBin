import pandas as pd
import requests as r

u = r'https://www.tmbc.gov.uk/do-it-online/miscellaneous-forms/refuse-and-recycling-collection-dates'

pc = r'https://www.tmbc.gov.uk/utils/pclu.php?postcode='

z = r'https://www.tmbc.gov.uk/utils/pclu.php?postcode=dG45IDJmYg%3D%3D&csrf=NzA5MWVhNDhhMDdkNDhkOGVlNDVmMGU5YTA5NmM0ZDIyZGQ5Yjk5Zg%3D%3D'

z2 = r'https://www.tmbc.gov.uk/utils/pclu.php?postcode=dG45IDJmYg%3D%3D&csrf=NzA5MWVhNDhhMDdkNDhkOGVlNDVmMGU5YTA5NmM0ZDIyZGQ5Yjk5Zg%3D%3D'

# r = pd.read_json(z)
# print(r)

a = r.get(z)
print(a.text)