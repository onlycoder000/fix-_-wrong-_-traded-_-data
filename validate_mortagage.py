import csv


with open('ready for seamless.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        z=False
        
            
        with open('data3.csv', 'r') as file2:
            reader2 = csv.reader(file2)
            for row2 in reader2:
                if row2[0] in row[0] or row[0] in row2[0]:
                    z=True
                    break
        
        if(z):
            with open('data_seamless.csv', mode='a') as open_file:
                open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                open_writer.writerow(row)