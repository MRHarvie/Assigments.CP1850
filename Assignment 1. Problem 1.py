print("Letter Grade Converter")

program_running = True
while program_running:
    numerical_grd = int(input("\nEnter numerical grade:  "))
    if numerical_grd >= 88 and numerical_grd <= 100:
        numerical_grd = "A"
    elif numerical_grd >= 80 and numerical_grd <= 87:
        numerical_grd = "B"
    elif numerical_grd >= 67 and numerical_grd <= 79:
        numerical_grd = "C"
    elif numerical_grd >= 60 and numerical_grd <= 66:
        numerical_grd = "D"
    else:
        numerical_grd = "F"
    print("Letter Grade: \t{}".format((numerical_grd)))
    if input("\nContinue? (y/n)     ") != 'y' and 'Y':
        break

print("\nBye!")