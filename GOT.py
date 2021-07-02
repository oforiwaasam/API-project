import requests
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

url = 'https://game-of-thrones-quotes.herokuapp.com/v1/characters'

response = requests.get(url)
print(response.status_code)

# dictionary of random generated quote
lst = response.json()
for entity in lst:
    entity['quotes_number'] = len(entity['quotes'])

# print(lst[0])

# converting dictionary into a pandas dataframe
GOT_df = pd.DataFrame.from_dict(lst)
# print(GOT_df)

ax = GOT_df.plot.bar(x='name', y='quotes_number')
plt.show()
