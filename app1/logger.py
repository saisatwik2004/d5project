import csv
from datetime import datetime

def log_prediction(actual, predicted, filename='labels.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), actual, predicted])
