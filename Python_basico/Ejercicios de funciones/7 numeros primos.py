def check_prime_number(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

def add_prime_number(numbers_list):
    prime_number_list = []
    
    for number in numbers_list:
        if check_prime_number(number):
            prime_number_list.append(number)
    
    return prime_number_list


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(add_prime_number(numbers_list))