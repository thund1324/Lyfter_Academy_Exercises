def sum_all_the_list(numbers_list):
    total = 0
    for number in numbers_list:
        total += number
    return total


numbers_list = [14, 15, 69]
print(f"Total de la suma: {sum_all_the_list(numbers_list)}")