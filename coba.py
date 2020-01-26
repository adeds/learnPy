space = 0
for i in range(0, 5):
    for k in range(0, i):
        print(' ', end='')
        space = k + 1
    for j in range(0, (5 - i) * 2):
        print('*', end='')
    print("*")
    if i == 4:
        while space >= 0:
            print(" ", end='')
            space = space - 1
        print("*")
