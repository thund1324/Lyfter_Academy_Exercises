note = int(input("Ingrese un número cuantas notas tiene este periodo: "))
approved = 0
disapproved = 0
course_approved = 0
course_disapproved = 0

for number in range(0, note):
    course = float(input("Ingrese la nota de la materia: "))

    if course >= 70 and course <= 100:
        approved += 1
        course_approved += course
    elif course < 70 and course >= 0:
        disapproved += 1
        course_disapproved += course

avarage = (course_approved + course_disapproved) / note 

print(" ")
print("--------------RESULTADOS--------------")
print("Porcentaje de notas: ", avarage, "%")

if approved == 0:
    print("Notas aprovadas: 0")
else:
    avarage_approved = course_approved / approved
    print(f"Aprobados: {approved} | | Porcentaje de aprobados: {avarage_approved}%")

if disapproved == 0:
    print("Notas desaprovadas: 0")
else:
    avarage_disapproved = course_disapproved / disapproved 
    print(f"Desaprobados: {disapproved} | | Porcentaje de desaprobados: {avarage_disapproved}%") 
