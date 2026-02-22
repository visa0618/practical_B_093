# Program 3: Odd Numbers between 1 to 50

odd = []

# find odd numbers
for i in range(1, 51):
    if i % 2 != 0:
        odd.append(i)

# print odd numbers
print("Odd numbers between 1 and 50:")
print(odd)

# minimum 3 odd numbers
print("\nThree minimum odd numbers:")
print(odd[:3])

# maximum 3 odd numbers
print("\nThree maximum odd numbers:")
print(odd[-3:])

# average
avg = sum(odd) / len(odd)

print("\nAverage of odd numbers:")
print(avg)