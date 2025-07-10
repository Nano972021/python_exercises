"""
Get the largest number in a list
1. Generate a random list from 1 - 100,000, has 20 elements, and call it 'lst'
2. Create an integer varialbe 'maximum' to represent the maximum number in the list
3. initiate 'maximum' with the first value in the list
4. Loop over the list while comparing each item with 'maximum':
    4.1. if the current value in the list is greater than maximum:
        4.1.1. Set 'maximum' to the current value
    4.2 If the current value is less than or equal 'maximum':
        4.2.1. Continue the loop
    4.3. If the list has no more values:
        4.3.1. Stop the loop
5. Display the maximum value in the console
"""
from random import randint
lst = [randint(1, 100000) for item in range(20)]
print(lst)

maximum = lst[0]
for item in range(1, len(lst)):
    if lst[item] > maximum:
        maximum = lst[item]

    else:
        continue

print(maximum)
