while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break

    if user_input in ("+", "-"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == "+":
            print("Result:", num1 + num2)
        elif user_input == "-":
            print("Result:", num1 - num2)
    else:
        print("Invalid input")






