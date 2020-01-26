z = 0
try:
    with open("coba.py") as file:
        exec(file.read())
except FileNotFoundError:
    print('not found')
