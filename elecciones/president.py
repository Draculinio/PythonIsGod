import random

kamala = 0
for _ in range(80000):kamala +=1 if random.randint(0,1)==1 else 0
print(kamala)