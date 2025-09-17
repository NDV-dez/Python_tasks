# # 11.15. Дан массив. Составить программу: 
# #            а) расчета квадратного корня из любого элемента массива; 
# #            б) расчета среднего арифметического двух любых элементов массива. 

from random import randint
from math import sqrt

# lst = []

# def input_lst():
#     size = int(input('Введите сколько элементов массива вы хотите: '))

#     for _ in range(size):
#         lst.append(randint(-100,100))

# def output_lst():
#     bar = '=' * len(lst)
#     print('ВАШ СПИСОК')
#     print(f'{bar}\n{lst}\n{bar}')

# def calculate_el_lst():
#     element = int(input('Введите какой элемент из массива вы хотите sqrt: '))
#     output_lst()

#     if element not in lst:
#         print(f'Элемента {element} в списке нет')
#         return 
#     if element < 0:
#         print(f'Элемент {element} отрицательный')
#         return 
    
#     return (element, sqrt(element))
    
# def average_calculate_element():
#     element1, element2 = int(input('Введите какой элемент из массива вы хотите: ')), int(input('Введите какой элемент из массива вы хотите: '))

#     if element1 not in lst or element2 not in lst:
#         print(f'Одного из введенных элементов не существует')
#         return
    
#     return (element1+element2)/2

# def average_calculate_element_v2():
#     output_lst()

#     elements = []
#     while True:
#         element = input('Введите элемент из массива или стоп: ')
#         if element == 'стоп':
#             break
#         element = int(element)
#         if element not in lst:
#             continue
#         elements.append(element)
    
#     average = sum(elements) / len(elements)
#     return average

# def main():
#     input_lst()
#     output_lst()
#     res_a = calculate_el_lst()
#     if res_a:
#         print(f'Квадратный корень из элемента {res_a[0]} = {res_a[1]}')

#     res_b = average_calculate_element()
#     print(f'Среденее арифметическое = {res_b}')
#     res_b2 = average_calculate_element_v2()
#     print(res_b2)

# main()


# 11.17. Дан массив. Все его элементы: 
#            а) увеличить в 2 раза; 
#            в) разделить на первый элемент. 


# lst = []

# def input_lst():
#     size = int(input('Введите сколько элементов массива вы хотите: '))

#     for _ in range(size):
#         lst.append(randint(-100,100))

# def all_lst_multiply_on_2():
#     print(f'Ваш список {lst}')
#     # Вариант 1)
#     lst_result = []
#     for elem in lst:
#         lst_result.append(elem * 2)
#     # Вариант 2)
#     lst_copy = lst.copy()
#     for i in range(len(lst_copy)):
#         lst_copy[i] *= 2

#     print(f'Первый вариант: {lst_result}')
#     print(f'Второй вариант: {lst_copy}')

# def div_elem():
#     lst_copy = lst.copy()
#     first_el = lst_copy[0]
#     for i in range(len(lst_copy)):
#         lst_copy[i] /= first_el
#     print(f'Список после деления на первый элемент = {lst_copy}')

# def main():
#     input_lst()
#     all_lst_multiply_on_2()
#     div_elem()
# main() 



# 11.19. Определить: 
#     д) сумму элементов массива с k1-го по k2-й (значения k1 и k2 вводятся с клавиатуры; k2 > k1); 


# lst = []

# def input_lst():
#     size = int(input('Введите сколько элементов массива вы хотите: '))

#     for _ in range(size):
#         lst.append(randint(-100,100))

# def output_lst():
#     bar = '=' * len(lst)
#     print('ВАШ СПИСОК')
#     print(f'{bar}\n{lst}\n{bar}')

# def calculate_slice_lst():
#     output_lst()
#     k1 = int(input('Введите номер первого элемента: '))
#     k2 = int(input('Введите номер первого элемента: '))

#     if k2 < k1:
#         return
#     summ = 0
#     for i in range(k1-1,k2):
#         summ += lst[i]

#     print(f'Cумма элементов массива с k1-го по k2-й = {summ}')

# def main():
#     input_lst()
#     calculate_slice_lst()

# main()

# 11.16. Дан массив целых чисел. Выяснить: 
#            а) является ли s-й элемент массива положительным числом; 
#            б) является ли k-й элемент массива четным числом; 


# lst = []

# def input_lst():
#     size = int(input('Введите сколько элементов массива вы хотите: '))

#     for _ in range(size):
#         lst.append(randint(-100,100))

# def output_lst():
#     bar = '=' * len(lst)
#     print('ВАШ СПИСОК')
#     print(f'{bar}\n{lst}\n{bar}')

# def check_el_positiv():
#     element = int(input('Введите элемент массива для проверки знака: '))
#     if lst[element-1] < 0:
#         print(f'Элемент {element} - отрицательный')
#     print(f'Элемент {element} - положительный')
    
