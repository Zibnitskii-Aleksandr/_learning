#
# Author        : Zibnitskii Aleksandr
# Date          : 05/05/2020
# Description   : Compare two numbers
# Task          : Пользователь вводит 2 числа, если первое больше второго, вывести их разность,
#                 если второе больше первого вывести их сумму, если числа равны, возвести первое
#                 в степень второго.

result =" "
numData = []

def procNumbers(data):
    if data[0] == data[1]:
        result = data[0] ** data[1]
        print("Число", data[0],"в степени",data[1], "будет равна", result)
    if data[0] > data[1]:
        result = data[0] - data[1]
        print("Их разность будет равна:",data[0],"-",data[1],"=",result)
    if data[0] < data[1]:
        result = data[0] + data[1]
        print("Их сумма будет равна:",data[0],"+",data[1],"=",result)

def getInput():
    return input("Введите значение: ")

print("~" * 45)
print("Для завершения работы программы введите '***'")
print("Для выполнения алгоритма введите последовательно два целых числа")

while result !="***":
    result = getInput()
    if result == "***":
        print("Спасибо! Всего хорошего...")
        break
    elif result.isnumeric() == False:
        print("Введите целое число или '***' для выхода из программы!")
        result = " "
        continue
    else:
        numData.append(int(result))
        result = " "
        if len(numData) == 2:
            break

print("~" * 45)
print("Для двух введенных Вами чисел",numData)
result = procNumbers(numData)
print("~" * 45)










