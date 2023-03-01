import csv
import json

data=[]
with open('data_seamless.csv', 'r') as file:
# with open('test1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(json.dumps(row))

print(len(data))
data=list(set(data))
print(len(data))


for r in data:
    with open('data_seamless_final.csv', mode='a') as open_file:
        open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        open_writer.writerow(json.loads(r))


