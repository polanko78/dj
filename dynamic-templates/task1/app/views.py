from django.shortcuts import render
import csv

def inflation_view(request):
    data = []
    template_name = 'inflation.html'
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
    context = {'data': data}

    return render(request, template_name,
                  context)