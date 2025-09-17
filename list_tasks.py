from random import randint

# # 1. Напишите программу, которая создает список покупок. 
# # Программа должна запрашивать у пользователя элементы 
# # до тех пор, пока он не введет "стоп". 
# # После этого выведите итоговый список покупок.

# def shop_market(tovars):
#     while True:
#         element = input('Введите любой товар: ')
#         if element == 'стоп':
#             break
        
#         tovars.append(element)

# def main():
#     tovar = []
#     shop_market(tovar)
#     print(tovar)

# main()

# Создайте список `students` и добавьте в него имена студентов, 
# вводимые пользователем. Когда пользователь введет "конец", 
# программа должна вывести список всех студентов.


# def names_students(stud_name):
#     while True:
#         name = input('Введите имя студента: ')
#         if name == 'конец':
#             break

#         stud_name.append(name)




# def main():
#     students = []
#     names_students(students)
#     print(students)

# main()

# 3. Напишите программу, которая создает список из 10 случайных чисел, 
# добавляя каждое число к списку по одному.

# def rand_numbers(list_num):
#     for i in range(10):
#         list_num.append(randint(-10,10))


# def main():
#     numbers = []
#     rand_numbers(numbers)
#     print(rand_numbers)

# main()

# Напишите программу, которая объединяет списки сотрудников 
# из двух отделов `department1` и `department2` в один общий список `all_employees`.

# def ext_lists(list1, list2):
#     list1.extend(list2)
#     return list1


# def main():
#     department1 = ['fsdf', 'dsfds']
#     department2 = ['fsadasddasf', 'dsfahtgrfhsdds']
#     res = ext_lists(department1, department2)
#     print(res)

# main()


# Создайте список из месяцев года. Пользователь вводит имена 
# дополнительных месяцев (например, для особых календарей), 
# и программа добавляет их к списку.



# def months(list_month):
#     for i in range(12):
#         element = input('Введите месяц: ')
#         list_month.append(element)
#     return list_month

# def main():
#     months_list = []
#     res = months(months_list)
#     print(res)

# main()

# У вас есть список чисел `a = [1, 2, 3]` и список чисел `b = [4, 5, 6]`.
# Создайте программу, которая объединяет эти два списка и выводит результат.

# def ext_lists(list1, list2):
#     list1.extend(list2)
#     return list1


# def main():
#     a = [1, 2, 3]
#     b = [4, 5, 6]
#     res = ext_lists(a, b)
#     print(res)

# main()



# Создайте список из пяти элементов. Программа должна запрашивать 
# у пользователя новое значение и индекс, на который нужно 
# вставить это значение. После вставки элемент выводится обновленный список.


# def insert_lists(list1):
#     ind = int(input('Введите индекс '))
#     num = int(input('Введите значение '))
#     list1.insert(ind, num)
#     return list1


# def main():
#     a = [1, 2, 3]
#     res = insert_lists(a)
#     print(res)

# main()


# У вас есть список задач на день. 
# Напишите программу, которая добавляет новую задачу в начало списка, 
# если она имеет высокий приоритет.

# def insert_lists(list1):
#     ind = int(input('Введите приоритет задачи (0 - высокий приоритет/ иначе в конец списка) '))
#     tasks = input('Введите новую задачу ')
#     if ind == 0:
#         list1.insert(ind, tasks)
#     else:
#         list1.append(tasks)

#     return list1


# def main():
#     a = ['Тренировка', 'Учеба']
#     res = insert_lists(a)
#     print(res)

# main()

# В программе, работающей с расписанием занятий, 
# необходимо вставить новое занятие на указанное пользователем место в списке.

# def insert_lists(list1):
#     ind = int(input('Введите индекс '))
#     task = (input('Введите занятие '))
#     list1.insert(ind, task)
#     return list1


# def main():
#     a = ['Сходить в магазин', 'Прогулка с собакой']
#     res = insert_lists(a)
#     print(res)

# main()


# Напишите программу, которая создает список из десяти элементов. 
# Программа должна запрашивать у пользователя элемент для удаления и удалять его из списка, 
# если он существует. Если элемента нет в списке, выводится сообщение об этом.
