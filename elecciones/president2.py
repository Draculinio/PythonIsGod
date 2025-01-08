import random

kamala = 0
for _ in range(80000):
    if random.randint(0,1)==1:
        kamala +=1 
print(kamala)