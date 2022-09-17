# Author        : Zibnitskii Aleksandr
# Date          : 07/05/2020
# Description   : Sorting input several numbers
# Task          : Пользователь вводит значения через запятую, если количество значений меньше 10,
#                 отсортировать их от большего к меньшему, если больше то от меньшего к большему.
from typing import List

numdata = []

def inputdata():
    numberbox = []
    print("Please, input your numbers in the next template (without brackets):")
    print("( nn1, nn2, nn3,... NNx)")
    number = input("Please enter your numbers: ")
    numberbox = number.split(",")
    convertbox = [int(N) for N in numberbox ]
    return convertbox

numdata = inputdata()
print("-" * 100)
print("Sorted result:")
print("Input length: ", len(numdata))
if len(numdata) <= 10:
    numdata.sort()
else:
    numdata.sort(reverse=True)
print(numdata)
