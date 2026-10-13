hotel = {
    "name": "Hotel California",
    "number_of_stars": 5,
    "rooms": [
        {
            "number": 3,
            "floor": 1,
            "price_per_night": 25.00
        },
        {
            "number": 4,
            "floor": 1,
            "price_per_night": 30.00
        }
    ]
}

print("--------Información del hotel--------")
print(f"Nombre del hotel: {hotel['name']}")
print(f"Número de estrellas: {hotel['number_of_stars']}")
print("------------------------")

for room in hotel['rooms']:
    print(f"Número de habitación: {room['number']}")
    print(f"Piso: {room['floor']}")
    print(f"Precio: {room['price_per_night']}")
    print("------------------------")