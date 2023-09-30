print("Tip Calculator\n")

meal_cost = float(input("Cost Of Meal:\t"))

print("\n15%")
tip_amnt15 = meal_cost * .15
ttl_amnt15 = meal_cost * 1.15
print("Tip Amount:\t{:.2f}".format(tip_amnt15))
print("Total Amount:\t{:.2f}\n".format(ttl_amnt15))

print("20%")
tip_amnt20 = meal_cost *.20
ttl_amnt20 = meal_cost *1.20
print("Tip Amount:\t{:.2f}".format(tip_amnt20))
print("Total Amount:\t{:.2f}\n".format(ttl_amnt20))

print("25%")
tip_amnt25 = meal_cost *.25
ttl_amnt25 = meal_cost *1.25
print("Tip Amount:\t{:.2f}".format(tip_amnt25))
print("Total Amount:\t{:.2f}\n".format(ttl_amnt25))
