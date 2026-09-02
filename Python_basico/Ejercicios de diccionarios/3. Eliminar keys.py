no_necessary = ['zip_code', 'apart_number']
info = {
    "name" : "Gilberto",
    "age" : 25,
    "state" : "Florida",
    "zip_code" : 14052,
    "apart_number" : 123
}

for key in no_necessary:
    info.pop(key)

print(info)