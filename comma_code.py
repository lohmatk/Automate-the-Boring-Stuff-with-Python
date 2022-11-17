# DONE by hand
# def list_to_str(some_list):
#     size = len(some_list)
#     i = 0
#     main_str = ''
#     while i < size - 2:
#         main_str = main_str + str(some_list[i])+', '
#         i += 1
#     x = main_str + str(some_list[size - 2]) + ' and ' + str(some_list[size - 1])
#     print(x)
#
#
# spam = ['cat', 'bat', 'fat', 'mad', 'nad']
# list_to_str(spam)

############################ with join()
## i din`t like it. works bad with small lists

# list1 = ['g', 'e', 'e', 'k', 's']
# print("".join(list1))

# def list_to_str(any_list):
#     nums = len(any_list)
#     main_str = ''
#     for i in range(nums):
#         if i ==0:
#             main_str = main_str + ''.join(any_list[i])
#
#         elif i > 0 and i < nums-2:
#             main_str = main_str + ', ' + ''.join(any_list[i])
#
#         elif i == nums-2:
#             main_str = main_str + ', ' + ''.join(any_list[i]) + ' and '
#
#         elif i == nums-1:
#             main_str = main_str + ''.join(any_list[i])
#     print(main_str)
#
#
# spam = ['cat', 'bat', 'dad']
# list_to_str(spam)

# spam = ['cat', 'bat', 'fat', 'mad', 'nad']
# print(', '.join(spam))

###### someones good solution

spam= ['apples', 'bananas', 'tofu', 'cats']
def list_thing(list):
    new_string = ''
    for i in list:
        new_string = new_string + str(i)
        if list.index(i) == (len(list)-2):
            new_string = new_string + ', and '
        elif list.index(i) == (len(list)-1):
            new_string = new_string
        else:
            new_string = new_string + ', '
    return new_string

print (list_thing(spam))