n = str(input("Input "))


def delete_string(string_delete):
    string_delete = str(string_delete)
    if (n.find(string_delete)) >= 0:
        new = n.replace(string_delete, "")
        return new


if delete_string("dang"):
    print(delete_string("dang"))
