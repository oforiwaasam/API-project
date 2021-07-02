import pandas as pd
import requests
import sqlalchemy
import datetime
from collections import defaultdict
from sqlalchemy import create_engine


def get_json(url):
    response = requests.get(url)
    return response.json()


def build_dataframe(json):
    # creating data frame to add data to
    quote_df = pd.DataFrame.from_dict(json)
    return quote_df


def write_table(dataframe, dbName, tableName):
    engine = create_engine('mysql://root:codio@localhost/{}'.format(dbName))
    dataframe.to_sql(tableName, con=engine, if_exists='replace', index=False)


def main():
    url = 'https://api.quotable.io/random'
    json = get_json(url)
    df = build_dataframe(json)
    write_table(df, 'random_quotes', 'quotes_table')


if __name__ == "__main__":
    main()
