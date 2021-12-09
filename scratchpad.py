given = [3, 2, 1, 42, 3, 1, 0, 5, 1]

for i in range(10):
    given.append(given.pop(0))
    given[6] += given[8]
    print(given)
