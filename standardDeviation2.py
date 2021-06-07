import csv
import math
with open("marks2.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
print(file_data)
data=file_data[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean

print(mean(data))
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)
sum=0
for element in squared_list:
    sum=sum+element
result=sum/(len(data)-1)
standard_deviation=math.sqrt(result)
print(standard_deviation)



