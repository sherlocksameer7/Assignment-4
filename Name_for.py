def prefix_adder(l1):
    l2 = []

    for i in l1:
        if len(i) > 0:
            l2.append("Dr. " +i)
        return l2

    l1 = ["Sameer", "Sherlock", "Strange", "Dhanush"]
    print(prefix_adder(l1))