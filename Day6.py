#single line statement
x = 54
y = 105

if x < y: print("y is greater than x")

#if, elif and else
value1 = 54758
value2 = 57758
if value2 < value1:
    print("value1 is greater than value2 ")
elif value1 == value2:
     print("value1 is equal to value2")
else:
     print("value1 is greater than value2")

#continue statement nested if 
S = 50
if S > 15:
    print("S is Above 15")
    if S > 30:
            print("S is also above 30!") 
    else:
        ("not above 30!")

#if statement on string
name = input("EnterName:")
if name == "Sam":
    print("Hello Sam How are u!")
    print("Saw you here after long time")
else:
    print("Hey Nice to see you here")
    print("have a great day")

#if, elif and else statement in string 
name1 = input("Enter name1:")
name2 = input("Enter name2:")
if name1 == "varry":
    print("Nice to See u again")
    print("Enjoy python")
    if name2 == "kedar":
        print("Hey kedar good morning")
elif name1 == name2:
    print("Both names are similar")
else:
    print("Hey are u new members")


#if-elif
num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))
if num1 > num2:
    print("biggest number is:", num1)
elif num1 < num2:
    print("biggest number is:", num2)