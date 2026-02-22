# right_half_pyramid.py
# Program to print Right Half Pyramid

print("Right Half Pyramid Pattern:\n")

rows = 6

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()