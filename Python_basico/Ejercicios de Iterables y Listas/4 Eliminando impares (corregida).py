first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(first_list)


second_list = []

for i in first_list:
    if i % 2 == 0:
        second_list.append(i)

print(f"Números pares: {second_list}")