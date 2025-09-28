from random import randint

# ======== append() ========
# 1) Напишите программу, которая создает список покупок. 
# Программа должна запрашивать у пользователя элементы 
# до тех пор, пока он не введет "стоп". 
# После этого выведите итоговый список покупок.

def shop_market(tovars):
    while True:
        element = input('Введите любой товар: ')
        if element == 'стоп':
            break
        tovars.append(element)

def main():
    tovar = []
    shop_market(tovar)
    print(tovar)

main()

# 2) Создайте список `students` и добавьте в него имена студентов, 
# вводимые пользователем. Когда пользователь введет "конец", 
# программа должна вывести список всех студентов.

def names_students(stud_name):
    while True:
        name = input('Введите имя студента: ')
        if name == 'конец':
            break
        stud_name.append(name)

def main():
    students = []
    names_students(students)
    print(students)

main()

# 3) Напишите программу, которая создает список из 10 случайных чисел, 
# добавляя каждое число к списку по одному.

def rand_numbers(list_num):
    for i in range(10):
        list_num.append(randint(-10,10))

def main():
    numbers = []
    rand_numbers(numbers)
    print(numbers)

main()

# ======== extend() ========
# 1) Напишите программу, которая объединяет списки сотрудников 
# из двух отделов `department1` и `department2` в один общий список `all_employees`.

def ext_lists(list1, list2):
    list1.extend(list2)
    return list1

def main():
    department1 = ['fsdf', 'dsfds']
    department2 = ['fsadasddasf', 'dsfahtgrfhsdds']
    res = ext_lists(department1, department2)
    print(res)

main()

# 2) Создайте список из месяцев года. Пользователь вводит имена 
# дополнительных месяцев (например, для особых календарей), 
# и программа добавляет их к списку.

def months(list_month):
    for i in range(12):
        element = input('Введите месяц: ')
        list_month.append(element)
    return list_month

def main():
    months_list = []
    res = months(months_list)
    print(res)

main()

# 3) У вас есть список чисел `a = [1, 2, 3]` и список чисел `b = [4, 5, 6]`.
# Создайте программу, которая объединяет эти два списка и выводит результат.

def ext_lists(list1, list2):
    list1.extend(list2)
    return list1

def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    res = ext_lists(a, b)
    print(res)

main()

# ======== insert() ========
# 1) Создайте список из пяти элементов. Программа должна запрашивать 
# у пользователя новое значение и индекс, на который нужно 
# вставить это значение. После вставки элемент выводится обновленный список.

def insert_lists(list1):
    ind = int(input('Введите индекс '))
    num = int(input('Введите значение '))
    list1.insert(ind, num)
    return list1

def main():
    a = [1, 2, 3]
    res = insert_lists(a)
    print(res)

main()

# 2) У вас есть список задач на день. 
# Напишите программу, которая добавляет новую задачу в начало списка, 
# если она имеет высокий приоритет.

def insert_lists(list1):
    ind = int(input('Введите приоритет задачи (0 - высокий приоритет/ иначе в конец списка) '))
    tasks = input('Введите новую задачу ')
    if ind == 0:
        list1.insert(ind, tasks)
    else:
        list1.append(tasks)

    return list1

def main():
    a = ['Тренировка', 'Учеба']
    res = insert_lists(a)
    print(res)

main()

# 3) В программе, работающей с расписанием занятий, 
# необходимо вставить новое занятие на указанное пользователем место в списке.

def insert_lists(list1):
    ind = int(input('Введите индекс '))
    task = (input('Введите занятие '))
    list1.insert(ind, task)
    return list1


def main():
    a = ['Сходить в магазин', 'Прогулка с собакой']
    res = insert_lists(a)
    print(res)

main()

# ======== revome() ========

# 1) Напишите программу, которая создает список из десяти элементов. 
# Программа должна запрашивать у пользователя элемент для удаления и удалять его из списка, 
# если он существует. Если элемента нет в списке, выводится сообщение об этом.


def remove_element(list1):
    element = int(input('Введите элемент для удаления '))
    if element in list1:
        list1.remove(element)
    else:
        print('Элемента нет в списке')
    return list1

