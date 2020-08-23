import itertools as it

lst = [1,2,3,4,5,6]
# combinations take a lst and a pair as input
itr = it.combinations_with_replacement(lst,2)
# above line of code will generate an iterator object which will have
# pair of elements
# you can access pair either by next(itr) or you have to run a loop over it

for i in itr:
    print(sum(i), i) # sum of i will return sum of the pairs if you want to see pairs just print(i)
# be careful now if you try to do next(itr) it will throw stopiteration exception and if you try to
# run a for loop it will not print anything since all the elements in iterator object is consumed