# def check_num_chetn():
#     element = int(input('Введите элемент массиватдля проверки четности: '))
#     if lst[element-1] % 2 != 0:
#         print(f'Элемент {element} - нечетный')
#     print(f'Элемент {element} - четный')


# def main():
#     input_lst()
#     output_lst()
#     check_el_positiv()
#     check_num_chetn()

# main()

# 11.36. Дан массив. Напечатать: 
#           а) все неотрицательные элементы; 
#           б) все элементы, не превышающие число 100. 



# lst = []

# def input_lst():
#     size = int(input('Введите сколько элементов массива вы хотите: '))

#     for _ in range(size):
#         lst.append(randint(-100,100))

# def output_lst():
#     bar = '=' * len(lst)
#     print('ВАШ СПИСОК')
#     print(f'{bar}\n{lst}\n{bar}')

# def print_negativ_el():
#     for i in range(len(lst)):
#         if lst[i] < 0:
#             continue
#         else:
#             print(f'Все положительные числа массива: ')
#             print(lst[i])
    
# def check_num_hundred():
#     for i in range(len(lst)):
#         if lst[i] > 100:
#             continue
#         else:
#             print(f'Все числа массива до 100: ')
#             print(lst[i])

# def main():
#     input_lst()
#     output_lst()
#     print_negativ_el()
#     check_num_hundred()

# main()


# 11.37. Дан массив целых чисел. Напечатать: 
#           а) все четные элементы; 
#           б) все элементы, оканчивающиеся нулем. 

# lst = []

# def input_lst():
#     size = int(input('Введите сколько элементов массива вы хотите: '))

#     for _ in range(size):
#         lst.append(randint(-100,100))

# def output_lst():
#     bar = '=' * len(lst)
#     print('ВАШ СПИСОК')
#     print(f'{bar}\n{lst}\n{bar}')

# def check_num_chetn():
#     for i in range(len(lst)):
#         if lst[i] % 2 != 0:
#             print(f'Элемент {lst[i]} - нечетный')
#         else:
#             print(f'Элемент {lst[i]} - четный')

# def last_num_el_zero():
#     for i in range(len(lst)):
#         if lst[i] % 10 != 0:
#             continue
#         print(f'Элемент {lst[i]} - оканчивается 0')

# def main():
#     input_lst()
#     output_lst()
#     check_num_chetn()
#     last_num_el_zero()

# main()


# 11.38. Дан массив натуральных чисел. Напечатать: 
#           а) все элементы массива, являющиеся двузначными числами; 
#           б) все элементы массива, являющиеся трехзначными числами. 

# lst = []

# def input_lst():
#     size = int(input('Введите сколько элементов массива вы хотите: '))

#     for _ in range(size):
#         lst.append(randint(-200,200))

# def output_lst():
#     bar = '=' * len(lst)
#     print('ВАШ СПИСОК')
#     print(f'{bar}\n{lst}\n{bar}')

# def dvuznach():
#     for i in range(len(lst)):
#         if lst[i] > 0:
#             if lst[i] < 9 or lst[i] >= 100:
#                 continue
#             print(f'Элемент {lst[i]} является двузначным числом')

# def trehznach():
#     for i in range(len(lst)):
#         if lst[i] > 0:
#             if lst[i] < 99 or lst[i] >= 1000:
#                 continue
#             print(f'Элемент {lst[i]} является трехзначным числом')

# def main():
#     input_lst()
#     output_lst()
#     dvuznach()
#     trehznach()

# main()

# 11.39. Дан массив. Напечатать: 
#           а) второй, четвертый и т. д. элементы; 


# lst = []

# def input_lst():
#     size = int(input('Введите сколько элементов массива вы хотите: '))

#     for _ in range(size):
#         lst.append(randint(-200,200))

# def output_lst():
#     bar = '=' * len(lst)
#     print('ВАШ СПИСОК')
#     print(f'{bar}\n{lst}\n{bar}')

# def print_start_second_el():
#     for i in range(1, len(lst)):
#         print(lst[i])

# def main():
#     input_lst()
#     output_lst()
#     print_start_second_el()

# main()

# 11.41. Дан массив целых чисел. Вывести на экран сначала его четные элементы, затем нечетные. 

# lst = [12, 124, 412, 12, 5, 9, 76, 91]

# lst1 = []
# lst2 = []

# for el in lst:
#     if el % 2 == 0:
#         lst1.append(el)
#         continue
#     lst2.append(el)

# lst1.extend(lst2)
# print(lst1)

# 11.42. Дан массив целых чисел. 
# Найти номера элементов, оканчивающихся цифрой 0 
# (известно, что такие элементы в массиве есть). 

lst = [12, 124, 412, 12, 50, 9, 760, 91]

lst_num = []

for el in range(len(lst)):
    if lst[el] % 10 == 0:
        lst_num.append(el+1)

print(lst_num)





