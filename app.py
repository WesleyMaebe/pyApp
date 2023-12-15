import random

def calculating(a,b):
  if (a == b):
     return multiplying(adding(a, b), adding(a,b))
  if (a > b):   
     return -10
  else:
    return b

def adding(a, b):
    return a + b

def multiplying(a,b):
   return a * b

for _ in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 5)
    total_points = calculating(a, b)
    print(total_points)