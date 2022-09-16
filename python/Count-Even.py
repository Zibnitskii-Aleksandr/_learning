#
# Author        : Zibnitskii Aleksandr
# Date          : 04/05/2020
# Description   : Count even numbers
# Task          : Дан список из целых чисел длиной N подсчитать количество четных чисел в списке
#               : (прим.: список генерируется автоматически из диапазона чисел от 1 до 50, длина
#                 списка задается пользователем)
#
import random

num_data = []
count = " "
result = 0

def listGenerator(count):
    global num_data
    for i in range(count):
        n = random.randint(1, 50)
        num_data.append(n)
    return num_data

def getLength(count):
    while count.isnumeric() != True:
        print("Введите длину генерируемое списка (целое число от 6 до 25)")
        print("или введите '***' для выхода из программы")
        count = input("Введите значение?: ")
        if count == "***":
            print("Всего хорошего!")
            print("~" * 80)
            break
        elif count.isnumeric() == True:
            if int(count) in range(0, 5):
                print("Число должно быть в диапазоне от 6 до 25!")
                print("~" * 80)
                count = " "
                continue
            else:
                return int(count)
        else:
            print("Неверный ввод значения!")
            print("~" * 80)

print("~" * 80)
count = getLength(count)
num_data = listGenerator(count)
result = list(filter(lambda n: n % 2== 0, num_data))
print("~" * 80)
print("Для сгенерированного списка из",count,"элементов")
print(num_data)
print("Количество четных элементов равно",len(result))
print(result)
print("~" * 80)
