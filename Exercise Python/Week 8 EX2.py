list_integer = [1, 5, 10, 3, 7, 2, 9, 20, 2]


def maximum():
    a = 0
    for i in list_integer:
        while i >= list_integer[a]:
            a = a + 1
            if a == len(list_integer):
                print(i)
                break
        a = 0


maximum()
