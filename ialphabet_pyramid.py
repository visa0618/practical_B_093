# Program 2: Full Pyramid Alphabet Pattern

rows = 5

for i in range(rows, 0, -1):
    
    # space for pyramid shape
    for space in range(rows - i):
        print(" ", end="")
    
    # print alphabets
    ch = 'A'
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    
    print()