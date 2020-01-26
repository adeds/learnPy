def printinfo(*args, **kwargs):
    for a in args:
        print('argumen posisi {}'.format(a))
    for key, value in kwargs.items():
        print('argument kata kunci {}:{}'.format(key, value))
    else:
        print("selesai\n")


# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i': 7, 'j': 8})
