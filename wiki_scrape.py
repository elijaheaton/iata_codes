import pandas as pd
import requests
from bs4 import BeautifulSoup


def update():
    url = "https://en.wikipedia.org/wiki/List_of_airline_codes"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': "wikitable"})

    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])

    df = df.drop(["ICAO", "Call sign", "Country/Region", "Comments"], axis=1).dropna()
    df.to_csv('data.csv', index=False)
