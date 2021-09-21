numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]


def delen(num):
    if (num % 2) != 0:
        return True
    else:
        return False
a = list(filter(delen, numbers))

for g in a:
    if g > 50:
     print(g)

