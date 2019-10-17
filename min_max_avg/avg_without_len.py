# avg

numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
x = 0
sum_of_numbers = 0
counter_of_iterations = 0  # number of iterations = number of indexes of list

for i in numbers:
    i = numbers[x]
    x += 1
    sum_of_numbers += i
    counter_of_iterations += 1
    print('Positions of this number in the list: ', counter_of_iterations)
    print('Number in the list: ', i)
    print() 

print('The sum is: ', sum_of_numbers)
avg_with_len = sum_of_numbers / counter_of_iterations
print('The average of this list is: ', avg_with_len)
print(counter_of_iterations)
