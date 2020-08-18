list_integer = [1, 5, 10, 3, 7, 2, 9, 20, 2]

new_list = []


def reverse(list_integer):
    a = 0
    for i in range(0, len(list_integer)):
        new_list.append(list_integer[(a-1)])
        a = a - 1
    return new_list


print(reverse(list_integer))
