def reverse(list_integer):
    new_list = []
    for position in range(-1, -len(list_integer)-1, -1):
        new_list.append(list_integer[position])
    return new_list


list_integer = [1, 5, 10, 3, 7, 2, 9, 20, 2]
print(reverse(list_integer))
