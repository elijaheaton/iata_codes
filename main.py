from datetime import datetime
import csv

from wiki_scrape import update


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
