#
# Author        : Zibnitskii Aleksandr
# Date          : 03/05/2020
# Description   : Fibonacci sequence calculation
# Task          : Рассчитать последовательность фибоначчи, длину ряда задает пользователь
#                 (прим.: алгоритм составлен для классической последовательности, в которой
#                 два первых члена последовательности равны "1"
#

fibArr = [ 1, 1]
count = " "

def Fibo(fibArr, count):
    i = 3
    for i in range(count-2):
        newNum = fibArr[-1] + fibArr[-2]
        fibArr.append(newNum)
    return fibArr

print("~" * 60)
while count.isnumeric() != True:
    print("Введите длину последовательности Фибоначчи (целое число > 2)")
    print("или введите '***' для выхода из программы")
    count = input("Введите значение?: ")
    if count == "***":
        print("Всего хорошего!")
        print("~" * 60)
        break
    elif count.isnumeric() == True:
        if int(count) in range(0, 3):
            print("Число должно быть больше 2!")
            count = " "
            print("~" * 60)
            continue
        Fibo(fibArr, int(count))
        print(fibArr)
        fibArr = [1, 1]
        print("~" * 60)
    else:
        print("Неверный ввод значения!")
        print("~" * 60)
    count = " "