def main():
    a = [randint(1,10) for _ in range(10)]
    print(a)
    res = remove_element(a)
    print(res)

main()

# 2) Создайте список из имен сотрудников. Напишите программу, 
# которая удаляет сотрудника по введенному пользователем имени.

def remove_element(list1):
    name = input('Введите имя сотрудника для удаления ')
    if name in list1:
        list1.remove(name)
    else:
        print('Такого сотрудника нет в списке')
    return list1

def main():
    a = ['Иванов', 'Петров', 'Сидоров']
    res = remove_element(a)
    print(res)

main()

# 3) Дан список `tasks = ["task1", "task2", "task3", "task4"]`. 
# Напишите программу, которая удаляет задачу, если пользователь пометил ее как выполненную.

def remove_element(list1):
    task = input('Введите выполненную задачу ')
    if task in list1:
        list1.remove(task)
    else:
        print('Такой задачи нет в списке')
    return list1

def main():
    tasks = ["task1", "task2", "task3", "task4"]
    res = remove_element(tasks)
    print(res)

main()


# ====== pop() ========

# 1) Напишите программу, которая создает список из пяти элементов 
# и предлагает пользователю удалить элемент по индексу. 
# Программа должна вывести удаленный элемент и обновленный список.

def pop_element(list1):
    ind = int(input('Введите индекс элемента для удаления '))
    if ind < len(list1):
        removed = list1.pop(ind)
        print(f'Удален элемент: {removed}')
    else:
        print('Индекс вне диапазона списка')
    return list1

def main():
    a = [randint(1,10) for _ in range(5)]
    print(a)
    res = pop_element(a)
    print(res)

main()

# 2) Создайте список из книг в очереди на чтение. 
# Напишите программу, которая удаляет последнюю книгу 
# из списка и выводит ее, предполагая, что пользователь закончил ее читать.

def pop_element(list1):
    if list1:
        removed = list1.pop()
        print(f'Вы закончили читать книгу: {removed}')
    else:
        print('Список книг пуст')
    return list1

def main():
    books = ['Book1', 'Book2', 'Book3']
    res = pop_element(books)
    print(res)

main()


# 3. У вас есть список продуктов в корзине. 
# Напишите программу, которая запрашивает у пользователя 
# индекс продукта для удаления, удаляет его и выводит обновленный список.

def pop_element(list1):
    ind = int(input('Введите индекс продукта для удаления '))
    if ind < len(list1):
        removed = list1.pop(ind)
        print(f'Удален продукт: {removed}')
    else:
        print('Индекс вне диапазона списка')
    return list1

def main():
    products = ['Milk', 'Bread', 'Eggs', 'Butter']
    print(products)
    res = pop_element(products)
    print(res)

main()

# ======= clear() ========

# 1. Создайте программу для ведения списка дел. 
# В конце дня программа должна очищать список для подготовки к новому дню.


# Вот эта задачка интересаная была! Решил сделать полноценную программу для списка дел.

def add_task(list1):
    while True:
        task = input('Введите задачу для добавления в список дел на сегодня (или "стоп" для завершения): ')
        if task.lower() == 'стоп':
            break
        list1.append(task)
    return list1

def view_tasks(list1):
    if list1:
        print('Список дел на сегодня:')
        for i, task in enumerate(list1, 1):
            print(f'{i}. {task}')
    else:
        print('Список дел пуст.')
    return list1

def remove_task(list1):
    view_tasks(list1)
    try:
        task = input('Введите задачу для удаления из списка дел на сегодня: ')
        if task in list1:
            list1.remove(task)
        else:
            print('Такой задачи нет в списке')
    except ValueError:
        print('Ошибка: Введите число.')
    return list1

def clear_list(list1):
    list1.clear()
    return list1

def main():
    tasks = []
    while True:
        action = input('Выберите действие: 1 - Добавить задачу, 2 - Просмотреть задачи, 3 - Удалить задачу, 4 - Очистить список, 5 - Выйти: ')
        if action == '1':
            add_task(tasks)
        elif action == '2':
            view_tasks(tasks)
        elif action == '3':
            remove_task(tasks)
        elif action == '4':
            clear_list(tasks)
            print('Список дел очищен.')
        elif action == '5':
            print('Выход из программы.')
            break
        else:
            print('Неверный выбор. Пожалуйста, выберите действие от 1 до 5.')

