def calculator():
    print("======simple calculator======")
    print("choose operation:")
    print("addition + ")
    print("subraction - ")
    print("multiplication * ")
    print("division / ")

    loop=""
    while loop!="q":
        try:
            a=int(input("Enter the A value ="))
            b=int(input("Enter the B value ="))
            operator=input("enter the operator (+,-,*,/):")
            match operator:
                case '+':
                    result = a + b
                case '-':
                    result = a - b
                case '*':
                    result = a * b
                case '/':
                    result = a / b
                case _:
                    result = "Operator not recognized"

            print("Result:", result)
            loop=input("Enter q to quite")
   
        except valueError as e:
            print("Error",)
calculator()
