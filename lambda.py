# Попробовать решить задачи включениями и lambda-функциями (ЕСЛИ ЭТО ВОЗМОЖНО).
# 1. Создайте список всех чисел от 1 до 30 включительно, которые делятся на 3.

numbers_div_by_3 = list(filter(lambda x: x % 3 == 0, range(1, 31)))
print(f'Числа от 1 до 30, делящиеся на 3: {numbers_div_by_3}')
# 2. Создайте список цифр числа 12345.

numbers_in_12345 = list(map(int, str(12345)))
print(f'Цифры числа 12345: {numbers_in_12345}')

# 3. Создайте список сумм цифр чисел от 10 до 20 включительно.

list_of_sums = list(map(lambda x: sum(int(digit) for digit in str(x)), range(10, 21)))
print(f'Суммы цифр чисел от 10 до 20: {list_of_sums}')

# 4. Создайте список всех чисел от 1 до 50 включительно, которые
# содержат цифру 3. (‘3’ in str(13) подсказка интересного решения)

list_with_3 = list(filter(lambda x: '3' in str(x), range(1, 51)))
print(f'Числа от 1 до 50, содержащие цифру 3: {list_with_3}')

# 5. Создайте список кортежей, где каждый кортеж состоит из числа от 1
# до 10 включительно и его квадрата.

list_of_tuples = list(map(lambda x: (x, x**2), range(1, 11)))
print(f'Кортежи чисел от 1 до 10 и их квадратов: {list_of_tuples}')

# 6. Напишите lambda-функцию, которая принимает два числа и
# возвращает их произведение.

multiply = lambda x, y: x * y
print(f'Произведение 6 и 7: {multiply(6, 7)}')

# 7. Напишите lambda-функцию, которая принимает три числа и
# возвращает их сумму.

sum_three = lambda x, y, z: x + y + z
print(f'Сумма 1, 2 и 3: {sum_three(1, 2, 3)}')

# 8. Напишите lambda-функцию, которая принимает два логических
# значения и возвращает их логическое И.

logical_and = lambda a, b: a and b
print(f'Логическое И для True и False: {logical_and(True, False)}')

# 9. Используйте lambda и функцию filter(), чтобы оставить в списке
# только числа, кратные 4.

list_numbers = [10, 12, 15, 16, 20, 24, 30]
filtered_numbers = list(filter(lambda x: x % 4 == 0, list_numbers))
print(f'Числа, кратные 4, из списка {list_numbers}: {filtered_numbers}')

# 10.Используйте lambda и функцию map(), чтобы возвести каждый
# элемент в списке в куб.

list_to_cube = [1, 2, 3, 4, 5]
cubed_list = list(map(lambda x: x**3, list_to_cube))
print(f'Кубы чисел из списка {list_to_cube}: {cubed_list}')
