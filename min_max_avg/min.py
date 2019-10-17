numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

min = numbers[0]

for number in numbers:
    if number < min:
        min = number

print()
print('Minimum value of this list is: ', min)
print()