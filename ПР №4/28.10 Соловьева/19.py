import math

num_var = int(input('Номер варианта № = '))
print('Соловьева Юлия')
print('Группа ИСП.23.1А')

count = 0
sum = 0
x = 0
print(" x            y")
print("-------------------")

while x <= num_var:
    y = 13.72 * math.cos(abs(x)) + (2 * math.pi + 1) / (2 * x + 15.3)
    print(f"{x:.2f}       {y:.4f}")
    x += 0.1 * num_var
    if y < 0:
        count += 1
        sum += y
    else:
        continue
sr = sum/count
print('Среднее арифметическое')
print(f"{sr:.3f}")