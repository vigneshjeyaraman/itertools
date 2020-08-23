import itertools as it

result = it.dropwhile(lambda x: x < 5, [1,2,3,4,5,6,7,8]) # it will ignore elements that falls into the condition.

for i in result:
    print(i)