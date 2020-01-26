list_a = ["Hello", "World", "In", "Python"]

small_list_a = [_.lower() for _ in list_a]
str_small_list_a = str(list_a).lower()


def strList_to_list(strList):
    return strList \
        .replace('[', '') \
        .replace(']', '') \
        .replace(",", '') \
        .replace("'", '') \
        .split()


small_list_a2 = list(strList_to_list(str_small_list_a))

print(list_a)
print(small_list_a)
print(str_small_list_a)
print(small_list_a2)
