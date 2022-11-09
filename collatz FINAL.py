def collatz():
    global e
    if (int(e) % 2) == 0:
        print(e, ' is even')
        e = int(e) / 2
        return e
    else:
        print(e, ' it`s odd')
        e = (int(e) * 3 + 1)
        return e

print('pass a value')
e = (input())
is_int=True
try:
    int(e)
except ValueError:
    is_int=False
if is_int:
    counter = 0
    while int(e) > 1:
        counter += 1
        collatz()
    if int(e) == 1:
        print(' "1" achieved, by', counter, 'steps')
else:
    print("OPEN YOUR EYES!!!!")