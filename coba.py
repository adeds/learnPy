space = 0
height = 10
for i in range(0, height):
    for k in range(0, i):
        print(' ', end='')
        space = k + 1
    for j in range(0, (height - i) * 2):
        print('*', end='')
    print("*")
    if i == height - 1:
        while space >= 0:
            print(" ", end='')
            space = space - 1
        print("*", '')
