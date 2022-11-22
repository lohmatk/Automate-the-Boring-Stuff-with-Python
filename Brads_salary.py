'''
Write a Python program to change Brad’s salary to 8500 in the following dictionary.
перестарался я. овет предполагался просто присвоить этому ключу новое значение...
Но я чето туплю как сделать в таком цикле чтобы при вводе несуществующего имени
выводилось какое-то сообщение незацикленно
'''

import pprint

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}


def change_slr(dict, who):
    for k in dict:
        if who == dict[k]['name']:
            print('How much he/she should be paid?')
            amount = input()
            dict[k]['salary'] = amount
            pprint.pprint(sample_dict)
        else:
            continue


print('Who should be paid different?\n')
name = input()
change_slr(sample_dict, name)

