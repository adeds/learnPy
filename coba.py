def changeme(gg, a=None):
    if a is None:
        a = [4]
    a.append([1, 2, 3, 4])
    print('{} di dalam fungsi: {}'.format(gg, a))


mylist = [10, 20, 30]
changeme('hwaaaa')
print('Nilai di luar fungsi: {}'.format(mylist))
