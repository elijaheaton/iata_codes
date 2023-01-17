from datetime import datetime
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup


class Converter:
    last_updated = None
    database = {}

    def __init__(self):
        self.last_updated = datetime.now()
        with open('data.csv', 'r') as data:
            for line in csv.reader(data):
                self.database[line[0]] = line[1]

    def update(self):
        update()
        self.last_updated = datetime.now()

    def last_update(self):
        return self.last_updated

    def get_name(self, code):
        if code in self.database:
            return self.database[code]
        else:
            raise Exception("Code not in the database.")


def update():
    url = "https://en.wikipedia.org/wiki/List_of_airline_codes"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': "wikitable"})

    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])

    df = df.drop(["ICAO", "Call sign", "Country/Region", "Comments"], axis=1).dropna()
    df.to_csv('data.csv', index=False)
