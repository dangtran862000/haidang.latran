list_num = [1, 5, 10, 3, 7, 2, 9, 20, 2]


def sum_even(list_num):
    sum_element = 0
    for i in list_num:
        if i % 2 == 0:
            sum_element = sum_element + i
    return sum_element


print(sum_even(list_num))
