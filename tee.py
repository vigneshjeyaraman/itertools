import itertools as it

result = it.tee([1,2,3,4,5], 5) # duplicates given list n times here n is 5.

for i in result:
    print(list(i))