sum = lambda arg: arg[0] if len(arg) == 1 else arg[-1] + sum(arg[0:-1])

print(sum((1, 2, 3, 4, 5, 6, 7)))
