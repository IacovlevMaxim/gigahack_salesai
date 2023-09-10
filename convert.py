import csv
import re

with open('data/ParentChild.txt', 'r') as file:
    lines = file.readlines()

child_parent = {}

for line in lines:
    child, parent = line.strip().split('|')
    
    child_parent[child] = parent


fields = []

with open("data/new_sales.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
     
    fields = next(csvreader)
    fields.insert(1, 'Parent Material Code')

    with open('new_data/SALES.CSV', 'w', newline='') as csvfile2:
        csvwriter = csv.writer(csvfile2)
        csvwriter.writerow(fields)
        

        for row in csvreader:
            row.insert(1, child_parent[row[0]])
            csvwriter.writerow(row)



with open('data/Customer.txt', 'r') as file:
    lines = file.readlines()

child_parent = {}

for line in lines:
    v1, v2, v3, v4, v5, v6, v7, v8 = line.strip().split('|')
    
    child_parent[v1] = [v2, v3, v4, v5, v6, v7, v8]



fields = []

with open("new_data/SALES.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
     
    fields = next(csvreader)
    fields = fields[:3] + ['Volume Segment', 'Preferential Segment', 'City', 'Region', 'Channel', 'Location type'] + fields[3:]


    with open('new_data/SALES2.CSV', 'w', newline='') as csvfile2:
        csvwriter = csv.writer(csvfile2)
        csvwriter.writerow(fields)
        
        for row in csvreader:
            row = row[:3] + child_parent[row[2]][:4] + child_parent[row[2]][5:] + row[3:]
            csvwriter.writerow(row)


with open('data/Material.txt', 'r') as file:
    lines = file.readlines()

child_parent = {}

for line in lines:
    v1, v2, v3, v4, v5, v6, v7, v8 = line.strip().split('|')
    
    child_parent[v7] = [v1, v2, v3, v4, v5, v6, v8]


fields = []

with open("new_data/SALES2.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    fields = fields[:2] + ['Material Group Code', 'Imported Material', 'Alco Group Code', 'Unit Volume', 'Material Type', 'Package Type', 'Price Segment'] + fields[2:]

    with open('new_data/SALES3.CSV', 'w', newline='') as csvfile2:
        csvwriter = csv.writer(csvfile2)
        
        csvwriter.writerow(fields)
        

        for row in csvreader:
            row = row[:2] + child_parent[row[1]] + row[2:]
            csvwriter.writerow(row)

def extractNumber(s):
    return str(re.search(r'\d+$', s).group())

with open("new_data/SALES3.csv", 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
        
    # extracting field names through first row
    fields = next(csvreader)
    print(fields)

    with open('new_data/SALES4.CSV', 'w', newline='') as csvfile2:
        csvwriter = csv.writer(csvfile2)
        csvwriter.writerow(fields)

        for row in csvreader:
            if row[3] == 'Yes' :
                row[3] = '1'
            elif row[3] == 'No':
                row[3] = '0'
            else : 
                print("Error on Yes/no")

            row[5] = row[5].replace('"', '').replace(',', '.')

            row[6] = extractNumber(row[6])
            row[7] = extractNumber(row[7])
            row[8] = extractNumber(row[8])

            row[10] = str(ord(row[10].lower())-97)
            

            row[12] = extractNumber(row[12])

            if row[13] == 'SOUTH' :
                row[13] = '0'
            elif row[13] == 'CENTER':
                row[13] = '1'
            elif row[13] == 'NORTH':
                row[13] = '2'
            else : 
                print("Error on NORTHCENTERSOUTH")

            row[14] = extractNumber(row[14])
            row[15] = extractNumber(row[15])

            csvwriter.writerow(row)





