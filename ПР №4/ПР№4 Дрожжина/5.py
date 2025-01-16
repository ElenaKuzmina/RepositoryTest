import math

num_var = int(input('Номер варианта  №='))
print('Дрожжина София Юрьевна')
print('Группа ИСП.23.1А')

x = 0
min_y = 1000
max_y = -1000
while x <= num_var :
    y = math.cos(abs(2*x)) / 2*math.pi - x - math.sin(3*x + 2.1)
    print(f'x {x:.3f}  y {y:.3f}')
    x += 0.1 * num_var
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y
    proiz = min_y * max_y
print('Произведение максимального и минимального значений функции:')
print(f'{proiz:.3f}')