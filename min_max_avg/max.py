numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

best = numbers[0]

for number in numbers:
    if number > best:
        best = number

print()
print('Maximum value of this list is: ', best)
print()
