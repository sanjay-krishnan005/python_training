import guessing_number
while True:
    pin = int(input("Enter the 4 digit Pin: "))
    if pin == 2005:
        print("Your pin is correct")
        break
    else:
        print("Invalid pin, please retype the pin")
guessing_number.game()        