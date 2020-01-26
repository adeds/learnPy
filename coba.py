import string

list_a = ["Hello", "World", "In", "Python", "I'm"]

small_list_a = [_.lower() for _ in list_a]
str_small_list_a = str(list_a).lower()


def strList_to_list(strList):
    return strList \
        .strip(string.punctuation) \
        .replace('[', '') \
        .replace(']', '') \
        .split("', '")


small_list_a2 = list(strList_to_list(str_small_list_a))

print('list         ',list_a)
print('smal list    ',small_list_a)
print('string       ',str_small_list_a)
print('smal list2   ',small_list_a)
