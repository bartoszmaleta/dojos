# working

doors = [0]*100
print(doors)
for tries in range(1, 101):
    for number_of_door in range(tries-1, 100, tries):
        if doors[number_of_door] == 0:
            doors[number_of_door] = 1
        elif doors[number_of_door] == 1:
            doors[number_of_door] = 0

opendoors = []
for i, value in enumerate(doors):
    if value == 1:
        opendoors.append(i+1)


print('Opened doors: ', opendoors)