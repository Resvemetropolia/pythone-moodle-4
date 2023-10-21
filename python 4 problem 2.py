INCHES = 2.54
while True:
    inches = float(input("Enter a length in inches (negative to quit): "))
    if inches < 0:
        print("Program ended.")
        break
    centimeters = inches * INCHES
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters")