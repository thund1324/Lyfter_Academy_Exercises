first_list = [1, 2, 3, 4, 21, 4, 3, 44, 66 ,8, 79 ,9 ,5, 3, 5, 7, 3, 0,8 ,4 ,8 ,6 ,5 ,4 ,7 , -61,-58, 0, 8, 16, 181, 42, 7]
minor = 0

for index1, index2 in enumerate(first_list):
    print(index2)
    if minor == 0 or index2 < minor:
        minor = index2

print(f"El numero menor que su indice es: {minor}")