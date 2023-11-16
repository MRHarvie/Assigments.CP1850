# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:29:55 2023

@author: harv3
"""

def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def display_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
    

def main():
    print("Prime Number Checker\n")
    while True:
        num = int(input("Please enter an integer between 1 and 5000: "))
        if num <= 0:
            print("Please select a number between 1 and 5000.")
        elif num >= 5000:
            print("Please select a number between 1 and 5000.")
        else:
    
            if prime(num):
                print(f"{num} is a prime number.")
            else:
                                    
                    print(f"{num} is NOT a prime number.")
                    factors = display_factors(num)                    
                    print(f"The factors of {num} are: {factors}")
            if input("\nContinue? (y/n)     ") != 'y' and 'Y':
                break
                print("Bye!")
                

if __name__ == "__main__":
    main()





