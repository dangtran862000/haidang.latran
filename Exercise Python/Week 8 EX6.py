def replace(s, old, new):
    position = 0
    for i in s:
        if i == old[position]:
            position = position + 1
            if position == len(old):
                s = s.replace(old, new)
                position = 0
                continue
    return s


print(replace("la tran hai dang", "tran", "nguyen"))
