import sqlalchemy
from sqlalchemy import create_engine
from collections import defaultdict
import pandas as pd
import requests

url = 'https://quotable.io/quotes?author=albert-einstein'

details = requests.get(url)
print(details.status_code)
# dictionary of einstein quotes
dict = details.json()
# list of famous quotes with details
quotes_info = dict['results']
my_dict = defaultdict(list)
# print(quotes_info)
for d in quotes_info:
    for key, value in d.items():
        my_dict[key].append(value)

# converting dictionary into a pandas dataframe
quotes_df = pd.DataFrame.from_dict(my_dict)
quotes_df = quotes_df.drop(columns=['tags'])
# print(quotes_df)

engine = create_engine('mysql://root:codio@localhost/einstein_quotes')
quotes_df.to_sql('einstein_table', con=engine,
                 if_exists='replace', index=False)
