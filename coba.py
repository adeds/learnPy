list_a = ["Hello", "World", "In", "Python"]

small_list_a = [_.lower() for _ in list_a]
str_small_list_a = str(list_a).lower()
small_list_a2 = list(
    str_small_list_a
    .replace('[', '')
    .replace(']', '')
    .replace(",", '')
    .replace("'",'')
    .split())

print(list_a)
print(small_list_a)
print(str_small_list_a)
print(small_list_a2)
