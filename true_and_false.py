# 3.5. Вычислить значение логического выражения при следующих значениях логических величин А, В и С: А = Истина, В = Ложь, С = Ложь: 
# а) А или В и не С; 
# b) А и не В или С; 
# c) не А и не В; 
# d) А и (не В или С); 
# e) не (А и С) или В; 
# f) А или (не (В и С)). 

print("Задание 3.5")
print("Результаты логических выражений:")
print("--------------------------------")
print('Значения величин:\nA = True\nB = False\nC = False\n')

A = True
B = False
C = False

result_a = A or B and not C
result_b = A and not B or C
result_c = not A and not B 
result_d = A and (not B or C)
result_e = not (A and C) or B
result_f = A or (not (B and C))

print(f"a) А или В и не С = {result_a}")
print(f"b) А и не В или С = {result_b}")
print(f"c) не А и не В = {result_c}")
print(f"d) А и (не В или С) = {result_d}")
print(f"e) не (А и С) или В = {result_e}")
print(f"f) А или (не (В и С)) = {result_f}", end='\n\n\n')

# 3.7. Вычислить значение логического выражения при следующих значениях логических величин А, В и С: А = Истина, В = Ложь, С = Ложь: 
# a) А или не (А и В) или С; 
# b) не А или А и (В или С); 
# c) (А или В и не С) и С. 

print("Задание 3.7")
print("Результаты логических выражений:")
print("--------------------------------")
print('Значения величин:\nA = True\nB = False\nC = False\n')

A = True
B = False
C = False

result_a = A or not (A and B) or C
result_b = not A or A and (B or C)
result_c = (A or B and not C) and C

print(f"a) A or not (A and B) or C = {result_a}")
print(f"b) not A or A and (B or C) = {result_b}")
print(f"c) (A or B and not C) and C = {result_c}", end='\n\n\n')

# 3.10. Вычислить значение логического выражения при следующих значениях логических величин А, В и С: А = Ложь, В = Ложь, С = Истина: 
# a) (не А или не В) и не С; 
# b) (не А или не В) и (А или В); 
# c) А и В или А и С или не С.

print("Задание 3.10")
print("Результаты логических выражений:")
print("--------------------------------")
print('Значения величин:\nA = False\nB = False\nC = True\n')

A = False
B = False
C = True

result_a = (not A or not B) and not C
result_b = (not A and not B) and (A or B)
result_c = A and B or A and C or not C

print(f"a) (not A or not B) and not C = {result_a}")
print(f"b) (not A and not B) and (A or B) = {result_b}")
print(f"c) A and B or A and C or not C = {result_c}", end='\n\n\n')

# 3.12. Вычислить значение логического выражения при всех возможных значениях логических величин А, В и С: 
# a) не (А или не В и С); 
# b) А и не (В или не С); 
# c) не (не А или В и С). 

print("Задание 3.12")
print("Результаты логических выражений:")
print("--------------------------------")
print('Мои значения величин:\nA = False\nB = True\nC = True\n')
A = False
B = True
C = True

result_a = not (A or not B and C)
result_b = A and not (B or not C)
result_c = not (not A or B and C)

print(f"a) not (A or not B and C) = {result_a}")
print(f"b) A and not (B or not C) = {result_b}")
print(f"c) not (not A or B and C) = {result_c}", end='\n\n\n')

# 3.14. Вычислить значение логического выражения при всех возможных значениях логических величин А, В и С: 
# a) не (А и В) и (не А или не С); 
# b) не (А и не В) или (А или не С); 
# c) А и не В или не (А или не С).

print("Задание 3.14")
print("Результаты логических выражений:")
print("--------------------------------")
print('Мои значения величин:\nA = False\nB = True\nC = False\n')
A = False
B = True
C = False

result_a = not (A and B) and (not A or not C)
result_b = not (A and not B) or (A or not C)
result_c = A and not B or not (A or not C)

print(f"a) not (A and B) and (not A or not C) = {result_a}")
print(f"b) not (A and not B) or (A or not C) = {result_b}")
print(f"c) A and not B or not (A or not C) = {result_c}", end='\n\n\n')

# 3.16. Записать условие, которое является истинным, когда: 
# a) каждое из чисел X и Y нечетное; 
# b) только одно из чисел X и Y меньше 20; 
# c) хотя бы одно из чисел X и Y равно нулю; 
# d) каждое из чисел X, Y, Z отрицательное; 
# e) только одно из чисел X, Y и Z кратно пяти; 
# f) хотя бы одно из чисел X, Y, Z больше 100. 

print("Задание 3.16")
print("Результаты логических выражений:")
print("--------------------------------")
print('Мои значения величин:\nX = 7\nY = 13\nZ = -5\n')

X, Y, Z = 7, 13, -5

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

# 3.30. Записать условие, которое является истинным, когда: 
# a) целое А кратно двум или трем; 
# b) целое А не кратно трем и оканчивается нулем. 

print("Задание 3.30")
print("Результаты логических выражений:")
print("--------------------------------")

A = 20  

result_a = (A % 2 == 0) or (A % 3 == 0)
result_b = (A % 3 != 0) and (A % 10 == 0)

print(f"Для A = {A}:")
print(f"a) Кратно двум или трем: {result_a}")
print(f"b) Не кратно трем и оканчивается нулем: {result_b}")

# 3.31. Записать условие, которое является истинным, когда: 
# a) целое N кратно пяти или семи; 
# b) целое N кратно четырем и не оканчивается нулем.

print("Задание 3.31")
print("Результаты логических выражений:")
print("--------------------------------")

N = 28

result_a = (N % 5 == 0) or (N % 7 == 0)
result_b = (N % 4 == 0) and (N % 10 != 0)

print(f"Для N = {N}:")
print(f"a) N кратно пяти или семи: {result_a}")
print(f"b) N кратно четырем и не оканчивается нулем: {result_b}", end='\n\n\n')