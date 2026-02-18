#EXTRAS Error handling
#Extras Receipt
#Extras punch card 

milk = 0.0
cold = 0
drip = 0
pcard = 0 


def inventory_f():
    global milk
    
    milk = float(input("How many gallons of milk are in the fridge?: "))
    latte = int(input("How many lattes do you expect to sell? "))
    
    milk_used = latte * 0.10
    
    if milk_used == milk:
        print("Exact amount of milk.")
    elif milk_used < milk:
        print("Surplus milk available.", milk - milk_used)
    else:
        print("Shortage of milk!", milk_used - milk)
    
    print("Milk needed:", milk_used, "gallons\n")


def transaction_calculator():
    global cold, drip, milk,pcard 
    
    print("1. for Special Cold Brew $6")
    print("2. for Standard Drip $3")
    print("3. exit back to transaction calculator")
    
    user = int(input("Please select an option: "))
    
    if user == 1:
        cold = int(input("How many Special Cold Brews did you buy? "))
        drip = 0
        total = cold * 6
        
    elif user == 2:
        drip = int(input("How many Standard Drip coffees did you buy? "))
        cold = 0
        total = drip * 3
        
    elif user == 3:
        return
    else:
        print("Invalid option")
        return

    
    drinks = cold + drip
    milk_used = drinks * 0.10
    

    # 15% discount if 10 or more drinks
    if drinks >= 10:
        discount = total * 0.15
        total = total - discount
        print("15% bulk discount applied!")

    # Pastry bundle (sub total)
    pastry = input("Would you like to add a Pastry Bundle for a flat rate of $5 extra?(Y/N): ").upper()
    
    if pastry == 'Y':
        total = total + 5
    elif pastry == 'N':
        pass
    else:
        print("please enter N for no or Y for yes")

    # Barista Tax
    btax = total * 0.10
    total = total + btax

    print("Total cost: $", round(total, 2))
    
    paid = float(input("how much did you pay? "))
    
    if paid < total:
        print("insufficient funds")
        print("please pay $", round(total - paid, 2))
    elif paid > total:
        pcard = pcard + 1 

        print("Here is your receipt!")
        if pastry == 'Y':
            print("Pastry fee  - $5")
        print("Barista tax-$",round(btax, 2))
        print("Your Total- $",round(total,2))
        print("your change = $", round(paid - total, 2))
        if pcard >= 5: 
            print("you have earned a free cold brew! Plesae ask your barista to redeem!")
        else:
            print("you are at  ",pcard,"punches. Once you get to 5 you will recieve a free Latte")
    elif paid == total:
        pcard = pcard + 1 
        if pastry == 'Y':
            print("Pastry fee  - $5")
        print("Barista tax-$",round(btax, 2))
        print("Your Total- $",round(total,2))
        print("your change = $", round(paid - total, 2))
        print("you paid the exact amount have a good day")
        if pcard >= 5: 
            print("you have earned a free cold brew! Plesae ask your barista to redeem!")
            pcard = 0
        else:
            print("you are at  ",pcard,"punches. Once you get to 5 you will recieve a free Latte")
            
    else:
        print("please input payment amount")
         

    print()


def menu():
    print("welcome.....")
    print(r""" 
          )  (
         (   ) )
         ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'""")
    print("1. Inventory Check")
    print("2. Transaction Calculator")
    print("3. Exit")
    
    return int(input("Please select an option: "))


while True:
    choice = menu()
    
    if choice == 1:
        inventory_f()
    elif choice == 2:
        transaction_calculator()
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid option\n")
