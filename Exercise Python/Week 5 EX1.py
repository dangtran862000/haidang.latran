def mystery_function(x, y):
    """
    do something mysterious
    """
    if x % y == 0:
        result = True
    else:
        result = False

    return result

if mystery_function(14, 5):
    print("True")
else:
    print("False")