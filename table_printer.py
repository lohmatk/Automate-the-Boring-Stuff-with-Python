"""версия где я наебался с условием задачи и вывел таблицу такую же как выглядит список списков,
а надо бы перевернуть"""

# tableData = [['apples', 'oranges', 'cherries', 'banans'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
#
# def table_printer(datalist):
#     m_list = []
#     for k in range(len(datalist[0])):
#         list_val = []
#         for i in range(len(datalist)):
#             list_val.append(len(tableData[i][k]))
#         m = max(list_val)
#         print(m)
#         m_list.append(m)
#     print(m_list)
#
#     for h in range(len(datalist)):
#         for t in range(len(datalist[0])):
#             print(datalist[h][t].rjust(m_list[t]), end='   ')
#         print('\n')
#
#
# table_printer(tableData)

"""поправил код просто поеняв местами переменные в цикле"""
#
tableData = [['apples', 'oranges', 'cherries', 'banans'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def table_printer(datalist):
    m_list = []
    for k in range(len(datalist)):
        list_val = []
        for i in range(len(datalist[0])):
            list_val.append(len(tableData[k][i]))
        m = max(list_val)
        m_list.append(m) # сложил максимальные значения в список и распечатал его просто так
    print(m_list)

    for h in range(len(datalist[0])):
        for t in range(len(datalist)):
            print(datalist[t][h].rjust(m_list[t]), end=' ')
        print()


table_printer(tableData)
