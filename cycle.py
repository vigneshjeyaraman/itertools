import itertools as it

a = it.cycle([-1,0,1]) # pass the list that you want to cycle through

# using next(a) you can values one by one and it is an infinite sequence
# means if you run an infinite loop and call next(a) it will run forever
# amazing right.
for i in range(12):
    print(next(a))