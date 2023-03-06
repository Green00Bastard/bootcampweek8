# INFINITE LOOP TO KEEP THE PROGRAM RUNNING UNITIL THE USER CHOOSES TO END IT
while True:
    #MAIN MENU OPTIONS
    print(6 * ("<") + ("Welcome to dynamic menu program") + 6 * (">"))
    print(2 * ("--") + ("1: ") + ("START PROGRAM") + 2 * ("--"))
    print(2 * ("--") + ("2: ") + ("END PROGRAM") + 2 * ("--"))
    #USER CHOICE
    choice = input("Select an option: ")
    #SUB_MENU LOOP WITH OPTIONS
    if choice == "1":
        while True:
            print(6 * ("<") + ("Sub-menu") + 6 * (">"))
            print(2 * ("--") + ("1: ") + ("Add") + 2 * ("--"))
            print(2 * ("--") + ("2: ") + ("Subtract") + 2 * ("--"))
            print(2 * ("--") + ("3: ") + ("Times") + 2 * ("--"))
            print(2 * ("--") + ("4: ") + ("Divide") + 2 * ("--"))
            print(2 * ("--") + ("5: ") + ("Return to Main") + 2 * ("--"))
            
            sub_choice = input("Select an option: ")
            #CONVERT USER CHOICE TO INTEGER
            try:
                sub_choice = int(sub_choice)
                
                if sub_choice == 1:
                    print("You chose Add")
                    print("input two numbers for addition below: \n")
                    num1 = int(input("ENTER YOUR FIRST NUMBER: \n"))
                    num2 = int(input("ENTER YOUR SECOND NUMBER: \n"))
                    print(num1 + num2)
                elif sub_choice == 2:
                    print("You chose Subtract")
                elif sub_choice == 3:
                    print("You chose Times")
                elif sub_choice == 4:
                    print("You chose Divide")
                elif sub_choice == 5:
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid option, please try again.")
                    
            except ValueError:
                print("Invalid option, please try again.")
                
    elif choice == "2":
        print("Ending program...")
        break
    
    else:
        print("Invalid option, please try again.")
