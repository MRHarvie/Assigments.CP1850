
print(60*"=") # Heading liner
print("Shipping calculator") # Heading for program


while True:
    print(60*"=")
    cost = float(input("Cost of items ordered:\t"))
    ship_cost = 0                                   # Initial shipping cost to start
    program = True
    
    
    if cost <= 0:
        print("You must enter a positive number. Please try again.")
        cost = float(input("Cost of items ordered:\t"))
        # Error message if user types negative number.
        
    if cost > 1 and cost <=30:
            shipping_cost = 5.95
            print("Shipping total: \t\t5.95")
            print("Total cost:\t\t\t\t{:.2f}".format(cost + shipping_cost))
    
    if cost >= 30 and cost <= 49.99:
            shipping_cost = 7.95
            print("Shipping total: \t\t7.95")
            print("Total cost:\t\t\t\t{:.2f}".format(cost + shipping_cost))
            
    if cost >= 50 and cost <= 74.99:
            shipping_cost = 9.95
            print("Shipping total: \t\t9.95")
            print("Total cost:\t\t\t\t{:.2f}".format(cost + shipping_cost))
        
    if cost >= 75:
            shipping_cost = 0
            print("Shipping total: \t\t\t0")
            print("Total cost:\t\t\t\t{:.2f}".format(cost + shipping_cost))
            
    if input("\nContinue? (y/n): ").lower() != "y":
        print("="*60)
        print("Bye!")
        break
        
        #Calculations for the shipping costs for each value.
        # 0-30 = 5.95
        # 30-49.99 = 7.95
        # 50-74.99 = 9.95
        # Above 75 = Free
        