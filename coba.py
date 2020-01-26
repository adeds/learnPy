def sum(arg1, arg2):
    # Add both the parameters and return them.
    total = arg1 + arg2
    print('{} the function: {}'.format("inside",total))
    return total
# Panggil sum
total = sum(10, 20);
print('Outside the function: {}'.format(total))