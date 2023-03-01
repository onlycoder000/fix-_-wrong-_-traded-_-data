import csv
from difflib import SequenceMatcher



with open('seamless.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        z=False
        for x in row:
            if 'mortga' in x or 'loan' in x:
                z=True
                break
        
        if(z):
            with open('data_seamless.csv', mode='a') as open_file:
                open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                open_writer.writerow(row)
