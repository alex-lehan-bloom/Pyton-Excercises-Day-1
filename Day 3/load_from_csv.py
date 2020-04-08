import csv

print(dir(csv))
def load_from_csv(path):
    with open(path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['last_name'], row['first_name'], row['role'])

path = "load_me.csv"

load_from_csv(path)