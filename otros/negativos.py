numbers = [23, 78, 98,78,65,-36,78,99]

print('Found a negative number' if any([n <0 for n in numbers]) else 'No negative number in the list')