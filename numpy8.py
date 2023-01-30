import numpy as np

lst = [1, 2, 3]
a = np.array([1, 2, 3])

print(lst*2) # список: [1, 2, 3, 1, 2, 3]
print(a*2) # массив: array([2, 4, 6])

# при умножении списка языка Python, он дублируется дважды, а при умножении
# на NumPy массив – каждый его элемент умножается математически на число 2

# Если бы мы захотели то же самое реализовать непосредственно на Python, оперируя списками, то пришлось бы делать что-то вроде:
v = [x*2 for x in lst]

print(-a) # унарный минус [-1 -2 -3]
print(a + 2) # сложение с числом [3 4 5]
print(2 + a)  # так тоже можно записывать [3 4 5]
print(a - 3) # вычитание с числом [-2 -1 0]
print(a * 5) # умножение на число [5 10 15]
print(a / 5)  # деление на число [0.2 0.4 0.6]
print(a // 2)  # целочисленное деление [0 1 1]
print(a ** 3)  # возведение в степень 3 [1 8 27]
print(a % 2)  # вычисление по модулю 2 [1 0 1]

b = np.array([3, 4, 5])

print(a - b)  # array([-2, -2, -2])
print(b + a)  # array([4, 6, 8])
print(a * b)  # array([ 3,  8, 15])
print(b / a)  # array([3. , 2. , 1.66666667])
print(b // a) # array([3, 2, 1], dtype=int32)
print(b ** a) # array([  3,  16, 125], dtype=int32)
print(b % a)  # array([0, 0, 2], dtype=int32)

b = np.array([3, 4, 5, 6])
# print(a + b)  # ошибка: длины массивов не совпадают


# транслирование массивов

b = np.arange(1, 7)
b.resize(2, 3)
print(a + b)
# Все рассмотренные операции можно распространить и на многомерные массивы, главное, чтобы они были согласованы по размерам

a = np.arange(1, 19)
a.resize(3, 3, 2)
b = np.ones((3, 2))

print(a - b)
print(a * 10)
print(a // b)

d = np.array([1, 2, 6, 8])
d += 5
print(d)
c = np.ones(4)
c *= d
print(c)

"""
При выполнении арифметических операций тип данных автоматически приводится к более общему.
результатом сложения вещественного числа с целочисленным, итоговое значение представляет собой вещественное число. 
Но тип данных массива a – целочисленный и он не может сохранять вещественные числа

Если, например, массив b определить с типом данных float64:

b = np.ones(4, dtype='float64')

а массив a имеет тип int32 (можно посмотреть через свойство a.dtype), то операция:
a += b

приведет к ошибке

при работе с целочисленными и вещественными числами на выходе получаем вещественные. 
При работе с вещественными и комплексными – комплексные
"""