main()

# 2. Напишите программу, которая позволяет пользователю 
# добавлять элементы в список, а затем, по запросу, очищает весь список.

def add_elements(list1):
    while True:
        element = input('Введите задачу для добавления в список дел (или "стоп" для завершения): ')
        if element.lower() == 'стоп':
            break
        list1.append(element)
    return list1

def clear_list(list1):
    list1.clear()
    return list1

def main():
    elements = []
    add_elements(elements)
    print(f'Текущий список: {elements}')
    clear = input('Хотите очистить список? (да/нет): ')
    if clear.lower() == 'да':
        clear_list(elements)
        print('Список очищен.')
    else:
        print('Список не был очищен.')
    print(f'Итоговый список: {elements}')

main()

# 3. У вас есть список временных данных, которые 
# нужно сбрасывать после обработки. Напишите 
# программу, которая очищает список после каждой обработки.

# Возможно не совсем так понял задание, но попытался сымитировать процесс обработки данных.

def process_data(list1):
    if not list1:
        print('Список пуст, нечего обрабатывать.')
        return list1

    print('Обработка данных:')
    for item in list1:
        print(f'Обрабатывается: {item}')
    
    list1.clear()
    print('Список очищен после обработки.')
    return list1

def main():
    data = ['data1', 'data2', 'data3']
    print(f'Исходный список: {data}')
    process_data(data)
    print(f'Текущий список после обработки: {data}')

main()

#  ===== index() ======

# 1. Напишите программу, которая запрашивает у 
# пользователя список студентов и имя студента. 
# Программа должна вывести индекс данного студента в списке.

def find_student_index(students, name):
    try:
        index = students.index(name)
        return index
    except ValueError:
        return -1
    
def main():
    students = ['Иванов', 'Петров', 'Сидоров']
    name = input('Введите имя студента для поиска: ')
    index = find_student_index(students, name)
    if index != -1:
        print(f'Студент {name} найден на индексе {index}.')
    else:
        print(f'Студент {name} не найден в списке.')

main()

# 2. Создайте программу, которая находит индекс 
# первого вхождения заданного числа в списке чисел.

def find_number_index(numbers, num):
    try:
        index = numbers.index(num)
        return index
    except ValueError:
        return -1
    
def main():
    numbers = [randint(1, 10) for _ in range(10)]
    print(f'Список чисел: {numbers}')
    num = int(input('Введите число для поиска его индекса: '))
    index = find_number_index(numbers, num)
    if index != -1:
        print(f'Число {num} найдено на индексе {index}.')
    else:
        print(f'Число {num} не найдено в списке.')

main()

# 3. У вас есть список слов. Напишите программу, 
# которая запрашивает слово и выводит его индекс в списке, если оно существует.

def find_word_index(words, word):
    try:
        index = words.index(word)
        return index
    except ValueError:
        return -1
    
def main():
    words = ['apple', 'banana', 'cherry', 'orange']
    print(f'Список слов: {words}')
    word = input('Введите слово для поиска его индекса: ')
    index = find_word_index(words, word)
    if index != -1:
        print(f'Слово "{word}" найдено на индексе {index}.')
    else:
        print(f'Слово "{word}" не найдено в списке.')

main()

# ===== count() =====

# 1. Напишите программу, которая создает список из случайных чисел. 
# Программа должна запрашивать у пользователя число и выводить количество его вхождений в списке.

def count_occurrences(numbers, num):
    count = numbers.count(num)
    return count

def main():
    numbers = [randint(1, 10) for _ in range(20)]
    print(f'Список чисел: {numbers}')
    num = int(input('Введите число для подсчета его вхождений: '))
    count = count_occurrences(numbers, num)
    print(f'Число {num} встречается {count} раз(а) в списке.')

main()

# 2. Создайте программу, которая подсчитывает, 
# сколько раз определенное имя встречается в списке имен.

