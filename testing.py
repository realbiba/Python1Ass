from src import *

n = int(input('Hello, write a number:'))

def function(x):
    list=[]
    for i in range(x):
        list.append(result[i]['name'])
    return list
print(function(n))
