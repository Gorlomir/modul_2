import random

def password():
    numbers = range(3, 20)
    rock_1 = random.choice(numbers)
    return rock_1
result = []
rock_1 = int(password())
print(rock_1)
for i in range(1, 21):
    for j in range(1, 21):
        if rock_1 % (i + j) == 0 and i < j and (i + j) != 0 :
                result.append(str(i))
                result.append(str(j))

print(''.join(result))