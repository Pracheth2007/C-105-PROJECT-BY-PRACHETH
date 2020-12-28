import math
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

squared_list= []
for number in data:
    r = int(number) - mean(data)
    r= r**2
    squared_list.append(r)

sum =0
for p in squared_list:
    sum =sum + p

result = sum/ (len(data)-1)

std_deviation = math.sqrt(result)
print(std_deviation)