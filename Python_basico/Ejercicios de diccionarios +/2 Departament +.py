employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

groups = {}

for employees in employees: 
    same_dept = employees["department"]
    name = employees["name"]
    if same_dept not in groups:
        groups[same_dept] = []
    
    groups[same_dept].append(name)

print(groups)