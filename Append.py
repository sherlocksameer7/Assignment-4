def name_adder(l1, l2):
    for i in l1:
        if len(i) > 0:
            l2.append(i)
        return l2

l1 = ["Sherlock", "Sameer"]
l2 = ["Arijit", "Sameer"]

print(name_adder(l1, l2))