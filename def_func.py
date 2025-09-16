# Одна штука товара стоит 20,4 руб. Напечатать таблицу стоимости 2,3,4...20 штук этого товара.
 
def prices(price):
    for i in range(2, 20+1):
        print(f'Стоимость {i} штук = {i * price:.2f} руб')
 
def main():
    price = 20.4
    prices(price)
 
main()
 
# Напечатать таблицу стоимости 50,100,150..1000г сыра. Стоимость 1кг вводится с клавиатуры.
 
def prices(price):
    for i in range(50, 1000+1, 50):
        cost = i * (price/1000)
        print(f'Стоимость {i} грамм = {int(cost)} руб')
 
def main():
    price = int(input('Введите стоимость 1кг сыра в руб: '))
    prices(price)
 
main()
 
# Известна масса каждого из 12 предметов. Найти общую массу всего набора
 
def sum_weight():
    summ = 0
    for i in range(1, 12+1):
        weight = int(input('Введите вес предмета : '))
        print(f'Вес {i} предмета = {weight}')
        summ += weight
    print(summ)
 
def main():
    sum_weight()
 
main()
 
 
# Напечатать числа след образом (6.5)
 
def nums():
    for i in range(21, 10-1, -1):
        print(i, i - 1.8)
 
def main():
    nums()
 
main()
 
def nums_2():
    for i in range(45, 25-1, -1):
        print(i, i - 0.5, i - 0.8)
 
def main():
    nums_2()
 
main()

# Напечатать числа след образом (6.6)


def nums():
    for i in range(21, 35+1):
        print(i, i - 0.6)
 
def main():
    nums()
 
main()
 
def nums_2():
    for i in range(16, 24+1):
        print(i, i - 0.5, i + 0.8)

def main():
    nums_2()
 
main()

# 4.6. Если целое число m делится нацело на целое число n, 
# то вывести на экран частное от деления, 
# в противном случае вывести сообщение "m на n нацело не делится". 

print("Задание 4.6")
print("--------------------------------")

def check_divide(m,n):
    if n == 0:
        return "Ошибка: деление на ноль!"
    if m % n == 0:
        return (f'Частное от деления {m} на {n} = {int(m / n)}')
    else:
        return (f"{m} на {n} нацело не делится")

def main():
    try:
        m = int(input("Введите значение m: "))
        n = int(input("Введите значение n: "))
        result = check_divide(m, n)
        print(result)

    except ValueError:
        print('Ошибка! Введите целое число.')
        exit()

main()

# 4.7. Определить, является ли число a делителем числа b? 

print("Задание 4.7")
print("--------------------------------")


def check_div(a,b):
    if a == 0:
        return "Ошибка: делитель не может быть нулем!"
    if b == 0:
        return "Любое число является делителем нуля (кроме 0)!"
    if b % a == 0:
        return (f'Число {a} является делителем числа {b}')
    else:
        return (f'Число {a} не является делителем числа {b}')

def main():
    try:
        a = int(input("Введите значение a: "))
        b = int(input("Введите значение b: "))
        result = check_div(a,b)
        print(result)
    except ValueError:
        print('Ошибка! Введите целое число.')
        exit()

main()

# 4.8. Дано натуральное число. Определить: 
# а) является ли оно четным; 
# б) оканчивается ли оно цифрой 7. 

# print("Задание 4.8")
# print("--------------------------------")


def check_num(num):
    if num < 1:
        return 'Вы ввели не натуральное число!'
    
    res = ''

    if num % 2 == 0:
        res += f"Число {num} является четным"
    else:
        res += f"Число {num} является нечетным"

    if num % 10 == 7:
        res += f"Число {num} оканчивается на 7"
    else:
        res += f"Число {num} не оканчивается на 7"

    return res


def main():
    try:
        a = int(input("Введите значение натурального числа: "))
        result = check_num(a)
        print(result)

    except ValueError:
        print('Ошибка! Введите целое число.')
        exit()

main()

# 4.10. Дано двузначное число. Определить, равен ли 
# квадрат этого числа учетверенной сумме кубов его цифр. 
# Например, для числа 48 ответ положительный, для числа 52 — отрицательный. 


def check_number(number):
    if number > 99 or number < 10:
        return('Введено не двузначное число!')

    digit = number % 10
    tens = number // 10

    if number**2 == 4 * (digit**3 + tens**3):
        return f'Квадрат числа {number} равен учетверенной сумме кубов его цифр'
    else:
        return f'Квадрат числа {number} не равен учетверенной сумме кубов его цифр'

