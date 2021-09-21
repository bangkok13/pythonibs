r = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
new_dict = {k: v for k, v in r.items() if v >= 3}
print(new_dict)

