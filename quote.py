import requests
import pandas as pd
from collections import defaultdict

url = 'https://api.quotable.io/random'

response = requests.get(url)
print(response.status_code)

# dictionary of random generated quote
dict = response.json()
# print(dict)

# converting dictionary into a pandas dataframe
quotes_df = pd.DataFrame.from_dict(dict)
print(quotes_df.columns)
