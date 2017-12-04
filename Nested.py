withdraw = int(input("How much do you want to withdraw "))
balance = 1000

if balance >= withdraw:
    confirm = input("Are you sure? ")
    if confirm == "Yes":
        print("Here is your money.")
else:
    print("Sorry, you don't have enough money.")
    