def count_name_occurrences(names, name):
    count = names.count(name)
    return count

def main():
    names = ['Иван', 'Петр', 'Сидор', 'Иван', 'Мария', 'Иван']
    print(f'Список имен: {names}')
    name = input('Введите имя для подсчета его вхождений: ')
    count = count_name_occurrences(names, name)
    print(f'Имя "{name}" встречается {count} раз(а) в списке.')

main()

# 3. У вас есть список покупок. Напишите программу, 
# которая подсчитывает, сколько раз каждый продукт встречается в списке.

def count_product_occurrences(products):
    product_count = {}
    for product in products:
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1
    return product_count

def main():
    products = ['яблоко', 'банан', 'яблоко', 'апельсин', 'банан', 'яблоко']
    print(f'Список продуктов: {products}')
    product_count = count_product_occurrences(products)
    for product, count in product_count.items():
        print(f'Продукт "{product}" встречается {count} раз(а) в списке.')

main()


#  ====== sort() =======
# 1. Напишите программу, которая создает список студентов и их оценок. 
# Программа должна сортировать список студентов по оценкам в порядке убывания.

def sort_students_by_grades(students):
    students.sort(key = lambda x: x[1],reverse=True)
    return students

def main():
    students = [('Иванов', 85), ('Петров', 92), ('Сидоров', 78), ('Мария', 95)]
    print(f'Исходный список студентов и их оценок: {students}')
    sorted_students = sort_students_by_grades(students)
    print(f'Отсортированный список студентов по оценкам (по убыванию): {sorted_students}')

main()

# 2. У вас есть список дат. Напишите программу, 
# которая сортирует эти даты в порядке возрастания.

def sort_dates(dates):
    dates.sort()
    return dates

def main():
    dates = ['2023-12-01', '2022-05-15', '2024-01-20', '2021-11-30']
    print(f'Исходный список дат: {dates}')
    sorted_dates = sort_dates(dates)
    print(f'Отсортированный список дат (по возрастанию): {sorted_dates}')

main()

# 3. Создайте список имен сотрудников. Напишите программу, 
# которая сортирует список в алфавитном порядке.

def sort_names(names):
    names.sort()
    return names

def main():
    names = ['Иванов', 'Петров', 'Сидоров', 'Мария']
    print(f'Исходный список имен сотрудников: {names}')
    sorted_names = sort_names(names)
    print(f'Отсортированный список имен сотрудников (в алфавитном порядке): {sorted_names}')

main()

# ====== reverse() ======
# 1. Напишите программу, которая создает 
# список из пяти чисел и выводит их в обратном порядке.

def reverse_list(numbers):
    numbers.reverse()
    return numbers

def main():
    numbers = [randint(1, 100) for _ in range(5)]
    print(f'Исходный список чисел: {numbers}')
    reversed_numbers = reverse_list(numbers)
    print(f'Список чисел в обратном порядке: {reversed_numbers}')

main()

# 2. У вас есть список из пяти строк. 
# Напишите программу, которая переворачивает этот список.

def reverse_list(strings):
    strings.reverse()
    return strings

def main():
    strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(f'Исходный список строк: {strings}')
    reversed_strings = reverse_list(strings)
    print(f'Список строк в обратном порядке: {reversed_strings}')

main()

# 3. Создайте список задач на день. Напишите программу, 
# которая выводит эти задачи в обратном порядке их добавления.

def reverse_list(tasks):
    tasks.reverse()
    return tasks

def main():
    tasks = ['Сходить в магазин', 'Позвонить маме', 'Закончить проект', 'Прогуляться', 'Прочитать книгу']
    print(f'Исходный список задач на день: {tasks}')
    reversed_tasks = reverse_list(tasks)
    print(f'Список задач в обратном порядке: {reversed_tasks}')

main()

# ===== copy() ======

# 1. Напишите программу, которая создает список из пяти элементов 
# и делает его копию. Измените оригинальный список 
# и выведите оба списка, чтобы показать, что они разные.

def copy_list(original):
    copied = original.copy()
    return copied

