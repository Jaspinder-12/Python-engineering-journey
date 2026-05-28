row = 7
for i in range(row):
    space = " " * i
    stars = "*" * (2 * (row - i ) - 1)
    print(space + stars)
    
    row = 7
for i in range(row):
    space = " " * (row - i - 1)
    stars = "*" * (2 * i + 1)
    print(space + stars)