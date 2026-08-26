number = 1
while number <= 1000:
    if number%3 == 0:
        print(number)
#In this condition, no need to convert number to string, because print() do automatic conversion. Only we do some character concatenation output.
    number = number + 1