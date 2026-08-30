def filter_even_numbers(original_list):
    filtered_list = []
    for i in original_list:
        if i % 2 == 0:
            filtered_list.append(i)
    return filtered_list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(original_list)
print("Original list:", original_list)
print("List with even numbers only:", filtered_list)