def maximum(list_integer):
    count = 0
    for i in list_integer:
        while i >= list_integer[count]:
            count = count + 1
            if count == len(list_integer):
                return i
        count = 0


list_integer = [1, 5, 10, 3, 7, 2, 9, 20, 2]

print(maximum(list_integer))
