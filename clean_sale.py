import csv

with open('import.csv', 'r') as file:
# with open('test1.csv', 'r') as file:
    reader = csv.reader(file)
    ln=0
    for row in reader:
        ok =False
        for i in row:
            if( 'lender' in i.lower()):
                ok=True

        if row[0]=='LOAN' and ok :
            with open('data_lender.csv', mode='a') as open_file:
                open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                open_writer.writerow(row)