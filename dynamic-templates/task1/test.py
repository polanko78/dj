import csv

data = []
with open('inflation_russia.csv', newline='', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        for i in range(0, 14):
            if row[i] == '':
                row[i] = '-'
            if i > 0:
                try:
                    row[i] = float(row[i])
                except Exception:
                    pass
        data.append(row)
print(data)