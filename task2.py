# Найдите сумму цифр трехзначного числа

number = int(input("Введите трехзначное число: "))
if 99 < number < 1000:
    summa = 0
    while number > 0:
        rem = number % 10
        summa = summa + rem
        number = number // 10
    print(f'Сумма цифр числа: {summa}')
else:
    print('Число не является трехзначным!')
