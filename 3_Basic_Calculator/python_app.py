# Define the functions needed: add, sub, mul, div
# Print the options to the user
# Ask for values
# Call the functions
# While loop to continue the program untill the user wants to exit

def add(a,b):
    answer = a + b 
    print(str(a) +'+'+ str(b)+ "=" + str(answer))

def sub(a,b):
    answer = a - b 
    print(str(a) + '-' + str(b)+ "=" + str(answer))

def mul(a,b):
    answer = a * b 
    print(str(a) + '*' + str(b)+ "=" + str(answer))

def div(a,b):
    answer = a / b 
    print(str(a) + '/' + str(b)+ "=" + str(answer))


while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ")

    if choice == 'a' or choice == 'A':
        print("Addition")
        a = int(input("Enter first Number"))
        b = int(input("Enter the second number"))
        add(a,b)

    elif choice == 'b' or choice == 'B':
        print("Substraction")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the Second number: "))
        sub(a,b)

    elif choice == 'c' or choice == 'C':
        print("Multiplication")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the Second number: "))
        mul(a,b)

    elif choice == 'D' or choice == 'd':
        print("Division")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the Second number: "))
        div(a,b)

    elif choice == "e" or choice =='E':
        print("Program ended")
        quit()

    else:
        print("Choose Valid Option")
        
