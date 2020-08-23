import itertools as it

a = it.cycle([-1,0,1])

for i in range(12):
    print(next(a))