# avg

numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
x = 0
sum_of_numbers = 0

for i in numbers:
    i = numbers[x]
    x += 1
    sum_of_numbers += i
    print('Number in the list: ', i)
    print() 

print('The sum is: ', sum_of_numbers)
avg_with_len = sum_of_numbers / len(numbers)
print('The average of this list is: ', avg_with_len)
