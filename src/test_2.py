import json
dict = eval(open('a.txt').read())

for i,j in dict.items():
    print(i+" "+j)
