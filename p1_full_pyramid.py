# inverted_pyramid.py
# Simple program to print inverted pyramid

rows = 5

for i in range(rows, 0, -1):
    # print spaces
    for j in range(rows - i):
        print(" ", end="")

    # print stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()