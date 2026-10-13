def first_function(sentence):
    sentence_list = sentence.split("-")
    sentence_list.sort()
    return "-".join(sentence_list)


sentence = input("Ingrese una oración separada por guiones: ")
print("----------------")
print(first_function(sentence))