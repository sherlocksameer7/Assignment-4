def type_adder(l1):
    l2 = []

    for i in l1:
        l2.append(type(i))
    return l2

l1 = [3.14, 66, "Teddy", [], {}]
print(type_adder(l1))