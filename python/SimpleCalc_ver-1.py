# SEDICOMM University, PCAP - Programming Essentials in Python
# Author        : Zibnitskii Aleksandr
# Date          : 11/04/2020
# Description   : Console Simple Caclulator ver.1
#
# Task          : Написать программу калькулятор, который будет запрашивать 2
#                 значения и что с ними сделать (+,-,/,*). Решение должно сохраняться,
#                 и вы должны дальше с ним работать. Например есть два числа 5,25 и +,
#                 то будет 30, и дальше я ввожу 10 и отнимаю его и так далее. 

save_input = []
first_iter = False

def InputFirstNum():
    a = float(input("Input the first number: "))
    return a

def InputSecondNum():
    b = float(input("Input the second number: "))
    return b

def PrintAction():
    print("-"*36)
    print("Select a math action [ +, -, * , / ]")
    print("or input 'x' - for exit")

def ActionSelect():
    usersel = input("Your choice: ")
    return usersel

def DoResult(user_input, user_select):
    print("-"*36)
    a = float(user_input[0])
    b = float(user_input[1])
    result = 0
    if user_select == "+":
        result = a + b
    elif user_select == "-":
        result = a - b
    elif user_select == "*":
        result = a * b
    else:
        result = a / b
    print(a,user_select,b,"=",round(result, 2))
    save_input[0] = round(result, 2)
    print("-"*36,"\n")

while True:
    if not first_iter:
        save_input.append(InputFirstNum())
        save_input.append(InputSecondNum())
        first_iter = True
    else:
        print("The first number is: ", save_input[0])
        save_input[1] = InputSecondNum()
    PrintAction()
    user_choice = ActionSelect()
    if ((user_choice == "+") or (user_choice == "-") or (user_choice == "*") or (user_choice == "/")):
        DoResult(save_input, user_choice)
    else:
        print("Thank's for your cooperation! Good bye")
        break
    

