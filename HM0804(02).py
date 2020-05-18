# 1
guess_me = 7
if (guess_me < 7):
    print("to low")
elif (guess_me > 7):
    print("to high")
else:
    print("just right")

# 2
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    elif start > guess_me:
        print('oops')
        break
    start += 1

# 3
for value in [3, 2, 1, 0]:
    print(value)


# 4
def good():
    return ['Harry', 'Ron', 'Hermione']


print(good())


# 5
class OopsException(Exception):
    pass


try:
    raise OopsException
except OopsException:
    print('Caught an oops')

# 6

import math

square_rt = lambda x: math.sqrt(x)
print(square_rt(49))
