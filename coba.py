amount = (input("Enter amount: "))
try:
    amount = int(amount)
except ValueError as a:
    pass
    print(a)
if isinstance(amount, int):
    if amount < 1000:
        discount = amount * 0.05
        print("Discount", discount)
    else:
        discount = amount * 0.10
        print("Discount", discount)
    print("Net payable:", amount - discount)
else:
    print("salah")
