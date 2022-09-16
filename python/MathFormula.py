# Author        : Zibnitskii Aleksandr
# Date          : 05/05/2020
# Description   : Calculation of a mathematical formula
# Task          : Пользователь вводит 3 числа, подставить и посчитать формулу:
#                 2a - 8b / (a-b+c). Вывести результат.
import sys

num_data = []
my_var = " "
result = 0

def getInput():
    return input("Введите значение: ")

while my_var !="***":
    print("~" * 65)
    print("Для выхода из программы введите '***'")
    print("Для выполнения программы - введите последовательно три любых целых числа,")
    print("после чего автоматически будет произведен расчет формулы: 2a - 8b / (a-b+c)")
    while len(num_data) < 3:
        my_var = getInput()
        if my_var == "***":
            print("Спасибо! Всего хорошего...")
            sys.exit()
        elif my_var.isnumeric() == False:
            print("Неверный ввод - принимаются только числа!")
            continue


        else:
            num_data.append(int(my_var))
            my_var = " "
            if len(num_data) == 3 and num_data[0] - num_data[1] + num_data[2] == 0:
                print("Повторите ввод с другими числами!")
                print("Сочетание введенных Вами чисел дает в знаменателе '0'!")
                print("На ноль делить нельзя!!!")
                num_data = []
                my_var = " "
                continue

    print("~" * 65)
    result = (2 * num_data[0] - 8 * num_data[1]) / (num_data[0] - num_data[1] + num_data[2])
    print("Для введеных Вами чисел -",num_data)
    print("Результат вычисления формулы: 2a - 8b / (a-b+c) будет равен",result)
    num_data = []




