wants_coffee = False
while not wants_coffee:
    ask = input("Heya Developer, Do you want wanna drink something hot? 'y'/'n'\n")
    if ask == 'y' or ask == 'n':
        wants_coffee = True
    else:
        print("Please either choose 'y' for yes or 'n' for no.")


if ask == 'y':
    def coffee_app():
        user_chose_coffee = False
        while not user_chose_coffee:
            user_chosen_coffee = input("What would you like? (espresso/latte/cappuccino):\n").lower()

            if user_chosen_coffee == 'espresso' or user_chosen_coffee == 'latte' or user_chosen_coffee == 'cappuccino':
                user_chose_coffee = True

        price_drinks = {"espresso": 2.50, "latte": 3, "cappuccino": 4}

        print(f"You chose {user_chosen_coffee}, it's price is of {price_drinks[user_chosen_coffee]}\n")

        user_quarters = int(input("Amount of quarters:  "))
        user_dimes = int(input("Amount of dimes:  "))
        user_nickles = int(input("Amount of nickles:  "))
        user_pennies = int(input("Amount of pennies:  "))

        user_quarters *= .25
        user_dimes *= .1
        user_nickles *= .05
        user_pennies *= .01
        total_user_paid = user_quarters + user_dimes + user_nickles + user_pennies
        print(f'total user paid:{total_user_paid}')
        print(f'total drink price:{price_drinks[user_chosen_coffee]}')

        if total_user_paid >= price_drinks[user_chosen_coffee]:
            print(f"Here's your {user_chosen_coffee}☕. Enjoy!")
            change = total_user_paid - price_drinks[user_chosen_coffee]
            if change > 0:
                print(f"And don't forget your change of ${round(change,2)}. Have a Good Day!")
        else:
            print("Sorry, that's not the right amount!")
            try_again = input("Wanna buy again? 'y' for yes any other keyword to exit the program.")

            if try_again == 'y':
                coffee_app()


    coffee_app()


