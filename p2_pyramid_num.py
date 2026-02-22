# Program 1: Inverted Right Half Pyramid Pattern (Numbers)

num = 1

for i in range(1, 6):   # rows
    for j in range(1, i+1):   # columns
        print(num, end=" ")
        num += 1
        
        # reset to 1 after 9
        if num > 9:
            num = 1
            
    print()