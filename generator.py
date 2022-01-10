def createCalculator(maxVal):
    f = open("calculator.py", "w+")

    #Gets user input for numbers and operators
    f.write('num1 = input("Enter the first value: ") \n')
    f.write('operator = input("Enter the operator: ") \n')
    f.write('num2 = input("Enter the second value: ") \n')

    #Create all operations
    for i in range(maxVal):
        for j in range(maxVal):
            f.write(f'if num1 == "{i}" and num2 == "{j}" and operator == "+": \n')
            f.write('\t print("' + str(i + j) + '") \n')
            f.write(f'if num1 == "{i}" and num2 == "{j}" and operator == "*": \n')
            f.write('\t print("' + str(i + j) + '") \n')

    f.close()