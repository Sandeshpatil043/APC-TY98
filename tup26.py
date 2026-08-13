t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 50, 60, 70)

common = ()

for n in t1:
    if n in t2:
        common = common + (n,)

print("Common elements:", common)