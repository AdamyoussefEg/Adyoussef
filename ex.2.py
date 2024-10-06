#مشروع اله حسابيه
from pystyle import *
print(Box.Lines(" [+] Learn python with Adam [+] "))
Write.Print(" [+] This program for Calculator. \n",Colors.blue_to_red,interval=0.1)
print(Box.DoubleCube("Example [2]"))

while True:
    number1 = int(Write.Input(" [+] Write fist number : ",Colors.blue_to_green,interval=0.1) )
    operator = Write.Input("Write Math code : ",Colors.red_to_yellow,interval=0.1)
    number2 = int(Write.Input(" [+] Write Secound number : ",Colors.green_to_blue,interval=0.1) )
    if operator == "+":
        Write.Print("[+] The result is : \n",Colors.blue_to_red,interval=0.1)
        print(number1+number2)
        input("\n press any key to exit ... ")

        break
    elif operator == "-":
        Write.Print("[+] The result is : \n",Colors.blue_to_red,interval=0.1)
        print(number1-number2)
        input("\n press any key to exit ... ")
        break
    elif operator == "/":
        Write.Print("[+] The result is : \n",Colors.blue_to_red,interval=0.1)
        print(number1+number2)
        input("\n press any key to exit ... ")
        break
    elif operator == "*":
        Write.Print("[+] The result is : \n",Colors.blue_to_red,interval=0.1)
        print(number1*number2)
        input("\n press any key to exit ... ")
        break
    elif operator == "**":
        Write.Print("[+] The result is : \n",Colors.blue_to_red,interval=0.1)
        print(number1**number2)
        input("\n press any key to exit ... ")
        break
    elif operator == "//":
        Write.Print("[+] The result is : \n",Colors.blue_to_red,interval=0.1)
        print(number1//number2)
        input("\n press any key to exit ... ")
        break
    elif operator == "%":
        Write.Print("[+] The result is : \n",Colors.blue_to_red,interval=0.1)
        print(number1%number2)
        input("\n press any key to exit ... ")
        break
    elif operator == "^":
        Write.Print("[+] The result is : \n",Colors.blue_to_red,interval=0.1)
        print(number1^number2)
        input("\n press any key to exit ... ")
        break
    else:
        Write.Print("\n [-] please only just write: + , - , / , * , ** , // , % , ^  ." )
        


