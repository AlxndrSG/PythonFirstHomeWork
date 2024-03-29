# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом
# называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

number = int(input('Введите номер билета: '))
if 99999 < number < 1000000:
    halfOne = number // 1000
    halfTwo = number % 1000
    if (halfOne % 10 + (halfOne // 10) % 10 + halfOne//100) == (halfTwo % 10+(halfTwo//10) % 10+halfTwo//100):
        print('Билет счастливый')
    else:
        print('Билет не счастливый')
else: 
    print('Такого билета не существует!')   
 
#Без проверки, через индекс строки
#number = input('Введите номер билета: ')
# if sum(list(map(int,number[3:]))) == sum(list(map(int,number[:3]))):
#     print('Билет счастливый')
# else:
#     print('Билет не счастливый')