def main():
    print("Задание 4.10")
    print("--------------------------------")
    try:
        number = int(input("Введите двузначное число: "))
        result = check_number(number)
        print(result)
    except ValueError:
        print('Ошибка! Введите целое число.')
        exit()

main()

# 4.15. Дано трехзначное число. Определить, равен ли квадрат этого числа сумме кубов его цифр. 


def check_number(number):
    if number < 100 or number > 999:
        return 'Введено не трехзначное число!'
     
    digit = number % 10
    tens = number // 10 % 10
    hundreds = number // 100

    if number**2 == (digit**3 + tens**3 + hundreds**3):
        return f'Квадрат числа {number} равен сумме кубов его цифр'
    else:
        return f'Квадрат числа {number} не равен сумме кубов его цифр'

def main():
    print("Задание 4.15")
    print("--------------------------------")
    try:
        number = int(input('Введите трехзначное число: '))
        result = check_number(number)
        print(result)
    except ValueError:
        print('Ошибка! Введите целое число.')
        exit()
main()


# 3.7. Вычислить значение логического выражения при следующих значениях логических величин А, В и С: А = Истина, В = Ложь, С = Ложь: 
# a) А или не (А и В) или С; 
# b) не А или А и (В или С); 
# c) (А или В и не С) и С. 

def results():
    A = True
    B = False
    C = False
    
    res_a = A or not (A and B) or C
    res_b = not A or A and (B or C)
    res_c = (A or B and not C) and C
    
    print(f"a) A or not (A and B) or C = {res_a}")
    print(f"b) not A or A and (B or C) = {res_b}")
    print(f"c) (A or B and not C) and C = {res_c}")

def main():
    print("Задание 3.7")
    print("Результаты логических выражений:")
    print("--------------------------------")
    print('Значения величин:\nA = True\nB = False\nC = False\n')
    
    results()

main()


# 3.10. Вычислить значение логического выражения при следующих значениях логических величин А, В и С: А = Ложь, В = Ложь, С = Истина: 
# a) (не А или не В) и не С; 
# b) (не А или не В) и (А или В); 
# c) А и В или А и С или не С.

def results():
    A = False
    B = False
    C = True

    result_a = (not A or not B) and not C
    result_b = (not A and not B) and (A or B)
    result_c = A and B or A and C or not C

    print(f"a) (not A or not B) and not C = {result_a}")
    print(f"b) (not A and not B) and (A or B) = {result_b}")
    print(f"c) A and B or A and C or not C = {result_c}", end='\n\n\n')

def main():
    print("Задание 3.10")
    print("Результаты логических выражений:")
    print("--------------------------------")
    print('Значения величин:\nA = False\nB = False\nC = True\n')
    
    results()

main()


# 3.12. Вычислить значение логического выражения при всех возможных значениях логических величин А, В и С: 
# a) не (А или не В и С); 
# b) А и не (В или не С); 
# c) не (не А или В и С). 


def results():
    A = False
    B = True
    C = True

    result_a = not (A or not B and C)
    result_b = A and not (B or not C)
    result_c = not (not A or B and C)

    print(f"a) not (A or not B and C) = {result_a}")
    print(f"b) A and not (B or not C) = {result_b}")
    print(f"c) not (not A or B and C) = {result_c}", end='\n\n\n')

def main():
    print("Задание 3.12")
    print("Результаты логических выражений:")
    print("--------------------------------")
    print('Мои значения величин:\nA = False\nB = True\nC = True\n')
    
    results()

main()


# 3.14. Вычислить значение логического выражения при всех возможных значениях логических величин А, В и С: 
# a) не (А и В) и (не А или не С); 
# b) не (А и не В) или (А или не С); 
# c) А и не В или не (А или не С).

def results():
    A = False
    B = True
    C = False

    result_a = not (A and B) and (not A or not C)
    result_b = not (A and not B) or (A or not C)
    result_c = A and not B or not (A or not C)

    print(f"a) not (A and B) and (not A or not C) = {result_a}")
    print(f"b) not (A and not B) or (A or not C) = {result_b}")
    print(f"c) A and not B or not (A or not C) = {result_c}", end='\n\n\n')

def main():
    print("Задание 3.14")
    print("Результаты логических выражений:")
    print("--------------------------------")
    print('Мои значения величин:\nA = False\nB = True\nC = False\n')
    
    results()

main()


# 3.16. Записать условие, которое является истинным, когда: 
# a) каждое из чисел X и Y нечетное; 
# b) только одно из чисел X и Y меньше 20; 
# c) хотя бы одно из чисел X и Y равно нулю; 
# d) каждое из чисел X, Y, Z отрицательное; 
# e) только одно из чисел X, Y и Z кратно пяти; 
# f) хотя бы одно из чисел X, Y, Z больше 100. 

