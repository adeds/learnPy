list_a = ["Hello", "World", "In", "Python"]
small_list_a_1 = str(list_a).lower()
small_list_a_2 = [_.lower() for _ in list_a]
print(small_list_a_1)
print(small_list_a_2)