print("Welcome to HDFC Bank")
restart = ("Y")
chances = 3
balance = 90000
while chances >= 0:
    print (int(input("please enter your 4 digit pin:")))
    pin  = 1234
    if pin == 1234:
        print("entered pin is correct \n")
        while restart not in ("n", "No", "no", "N"):
             print("Please  press 1 for your balance \n")
             print("Please  pre s 2 for your withdrwal \n")
             print("Please  press 3 for your deposite \n")
             print("Please  press 4 for your return card \n")
             option = int(input("what whould u like to choose?"))
             if option == 1:
                 print("\n your balance is Rs", balance)
                 restart = input("would u like to go back?")
                 if restart in ("n", "No", "no", "N"):
                     print("Thank u for banking with us")
                     break
             elif option == 2:
                option2 = ("Y")
                withdrwal = float(input("How much would u like to withdrwal? \n1000rs/2000rs/5000rs/10000rs/15000rs for other enter 1:"))
                if withdrwal in [1000, 2000, 5000, 10000, 15000]:
                    balance = balance - withdrwal
                    print("your balence is now Rs \n",  balance)
                    restart = input("what would you like to do?")
                    if restart in ("n", "No", "no", "N"):
                        print("Thank u for banking with us")
                        break
                elif withdrwal != [1000, 2000, 5000, 10000, 15000]:
                    print("invalid amount, please re-try \n")
                    restart = ("Y")         

                elif withdrwal == 1:
                    widrwal = float(input("Enter desired amount here:"))     

             elif option == 3:
                 deposite = float(input("How much amount would u like to deposite?"))
                 balance = balance + deposite
                 print("\n your balance is now Rs", balance)
                 restart = input("would you like to go bake?")
                 if restart in ("n", "No", "no", "N"):
                     print("Thank you for banking with us")
                     break
            
             elif option == 4:
                 print("Please wait while your card is returned \n")
                 print("Thank you for banking with us")
                 break
            
             else:
                 print("Please enter correct pin number \n")
                 restart = ("Y")
        
    elif pin != ('1234'):
        print("Incorrect pin")
        chances = chances - 1
        if chances == 0:
            print("\n Pin tries exceeded, please contact with nearest branch or contact with us on support@HDFC.co")
            break

    