def main():
    original = [randint(1, 100) for _ in range(5)]
    print(f'Оригинальный список: {original}')
    copied = copy_list(original)
    original.append(999) 
    print(f'Измененный оригинальный список: {original}')
    print(f'Копия списка: {copied}')

main()

# 2. Создайте список сотрудников и сделайте его копию. 
# Добавьте нового сотрудника в оригинальный список 
# и покажите, что копия осталась без изменений.

def copy_list(original):
    copied = original.copy()
    return copied


def main():    
    employees = ['Иванов', 'Петров', 'Сидоров']
    print(f'Оригинальный список сотрудников: {employees}')
    copied = copy_list(employees)
    employees.append('Мария')
    print(f'Измененный оригинальный список сотрудников: {employees}')
    print(f'Копия списка сотрудников: {copied}')

main()


# 3. У вас есть список продуктов. Напишите программу, 
# которая создает копию этого списка, удаляет все 
# элементы из оригинала и показывает, что копия осталась без изменений.

def copy_list(original):
    copied = original.copy()
    return copied

def main():    
    products = ['яблоко', 'банан', 'апельсин']
    print(f'Оригинальный список продуктов: {products}')
    copied = copy_list(products)
    products.clear()
    print(f'Очищенный оригинальный список продуктов: {products}')
    print(f'Копия списка продуктов: {copied}')

main()


# ====== __len__() / len() ======

# 1. Напишите программу, которая создает список покупок. 
# Программа должна запрашивать у пользователя элементы до тех пор, 
# пока он не введет "стоп". Затем программа выводит количество элементов в списке.

def shopping_list():
    tovars = []
    while True:
        element = input('Введите любой товар (или "стоп" для завершения): ')
        if element.lower() == 'стоп':
            break
        tovars.append(element)
    return tovars

def main():
    tovars = shopping_list()
    print(f'Количество товаров в списке: {len(tovars)}')
    print(f'Список товаров: {tovars}')

main()

# 2. Создайте список задач на неделю. 
# Напишите программу, которая выводит количество задач на каждый день.

def tasks_per_day():
    week_tasks = {}
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    
    for day in days:
        tasks = []
        print(f'Введите задачи для {day} (или "стоп" для завершения):')
        while True:
            task = input()
            if task.lower() == 'стоп':
                break
            tasks.append(task)
        week_tasks[day] = tasks
    
    return week_tasks

def main():
    week_tasks = tasks_per_day()
    for day, tasks in week_tasks.items():
        print(f'{day}: {len(tasks)} задача(и)')
main()


# 3. У вас есть список студентов. Напишите программу, 
# которая выводит количество студентов в этом списке.

def main():
    students = ['Иванов', 'Петров', 'Сидоров', 'Мария']
    print(f'Количество студентов в списке: {len(students)}')
    print(f'Список студентов: {students}')  

main()

# ====== __delitem__() / del() ======

# 1. Напишите программу, которая создает список из пяти элементов. 
# Программа должна запрашивать у пользователя индекс для удаления элемента и удалять его.

def remove_element_by_index(list1):
    ind = int(input('Введите индекс элемента для удаления '))
    if 0 <= ind < len(list1):
        del list1[ind]
    else:
        print('Индекс вне диапазона списка')
    return list1

def main():
    a = [randint(1,10) for _ in range(5)]
    print(a)
    res = remove_element_by_index(a)
    print(res)

main()

# 2. Создайте список продуктов. Напишите программу, 
# которая удаляет элемент из списка по заданному пользователем индексу.

def remove_element_by_index(list1):
    ind = int(input('Введите индекс продукта для удаления '))
    if 0 <= ind < len(list1):
        del list1[ind]
    else:
        print('Индекс вне диапазона списка')
    return list1

def main():
    products = ['Milk', 'Bread', 'Eggs', 'Butter']
    print(products)
    res = remove_element_by_index(products)
    print(res)

main()


# 3. У вас есть список задач. Напишите программу, 
# которая удаляет задачу по ее индексу, запрашиваемому у пользователя.

def remove_task_by_index(tasks):
    ind = int(input('Введите индекс задачи для удаления '))
    if 0 <= ind < len(tasks):
        del tasks[ind]
    else:
        print('Индекс вне диапазона списка')
    return tasks

