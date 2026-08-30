def sum_of_list(number_list):
    sum = 0     #Initialize the value of sum
    for i in number_list:
        sum += i
    return sum
        
number_list = [1, 2, 3, 4, 5]
result = sum_of_list(number_list) #Assign the function's return value to result.
print(f"The sum of the numbers in the list is: {result}")