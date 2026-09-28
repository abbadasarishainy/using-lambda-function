from functools import reduce
s=[1,2,3,4,5,6,7]
d=reduce(lambda x,y:x+y,s)
print(d)
