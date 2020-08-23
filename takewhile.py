import itertools as it

result = it.takewhile(lambda x: x < 5, [1,2,3,4,5,6,7,8]) # it will take elements that falls into the condition and drop others.

for i in result:
    print(i)