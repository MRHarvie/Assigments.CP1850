quarter_value = 25
dime_value = 10
nickle_value = 5
cent_value = 1
calculator_running = True
while calculator_running:
    cents = int(input("Enter Number Of Cents (0-99):\t"))
    
    quarters = cents//quarter_value
    cents %= quarter_value

    dimes = cents//dime_value
    cents %= dime_value

    nickles = cents//nickle_value
    cents %= nickle_value

    pennies = cents
    cents %= cent_value
    
    print("Quarter:  {}".format(quarters))
    print("Dimes:  {}".format(dimes))
    print("Nickles:  {}".format(nickles))
    print("Pennies:  {}".format(pennies))
    
    if input("\nContinue? (y/n): ").lower() != "y":
        break

print("Bye!")