def results(X,Y,Z):
    result_a = (X % 2 == 1) and (Y % 2 == 1)
    result_b = (X < 20) != (Y < 20)
    result_c = (X == 0) or (Y == 0)
    result_d = (X < 0) and (Y < 0) and (Z < 0)
    result_e = ((X%5==0 and Y%5!=0 and Z%5!=0) or 
                (X%5!=0 and Y%5==0 and Z%5!=0) or 
                (X%5!=0 and Y%5!=0 and Z%5==0))
    result_f = (X > 100) or (Y > 100) or (Z > 100)

    print(f"a) Каждое из чисел X и Y нечетное = {result_a}")
    print(f"b) Только одно из чисел X и Y меньше 20 = {result_b}")
    print(f"c) Хотя бы одно из чисел X и Y равно нулю = {result_c}")
    print(f"d) Каждое из чисел X, Y, Z отрицательное = {result_d}")
    print(f"e) Только одно из чисел X, Y и Z кратно пяти = {result_e}")
    print(f"f) Хотя бы одно из чисел X, Y, Z больше 100 = {result_f}", end='\n\n\n')

def main():
    print("Задание 3.16")
    print("Результаты логических выражений:")
    print("--------------------------------")
    print('Мои значения величин:\nX = 7\nY = 13\nZ = -5\n')
    X, Y, Z = 7, 13, -5

    results(X,Y,Z)

main()

# 2.7. Дано двузначное число. Получить число, образованное при перестановке цифр заданного числа.

def rev_num(num):
    if num > 99 or num < 10:
        return 'Введено не двузначное число!'


    digit = num // 10
    tens = num % 10
    result = tens * 10 + digit

    return f'Пользователь ввел {num}.\nЧисло образованное при перестановке цифр = {result}'

def main():
    number_rev = int(input('Введите двузначное число: '))
    result = rev_num(number_rev)
    print(result)

main()

# 2.6. Дано двузначное число. Найти: 
# а) число десятков в нем; 
# б) число единиц в нем; 
# в) сумму его цифр; 
# г) произведение его цифр. 

def check_num(num):
    if num > 99 or num < 10:
        return 'Введено не двузначное число!'


    result_a = num // 10
    result_b = num % 10
    result_c = result_a + result_b
    result_d = result_a * result_b

    print(f'Пользователь ввел {num}.\nВ числе {num} хранится {result_a} десятков.\nВ числе {num} хранится {result_b} единиц')
    print(f'Сумма {result_a} + {result_b} = {result_c}\nПроизведение цифр {result_a} * {result_b} = {result_d}')

def main():
    number_rev = int(input('Введите двузначное число: '))
    check_num(number_rev)

main()


# 2.8. Дано трехзначное число. Найти: 
# а) число единиц в нем;
# б) число десятков в нем; 
# в) сумму его цифр; 
# г) произведение его цифр. 

def check_num(num):
    if num > 99 or num < 10:
        return 'Введено не двузначное число!'


    digit = num % 10
    tens = num // 10 % 10
    hundreds = num // 100
    summ_num = digit + tens + hundreds
    mult_num = digit * tens * hundreds

    print(f'В числе {num} хранится {digit} единиц, {tens} десятков, {hundreds} сотен.')
    print(f'Произведение цифир числа {num} = {mult_num}\nСумма числа {num} = {summ_num}')

def main():
    number_rev = int(input('Введите двузначное число: '))
    check_num(number_rev)

main()

# 2.9. Дано трехзначное число. Найти число, полученное при прочтении его цифр справа налево. 

def rev_num(num):
    if num < 100 or num > 999:
        return 'Введено не трехзначное число!'


    digit = num % 10
    tens = num // 10 % 10
    hundreds = num // 100

    result = digit * 100 + tens * 10 + hundreds
    print(f'Пользователь ввел {num}.\nЧисло, полученное при прочтении его цифр справа налево = {result}')

def main():
    number = int(input('Введите трехзначное число: '))
    rev_num(number)

main()


# 2.10. Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее в конце. Найти полученное число. 

def new_num(number):
    if number < 100 or number > 999:
        return 'Введено не трехзначное число!'

    last_num = number // 100
    result = number % 100 * 10 + last_num
    return f'Пользователь ввел {number}.\nПри переносе первой цифры в конец числа, получили: {result}'

def main():
    number = int(input('Введите трехзначное число: '))
    result = new_num(number)
    print(result)

main()
