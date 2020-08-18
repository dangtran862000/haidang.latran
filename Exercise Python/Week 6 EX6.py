n = str(input("Input"))


def delete_string(letter):
    for i in n:
        if i == str(letter):
            new_str = n.replace(i, "")
            return new_str
        else:
            continue


if delete_string("a"):
    print(delete_string("a"))
