# 4.6. Если целое число m делится нацело на целое число n, 
# то вывести на экран частное от деления, 
# в противном случае вывести сообщение "m на n нацело не делится". 

print("Задание 4.6")
print("--------------------------------")

try:
    m = int(input("Введите значение m: "))
    n = int(input("Введите значение n: "))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if m % n == 0:
    print(f'Частное от деления {m} на {n} = {int(m / n)}')
else:
    print(f"{m} на {n} нацело не делится")


# 4.7. Определить, является ли число a делителем числа b? 

print("Задание 4.7")
print("--------------------------------")

try:
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if b % a == 0:
    print(f'Число {a} является делителем числа {b}')
else:
    print(f'Число {a} не является делителем числа {b}')

# 4.8. Дано натуральное число. Определить: 
# а) является ли оно четным; 
# б) оканчивается ли оно цифрой 7. 

print("Задание 4.8")
print("--------------------------------")

try:
    a = int(input("Введите значение натурального числа: "))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if a < 0:
    print('Вы ввели не натуральное число!')
    exit()

if a % 2 == 0:
    print(f"Число {a} является четным")
else:
    print(f"Число {a} является нечетным")

if a % 10 == 7:
    print(f"Число {a} оканчивается на 7")
else:
    print(f"Число {a} не оканчивается на 7")


# 4.9. Дано двузначное число. Определить: 
# а) какая из его цифр больше: первая или вторая; 
# б) одинаковы ли его цифры.

print("Задание 4.9")
print("--------------------------------")

try:
    number = int(input("Введите двузначное число: "))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number > 99 or number < 10:
    print('Введено не двузначное число!')

digit = number % 10
tens = number // 10
# a)
if digit > tens:
    print(f'Цифра {digit} больше цифры {tens}')
else:
    print(f'Цифра {tens} больше цифры {digit}')
# b)
if digit == tens:
    print(f'Цифры числа {number} равны')
else:
    print(f'Цифры числа {number} не равны')

# 4.10. Дано двузначное число. Определить, равен ли 
# квадрат этого числа учетверенной сумме кубов его цифр. 
# Например, для числа 48 ответ положительный, для числа 52 — отрицательный. 

print("Задание 4.10")
print("--------------------------------")

try:
    number = int(input("Введите двузначное число: "))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number > 99 or number < 10:
    print('Введено не двузначное число!')

digit = number % 10
tens = number // 10

if number**2 == 4 * (digit**3 + tens**3):
    print(f'Квадрат числа {number} равен учетверенной сумме кубов его цифр')
else:
    print(f'Квадрат числа {number} не равен учетверенной сумме кубов его цифр')
    
# 4.11. Дано двузначное число. Определить: 
# а) является ли сумма его цифр двузначным числом; 
# б) больше ли числа а сумма его цифр. 

print("Задание 4.11")
print("--------------------------------")

try:
    number = int(input("Введите двузначное число: "))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number > 99 or number < 10:
    print('Введено не двузначное число!')

digit = number % 10
tens = number // 10

# a)
if 10 < (digit + tens) < 99:
    print(f'Сумма цифр числа {number} является двузначным числом')
else:
    print(f'Сумма цифр числа {number} не является двузначным числом')

# b)
if (digit + tens) > number:
    print(f'Сумма цифр {digit}, {tens} больше числа {number}')
else:
    print(f'Сумма цифр {digit}, {tens}  меньше числа {number}')

# 4.12. Дано двузначное число. Определить: 
# а) кратна ли трем сумма его цифр; 
# б) кратна ли сумма его цифр числу а. 

print("Задание 4.12")
print("--------------------------------")

try:
    number = int(input("Введите двузначное число: "))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number > 99 or number < 10:
    print('Введено не двузначное число!')

digit = number % 10
tens = number // 10

# a)

if (digit + tens) % 3 == 0:
    print(f'Сумма цифр {digit}, {tens} кратна 3')
else:
    print(f'Сумма цифр {digit}, {tens} не кратна 3')

# b)

if (digit + tens) % number == 0:
    print(f'Сумма цифр {digit}, {tens} кратна {number}')
else:
    print(f'Сумма цифр {digit}, {tens} не кратна {number}')


# 4.13. Дано трехзначное число. Выяснить, является ли оно палиндромом ("перевертышем"),
# т. е. таким числом, десятичная запись которого читается одинаково слева направо и справа налево. 

print("Задание 4.13")
print("--------------------------------")


