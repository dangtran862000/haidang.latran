list_integer = [1, 5, 10, 3, 7, 2, 9, 10, 2]
new_list = []


def count(list_integer, item):
    count_element = 0
    for i in list_integer:
        if i == item:
            count_element = count_element+1
    return count_element


def isin(list_integer, item):
    for i in list_integer:
        if i == item:
            return True
        else:
            continue
    return False


def index(list_integer, item):
    position = -1
    for i in list_integer:
        position = position + 1
        if i == item:
            return position
        else:
            continue
    return -1


def insert(list_integer, index, item):
    position = 0
    for i in list_integer:
        if position == index:
            position = position + 1
            new_list.append(item)

        else:
            position = position + 1
            new_list.append(i)
    return new_list


print(count(list_integer, 10))
print(isin(list_integer, 10))
print(index(list_integer, 9))
print(insert(list_integer, 4, "haidang"))