def main():
    tasks = ['Сходить в магазин', 'Позвонить маме', 'Закончить проект', 'Прогуляться', 'Прочитать книгу']
    print(tasks)
    res = remove_task_by_index(tasks)
    print(res)

main()

# ====== __contains__() / in ======

# 1. Напишите программу, которая создает список из пяти элементов и 
# запрашивает у пользователя значение. Программа должна проверять, есть ли это значение в списке.

def check_value_in_list(list1):
    value = int(input('Введите значение для проверки его наличия в списке: '))
    if value in list1:
        print(f'Значение "{value}" найдено в списке.')
    else:
        print(f'Значение "{value}" не найдено в списке.')
    return list1

def main():
    a = [randint(1,10) for _ in range(5)]
    print(a)
    res = check_value_in_list(a)
    print(res)

main()

# 2. Создайте список книг. Напишите программу, 
# которая проверяет, есть ли определенная книга в списке.

def check_book_in_list(books):
    book = input('Введите название книги для проверки ее наличия в списке: ')
    if book in books:
        print(f'Книга "{book}" найдена в списке.')
    else:
        print(f'Книга "{book}" не найдена в списке.')
    return books

def main():
    books = ['Война и мир', 'Преступление и наказание', 'Мастер и Маргарита']
    print(books)
    res = check_book_in_list(books)
    print(res)

main()

# 3. У вас есть список имен сотрудников. Напишите программу, 
# которая проверяет, есть ли определенное имя в списке.

def check_employee_in_list(employees):
    name = input('Введите имя сотрудника для проверки его наличия в списке: ')
    if name in employees:
        print(f'Сотрудник "{name}" найден в списке.')
    else:
        print(f'Сотрудник "{name}" не найден в списке.')
    return employees

def main():
    employees = ['Иванов', 'Петров', 'Сидоров', 'Мария']
    print(employees)
    res = check_employee_in_list(employees)
    print(res)

main()

# ===== map() =====
# 1. Напишите программу, которая создает список чисел 
# и использует функцию `map` для удвоения каждого элемента списка.

def double(x):
    return x * 2

def main():
    numbers = [randint(1, 10) for _ in range(5)]
    print(f'Исходный список чисел: {numbers}')
    doubled_numbers = list(map(double, numbers))
    print(f'Список чисел после удвоения: {doubled_numbers}')

# main()

# 2. Создайте список строк. Напишите программу, которая 
# использует функцию `map` для приведения всех строк к верхнему регистру.

def to_upper(s):
    return s.upper()

def main():
    strings = ['apple', 'banana', 'cherry']
    print(f'Исходный список строк: {strings}')
    upper_strings = list(map(to_upper, strings))
    print(f'Список строк в верхнем регистре: {upper_strings}')

main()  

# 3. У вас есть список температур в Цельсиях. Напишите программу, 
# которая использует функцию `map` для перевода их в Фаренгейты.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def main():
    celsius_temps = [0, 20, 37, 100]
    print(f'Температуры в Цельсиях: {celsius_temps}')
    fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
    print(f'Температуры в Фаренгейтах: {fahrenheit_temps}')

main()


# ===== filter() =====
# 1. Напишите программу, которая создает список чисел и 
# использует функцию `filter` для получения только четных чисел.


def is_even(n):
    return n % 2 == 0  

def main():
    numbers = [randint(1, 20) for _ in range(10)]
    print(f'Исходный список чисел: {numbers}')
    even_numbers = list(filter(is_even, numbers))
    print(f'Список четных чисел: {even_numbers}')   

main()

# 2. Создайте список строк. Напишите программу, которая 
# использует функцию `filter` для отбора строк длиной более 5 символов.

def is_longer_than_five(s):
    return len(s) > 5

def main():
    strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(f'Исходный список строк: {strings}')
    long_strings = list(filter(is_longer_than_five, strings))
    print(f'Список строк длиной более 5 символов: {long_strings}')

main()

# 3. У вас есть список сотрудников с указанием их возраста. 
# Напишите программу, которая использует функцию `filter` для отбора сотрудников старше 30 лет.

