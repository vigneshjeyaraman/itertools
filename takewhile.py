import itertools as it

result = filter(lambda x: x < 5, [1,2,3,4,5,6,7,8]) # it will take elements which fall into the condition and drop others.

for i in result:
    print(i)