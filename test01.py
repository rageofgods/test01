import random
a = True
b = False

c = random.randint(1, 100)
d = random.choice(['ABC', 'DEF'])

if c < 50:
    a = True
if c > 50 and c < 100:
    a = False

print(c)
print(a)
print(d)