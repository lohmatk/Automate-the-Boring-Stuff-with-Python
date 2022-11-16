# def collatz():
#     global e
#     if int(e) % 2 == 0:
#         print(e, ' is even')
#         e = int(e) / 2
#         return e
#     else:
#         print(e, ' it`s odd')
#         e = int(e) * 3 + 1
#         return e
#
# print('pass a value')
# e = input()
#
# is_int = True
# try:
#     int(e)
# except ValueError:
#     is_int = False
#     print("error")
# if is_int:
#     counter = 0
#     while int(e) > 1:
#         counter += 1
#         collatz()
#     if int(e) == 1:
#         print(' "1" achieved, by', counter, 'steps')
# else:
#     print("OPEN YOUR EYES!!!!")

# //////////////////

def collatz(x):
    counter = 1
    while x > 1:
        counter += 1
        if x % 2 == 0:
            print(x, ' is even')
            x = x / 2
        else:
            print(x, ' it`s odd')
            x = x * 3 + 1
    if x == 1:
        print(counter, 'циклов потребовалось, чтобы получить ЕДИНИЦУ')

def inputChecking(inp):
    if inp.isdigit():
        inp = int(inp)
        collatz(inp)
    else:
        print('stupayte na hyi')


print('pass a value')
nums = input()
inputChecking(nums)


