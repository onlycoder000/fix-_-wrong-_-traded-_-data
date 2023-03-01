
import csv
import sys
import re 


z='broker'
unsual=[]

with open('data1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for i in row:
            if i.find(':') > -1:
                s=i.split(':')
                unsual.append(s[0]+':')
    
unsual=list(set(unsual))
for z in unsual:
    if 'note' in z.lower():
        pass
    elif 'we are looking' in z.lower():
        pass
    elif 'postal owner or broker' in z.lower():
        pass
    elif 'broker' in z.lower():
        unsual.remove(z)
        print('removed: '+z)



with open('data1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        d=[]
        for i in row:
            ok=False
            for z in unsual:
                if(not i.find(z) == -1):
                    ok=True

            if ok or not i :
                pass
            elif len(re.findall("#", i)) > 3:
                pass
            else:
                d.append(i)


        with open('data.csv', mode='a') as open_file:
            open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            open_writer.writerow(d)
                