try:
    number = int(input('Введите трехзначное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100
palindrom = digit * 100 + tens * 10 + hundreds

if number == palindrom:
    print(f'Число {number} является палиндромом')
else:
    print(f'Число {number} не является палиндромом')


# 4.14.  Дано трехзначное число. Определить, какая из его цифр больше:
# а) первая или последняя; 
# б) первая или вторая; 
# в) вторая или последняя. 

print("Задание 4.14")
print("--------------------------------")


try:
    number = int(input('Введите трехзначное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100

# a)

if hundreds > digit:
    print(f'В числе {number}, первая цифра больше последней')
else:
    print(f'В числе {number}, последняя цифра больше первой')

# б)

if hundreds > tens:
    print(f'В числе {number}, первая цифра больше второй')
else:
    print(f'В числе {number}, вторая цифра больше первой')

# в)

if digit > tens:
    print(f'В числе {number}, последняя цифра больше второй')
else:
    print(f'В числе {number}, вторая цифра больше последней')

# 4.15. Дано трехзначное число. Определить, равен ли квадрат этого числа сумме кубов его цифр. 

print("Задание 4.15")
print("--------------------------------")

try:
    number = int(input('Введите трехзначное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100

if number**2 == (digit**3 + tens**3 + hundreds**3):
    print(f'Квадрат числа {number} равен сумме кубов его цифр')
else:
    print(f'Квадрат числа {number} не равен сумме кубов его цифр')


# 4.16. Дано трехзначное число. Определить: 
# а) является ли сумма его цифр двузначным числом; 
# б) является ли произведение его цифр трехзначным числом; 
# в) больше ли числа а произведение его цифр; 
# г) кратна ли пяти сумма его цифр; 
# д) кратна ли сумма его цифр числу а.


print("Задание 4.16")
print("--------------------------------")

try:
    number = int(input('Введите трехзначное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100

# a)

if 10 <= (digit + tens + hundreds) <= 99:
    print(f'Сумма цифр числа {number} является двузначным числом')
else:
    print(f'Сумма цифр числа {number} не является двузначным числом')

# б)

if 100 <= (digit * tens * hundreds) <= 999:
    print(f'Произведение цифр числа {number} является трехзначным числом')
else:
    print(f'Произведение цифр числа {number} не является трехзначным числом')   

# в)

if (digit * tens * hundreds) > number:
    print(f'Произведение цифр числа {hundreds}, {tens}, {digit} больше числа {number}')
else:
    print(f'Произведение цифр числа {hundreds}, {tens}, {digit} не больше числа {number}') 

# г)

if (digit + tens + hundreds) % 5 == 0:
    print(f'Сумма цифр числа {number} кратна 5')
else:
    print(f'Сумма цифр числа {number} не кратна 5')    

# д)

if (digit + tens + hundreds) % number == 0:
    print(f'Сумма цифр числа кратна числу {number}')
else:
    print(f'Сумма цифр числа не кратна числу {number}')

# 4.17. Дано трехзначное число. 
# а) Верно ли, что все его цифры одинаковые? 
# б) Определить, есть ли среди его цифр одинаковые. 


print("Задание 4.17")
print("--------------------------------")

try:
    number = int(input('Введите трехзначное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100

# а)

if digit == tens == hundreds:
    print(f'Все цифры числа {number} одинаковы')
else:
    print(f'Утверждение о том что все цифры {number} одинаковы - неверно')

# б)

if digit == tens or digit == hundreds or tens == hundreds:
    print(f'В числе {number} есть одинаковые цифры')
else:
    print(f'В числе {number} нет одинаковых цифр')

# 4.18. Дано четырехзначное число. Определить: 
# а) равна ли сумма двух первых его цифр сумме двух его последних цифр; 
# б) кратна ли трем сумма его цифр; 
# в) кратно ли четырем произведение его цифр;
# г) кратно ли произведение его цифр числу а. 

print("Задание 4.18")
print("--------------------------------")

try:
    number = int(input('Введите четырехзначное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number < 1000 or number > 9999:
    print('Введено не четырехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000

# а)

if (thousands + hundreds) == (tens + digit):
    print(f'Сумма двух первых цифр числа {number} равна сумме двух его последних цифр')
else:
    print(f'Сумма двух первых цифр числа {number} не равна сумме двух его последних цифр')

# б)

if (thousands + hundreds + tens + digit) % 3 == 0:
    print(f'Сумма цифр числа {number} кратна трем')
else:
    print(f'Сумма цифр числа {number} не кратна трем')

# в)

if (thousands * hundreds * tens * digit) % 4 == 0:
    print(f'Произведение цифр числа {number} кратна четырем')
else:
    print(f'Произведение цифр числа {number} не кратна четырем')

# г)

if (thousands * hundreds * tens * digit) % number == 0:
    print(f'Произведение цифр кратно числу {number}')
else:
    print(f'Произведение цифр не кратно числу {number}')

# 4.19. Дано натуральное число. 
# а) Верно ли, что оно заканчивается четной цифрой? 
# б) Верно ли, что оно заканчивается нечетной цифрой?

print("Задание 4.19")
print("--------------------------------")

try:
    number = int(input('Введите натуральное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()


if number < 0:
    print('Вы ввели не натуральное число!')
    exit()

# а)

if (number % 10) % 2 == 0:
    print(f'Число {number} заканчивается четной цифрой')
else:
    print(f'Число {number} заканчивается нечетной цифрой')

# б)

if (number % 10) % 2 != 0:
    print(f'Число {number} заканчивается нечетной цифрой')
else:
    print(f'Число {number} заканчивается четной цифрой')

# 4.30. Дано трехзначное число. Определить: 
# а) входят ли в него цифры 4 или 7; 
# б) входят ли в него цифры 3, 6 или 9. 


print("Задание 4.30")
print("--------------------------------")

try:
    number = int(input('Введите трехзначное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100

# а)
has_4_or_7 = False
if hundreds == 4 or hundreds == 7:
    has_4_or_7 = True
elif tens == 4 or tens == 7:
    has_4_or_7 = True
elif digit == 4 or digit == 7:
    has_4_or_7 = True

if has_4_or_7:
    print(f'В число {number} входят цифры 4 или 7')
else:
    print(f'В число {number} не входят цифры 4 или 7')

# б)

has_3_or_6_or_9 = False
if hundreds == 3 or hundreds == 6 or hundreds == 9:
    has_3_or_6_or_9 = True
elif tens == 3 or tens == 6 or tens == 9:
    has_3_or_6_or_9= True
elif digit == 3 or digit == 6 or digit == 9:
    has_3_or_6_or_9 = True

if has_3_or_6_or_9:
    print(f'В число {number} входят цифры 3, 6 или 9')
else:
    print(f'В число {number} не входят цифры 3, 6 или 9')

# 4.32. Дано натуральное число n (n > 9999). Выяснить, является ли оно палиндромом 
# ("перевертышем") с учетом четырех цифр, как, например, числа 7777, 8338, 0330 и т. п. (
# Палиндромом называется число, десятичная запись которого читается одинаково слева направо и справа налево.) 

print("Задание 4.32")
print("--------------------------------")

try:
    number = int(input('Введите натуральное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()


if number < 0:
    print('Число должно быть натуральным (положительным)!')
    exit()
if number <= 9999:
    print('Число должно быть больше 9999!')
    exit()

last_four_digits = number % 10000
digit_1 = last_four_digits % 10
digit_2 = last_four_digits // 10 % 10
digit_3 = last_four_digits // 100 % 10
digit_4 = last_four_digits // 1000

if digit_1 == digit_4 and digit_2 == digit_3:
    print(f'Последние 4 цифры числа {number} ({last_four_digits:04d}) образуют палиндром')
else:
    print(f'Последние 4 цифры числа {number} ({last_four_digits:04d}) не образуют палиндром')

# 4.33. Дано натуральное число n (n > 9999). 
# Выяснить, верно ли, что это число содержит 
# ровно три одинаковые цифры с учетом четырех цифр,
# как, например, числа 3363, 4844, 0300 и т. п. 

print("Задание 4.33")
print("--------------------------------")

try:
    number = int(input('Введите натуральное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()


if number < 0:
    print('Число должно быть натуральным (положительным)!')
    exit()
if number <= 9999:
    print('Число должно быть больше 9999!')
    exit()

last_four_digits = number % 10000
d1 = last_four_digits // 1000
d2 = last_four_digits // 100 % 10
d3 = last_four_digits // 10 % 10
d4 = last_four_digits % 10

if (d1 == d2 == d3 and d1 != d4) or (d1 == d2 == d4 and d1 != d3) or (d1 == d3 == d4 and d1 != d2) or (d2 == d3 == d4 and d2 != d1):
    print(f'В последних 4 цифрах числа {number} ({last_four_digits:04d}) есть ровно три одинаковые цифры')
else:
    print(f'В последних 4 цифрах числа {number} ({last_four_digits:04d}) нет ровно трех одинаковых цифр')

# 4.34. Дано натуральное число n (n > 9999). 
# Выяснить, различны ли все четыре цифры этого числа (с учетом четырех цифр). 
# Например, в числе 3678 все цифры различны, в числе 0023 — нет.

print("Задание 4.34")
print("--------------------------------")

try:
    number = int(input('Введите натуральное число: '))

except ValueError:
    print('Ошибка! Введите целое число.')
    exit()

if number < 0:
    print('Число должно быть натуральным (положительным)!')
    exit()
if number <= 9999:
    print('Число должно быть больше 9999!')
    exit()

last_four_digits = number % 10000
d1 = last_four_digits // 1000
d2 = last_four_digits // 100 % 10
d3 = last_four_digits // 10 % 10
d4 = last_four_digits % 10

if d1 != d2 and d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4 and d3 != d4:
    print(f'В последних 4 цифрах числа {number} ({last_four_digits:04d}) все цифры разные')
else:
    print(f'В последних 4 цифрах числа {number} ({last_four_digits:04d}) не все цифры разные')
