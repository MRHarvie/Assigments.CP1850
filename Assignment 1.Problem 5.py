square_calculator = True
while square_calculator:
    start_number = int(input("Starting Number:\t"))
    end_number = int(input("End Number:\t"))
    if start_number > end_number:
        print("Please enter a valid range of numbers.")
        square_calculator = False
    else:
        print("Number\t\tSquare\t\t Cube")
        print("======\t\t======\t\t ======")
# Iterate through the range and calculate squares and cubes
        for num in range(start_number,end_number + 1):
            square = num ** 2
            cube = num ** 3
            print("{}\t\t\t{}\t\t {}".format(num,square,cube))
            square_calculator = False
    

