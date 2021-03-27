import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    read_budget_data = csv.reader(csvfile, delimiter=',')