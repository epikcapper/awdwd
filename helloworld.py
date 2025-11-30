print("Welcome to the CS 11 custom calculator!")
print()

choice = input("Do you want to do addition or subtraction? ")

if choice == "addition":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("The answer is:", result)

elif choice == "subtraction":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("The answer is:", result)

else:
    print("Invalid choice, try again.")
