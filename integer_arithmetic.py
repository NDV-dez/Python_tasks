# 2.6. Дано двузначное число. Найти: 
# а) число десятков в нем; 
# б) число единиц в нем; 
# в) сумму его цифр; 
# г) произведение его цифр. 

# 32
# a)3 b)2 c)5 d)6

number = int(input("Введите двузначное число: "))

if number > 99 or number < 10:
    print('Введено не двузначное число!')
    exit()

result_a = number // 10
result_b = number % 10
result_c = result_a + result_b
result_d = result_a * result_b

print(f'Пользователь ввел {number}.\nВ числе {number} хранится {result_a} десятков.\nВ числе {number} хранится {result_b} единиц')
print(f'Сумма {result_a} + {result_b} = {result_c}\nПроизведение цифр {result_a} * {result_b} = {result_d}')

# 2.7. Дано двузначное число. Получить число, образованное при перестановке цифр заданного числа.

# 32 -> 23

number_rev = int(input('Введите двузначное число: '))

if number > 99 or number < 10:
    print('Введено не двузначное число!')
    exit()

digit = number_rev // 10
tens = number_rev % 10
result = tens * 10 + digit
# result = int(str(tens) + str(digit))
print(f'Пользователь ввел {number_rev}.\nЧисло образованное при перестановке цифр = {result}')

# 2.8. Дано трехзначное число. Найти: 
# а) число единиц в нем;
# б) число десятков в нем; 
# в) сумму его цифр; 
# г) произведение его цифр. 

number = int(input('Введите трехзначное число: '))

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100
summ_num = digit + tens + hundreds
mult_num = digit * tens * hundreds

print(f'В числе {number} хранится {digit} единиц, {tens} десятков, {hundreds} сотен.')
print(f'Произведение цифир числа {number} = {mult_num}\nСумма числа {number} = {summ_num}')

# 2.9. Дано трехзначное число. Найти число, полученное при прочтении его цифр справа налево. 

number = int(input('Введите трехзначное число: '))

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100

result = digit * 100 + tens * 10 + hundreds
print(f'Пользователь ввел {number}.\nЧисло, полученное при прочтении его цифр справа налево = {result}')

# 2.10. Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее в конце. Найти полученное число. 

number = int(input('Введите трехзначное число: '))

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

last_num = number // 100
result = number % 100 * 10 + last_num
print(f'Пользователь ввел {number}.\nПри переносе первой цифры в конец числа, получили: {result}')

#2.11. Дано трехзначное число. В нем зачеркнули последнюю справа цифру и приписали ее в начале. Найти полученное число. 


number = int(input('Введите трехзначное число: '))

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

last_num = number % 10
result = last_num * 100 + number // 10
print(f'Пользователь ввел {number}.\nПри переносе последней цифры в начало числа, получили: {result}')

# 2.12. Дано трехзначное число. Найти число, полученное при перестановке первой и второй цифр заданного числа. 

number = int(input('Введите трехзначное число: '))

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100
result = tens * 100 + hundreds * 10 + digit

print(f'Пользователь ввел {number}.\nПри перестановке первой цифры и второй, получили: {result}')

# 123 - > 213  2*100=200 1*10=10 3

# 2.13. Дано трехзначное число. Найти число, полученное при перестановке второй и третьей цифр заданного числа. 

number = int(input('Введите трехзначное число: '))

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100
result = hundreds*100 + digit*10 +tens

print(f'Пользователь ввел {number}.\nПри перестановке второй цифры и третьей, получили: {result}')

#123 132 100 + 30 + 2

# 2.14. Дано трехзначное число, в котором все цифры различны. Получить шесть чисел, образованных при перестановке цифр заданного числа.

number = int(input('Введите трехзначное число: '))

if number < 100 or number > 999:
    print('Введено не трехзначное число!')
    exit()

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100

if digit == tens or digit == hundreds or tens == hundreds:
    print('Все цифры числа должны быть различны!')
    exit()

result_1 = hundreds*100 + digit*10 +tens
result_2 = hundreds*10 + digit*100 +tens
result_3 = hundreds + digit*10 +tens*100
result_4 = hundreds + digit*100 +tens*10
result_5 = hundreds*10 + digit +tens*100
result_6 = hundreds*100 + digit +tens*10

print('Все перестановки цифр:')
print(result_1,result_2,result_3,result_4,result_5,result_6)

# 2.15. Дано четырехзначное число. Найти:
# а) сумму его цифр;
# б) произведение его цифр. 


number = int(input('Введите четырехзначное число: '))

if number < 1000 or number > 9999:
    print('Введено не четырехзначное число!')
    exit()

summ = (number % 10) + (number // 10 % 10) + (number // 100 % 10) + (number // 1000)
mult = (number % 10) * (number // 10 % 10) * (number // 100 % 10) * (number // 1000)

print(f'Сумма цифр числа {number} = {summ}.\nПроизведение цифр числа {number} = {mult}')

# 2.16. Дано четырехзначное число. Найти: 
# а) число, полученное при прочтении его цифр справа налево; 
# б) число, образуемое при перестановке первой и второй, третьей и четвертой цифр заданного числа. Например, из числа 5434 получить 4543, из числа 7048— 784; 
# в) число, образуемое при перестановке второй и третьей цифр заданного числа. Например, из числа 5084 получить 5804; 
# г) число, образуемое при перестановке двух первых и двух последних цифр заданного числа. Например, из числа 4566 получить 6645, из числа 7304 — 473. 
# Последнюю задачу решить двумя способами: 
# 1) с выделением отдельных цифр заданного числа; 
# 2) без выделения отдельных цифр заданного числа. 


number = int(input('Введите четырехзначное число: '))

if number < 1000 or number > 9999:
    print('Введено не четырехзначное число!')
    exit()

# 1 способ: 

digit = number % 10
tens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000

result_a = digit * 1000 + tens * 100 + hundreds * 10 + thousands
result_b = hundreds * 1000 + thousands * 100 + digit * 10 + tens
result_c =  thousands * 1000 + tens  * 100 + hundreds * 10 + digit
result_d =  tens * 1000 + digit * 100 + thousands * 10 + hundreds

print(f'Исходное число {number}\nСправа налево: {result_a}\nПерестановка пар цифр: {result_b}\nПерестановка второй и третьей цифр: {result_c}\nПерестановка двух первых и двух последних: {result_d}')

# 2 способ

result_a = (number % 10) * 1000 + (number // 10 % 10) * 100 + (number // 100 % 10) * 10 + number // 1000
result_b = (number // 100 % 10) * 1000 + (number // 1000) * 100 + (number % 10) * 10 + number // 10 % 10
result_c =  (number // 1000) * 1000 + (number // 10 % 10)  * 100 + (number // 100 % 10) * 10 + number % 10
result_d =  (number // 10 % 10) * 1000 + (number % 10) * 100 + (number // 1000) * 10 + number // 100 % 10

print(f'Исходное число {number}\nСправа налево: {result_a}\nПерестановка пар цифр: {result_b}\nПерестановка второй и третьей цифр: {result_c}\nПерестановка двух первых и двух последних: {result_d}')
