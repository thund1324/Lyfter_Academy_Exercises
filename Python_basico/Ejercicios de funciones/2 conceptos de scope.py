def first_function():
    greeting = "Hello world"
    print(greeting)


first_function()
#Aqui queria acceder directamente a la variable "greeting", pero no pude debido a que no se definio como una variable global
#print(greeting)

num2 = 14

def second_list():
    global num2
    num2 = 5
    


second_list()
print(num2)