def is_older_than_thirty(employee):
    return employee['age'] > 30

def main():
    employees = [
        {'name': 'Иванов', 'age': 28},
        {'name': 'Петров', 'age': 35},
        {'name': 'Сидоров', 'age': 40},
        {'name': 'Мария', 'age': 22}
    ]
    print(f'Исходный список сотрудников: {employees}')
    older_employees = list(filter(is_older_than_thirty, employees))
    print(f'Список сотрудников старше 30 лет: {older_employees}')

main()

#  ====== enumerate() ======
# 1. Напишите программу, которая создает список 
# студентов и выводит каждого студента вместе с его номером по порядку

def list_students_with_indices(students):
    for index, student in enumerate(students, start=1):
        print(f'{index}. {student}')

def main():
    students = ['Иванов', 'Петров', 'Сидоров', 'Мария']
    list_students_with_indices(students)

main()


# 2. Создайте список задач на день. 
# Напишите программу, которая выводит каждую задачу с ее индексом в списке.

def list_tasks_with_indices(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')

def main():
    tasks = ['Сходить в магазин', 'Позвонить маме', 'Закончить проект', 'Прогуляться', 'Прочитать книгу']
    list_tasks_with_indices(tasks)

main()


# 3. У вас есть список покупок. Напишите программу, 
# которая выводит каждый продукт и его позицию в списке.

def list_products_with_indices(products):
    for index, product in enumerate(products, start=1):
        print(f'{index}. {product}')

def main():
    products = ['яблоко', 'банан', 'апельсин', 'груша']
    list_products_with_indices(products)

main()

#  ====== zip() ======
# 1. Напишите программу, которая объединяет два списка 
# имен и возрастов в один список кортежей (имя, возраст)

def combine_names_and_ages(names, ages):
    return list(zip(names, ages))

def main():
    names = ['Иван', 'Петр', 'Сидор']
    ages = [25, 30, 22]
    combined = combine_names_and_ages(names, ages)
    print(f'Список кортежей (имя, возраст): {combined}')

main()

# 2. Создайте два списка: один с названиями продуктов, другой с их ценами. 
# Напишите программу, которая создает список кортежей (продукт, цена).

def combine_products_and_prices(products, prices):
    return list(zip(products, prices))

def main():
    products = ['яблоко', 'банан', 'апельсин']
    prices = [50, 30, 40]
    combined = combine_products_and_prices(products, prices)
    print(f'Список кортежей (продукт, цена): {combined}')

main()

# 3. У вас есть два списка: первый — названия книг, второй — авторы. 
# Напишите программу, которая создает список кортежей (название книги, автор).


def combine_books_and_authors(books, authors):
    return list(zip(books, authors))

def main():
    books = ['Война и мир', 'Преступление и наказание', 'Мастер и Маргарита']
    authors = ['Лев Толстой', 'Федор Достоевский', 'Михаил Булгаков']
    combined = combine_books_and_authors(books, authors)
    print(f'Список кортежей (название книги, автор): {combined}')

main()

#  ====== reversed() ======
# 1. Напишите программу, которая создает список из пяти элементов и 
# выводит их в обратном порядке с помощью функции `reversed()` 

def reverse_list(lst):
    return list(reversed(lst))

def main():
    a = [randint(1, 100) for _ in range(5)]
    print(f'Исходный список: {a}')
    reversed_a = reverse_list(a)
    print(f'Список в обратном порядке: {reversed_a}')

main()


# 2. Создайте список дат. Напишите программу, 
# которая выводит их в обратном порядке.


def reverse_dates(dates):
    return list(reversed(dates))

def main():
    dates = ['2023-12-01', '2022-05-15', '2024-01-20', '2021-11-30']
    print(f'Исходный список дат: {dates}')
    reversed_dates = reverse_dates(dates)
    print(f'Список дат в обратном порядке: {reversed_dates}')

main()


# 3. У вас есть список строк. Напишите программу, которая 
# переворачивает этот список с использованием функции `reversed()`.

def reverse_strings(strings):
    return list(reversed(strings))

def main():
    strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(f'Исходный список строк: {strings}')
    reversed_strings = reverse_strings(strings)
    print(f'Список строк в обратном порядке: {reversed_strings}')

main()


# ========== на различие между reversed() и reverse() ============

# 1. Напишите программу, которая демонстрирует разницу между методами `reverse()` и `reversed()` 
# на одном и том же списке, показывая как изменяется сам список и его итерация в обратном порядке. 

def demonstrate_reverse_methods(lst):
    print(f'Исходный список: {lst}')
 
    lst.reverse()
    print(f'Исходный список после метода reverse() изменился: {lst}')

    print('Итерация по списку после reverse():')
    for item in lst:
        print(item, end=' ')
    print()
    
    reversed_lst = list(reversed(lst))
    print(f'Исходный список после функции reversed(): {reversed_lst}')
    
    print('Итерация по списку после reversed():')
    for item in reversed_lst:
        print(item, end=' ')
    print()
    
    return lst, reversed_lst

def main():
    a = [randint(1, 100) for _ in range(5)]
    demonstrate_reverse_methods(a)

main()




# 2. Создайте список чисел. Используйте сначала `reverse()`, чтобы изменить порядок элементов, затем `reversed()`, 
# чтобы вывести их в обратном порядке без изменения самого списка.

# Странная задача, точно такая же по сути как и предыдущая.

def demonstrate_reverse_methods(lst):
    print(f'Исходный список: {lst}')
 
    lst.reverse()
    print(f'Исходный список после метода reverse() изменился: {lst}')

    print('Итерация по списку после reverse():')
    for item in lst:
        print(item, end=' ')
    print()
    
    reversed_lst = list(reversed(lst))
    print(f'Исходный список после функции reversed(): {reversed_lst}')
    
    print('Итерация по списку после reversed():')
    for item in reversed_lst:
        print(item, end=' ')
    print()
    
    return lst, reversed_lst

def main():
    a = [randint(1, 100) for _ in range(5)]
    demonstrate_reverse_methods(a)

main()

# 3. У вас есть список строк. Напишите программу, которая использует `reverse()` 
# для изменения порядка списка и `reversed()` 
# для создания итератора, который будет перебирать элементы списка в обратном порядке.

def demonstrate_reverse_methods(lst):
    print(f'Исходный список: {lst}')
 
    lst.reverse()
    print(f'Исходный список после метода reverse() изменился: {lst}')

    print('Итерация по списку после reverse():')
    for item in lst:
        print(item, end=' ')
    print()
    
    reversed_lst = list(reversed(lst))
    print(f'Исходный список после функции reversed(): {reversed_lst}')
    
    print('Итерация по списку после reversed():')
    for item in reversed_lst:
        print(item, end=' ')
    print()
    
    return lst, reversed_lst

def main():
    strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    demonstrate_reverse_methods(strings)

main()

#  ======== any() и all() =========
# 1. Напишите программу, которая проверяет, 
# есть ли в списке чисел хотя бы одно положительное число.

def has_positive_number(numbers):
    return any(n > 0 for n in numbers)

def main():
    numbers = [randint(-10, 10) for _ in range(3)]
    print(f'Список чисел: {numbers}')
    if has_positive_number(numbers):
        print('В списке есть хотя бы одно положительное число.')
    else:
        print('В списке нет положительных чисел.')

main()

# 2. Создайте список логических значений (True/False). 
# Напишите программу, которая проверяет, все ли значения в списке True.

def all_true(values):
    return all(values)

def main():
    values = [True, True, False, True]
    print(f'Список логических значений: {values}')
    if all_true(values):
        print('Все значения в списке True.')
    else:
        print('Не все значения в списке True.')

main()  

# 3. У вас есть список слов. Напишите программу, 
# которая проверяет, все ли слова в списке начинаются с буквы "a".

def all_start_with_a(words):
    return all(word.lower().startswith('a') for word in words)

def main():
    words = ['apple', 'banana', 'avocado', 'apricot']
    print(f'Список слов: {words}')
    if all_start_with_a(words):
        print('Все слова в списке начинаются с буквы "a".')
    else:
        print('Не все слова в списке начинаются с буквы "a".')

main()