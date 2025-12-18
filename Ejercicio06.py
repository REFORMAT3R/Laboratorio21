import json
equipos = [
    {
        "nombre": "Real Madrid",
        "pais": "España",
        "nivelAtaque": 92,
        "nivelDefensa": 88
    },
    {
        "nombre": "Manchester City",
        "pais": "Inglaterra",
        "nivelAtaque": 94,
        "nivelDefensa": 85
    },
    {
        "nombre": "Bayern Múnich",
        "pais": "Alemania",
        "nivelAtaque": 90,
        "nivelDefensa": 87
    },
    {
        "nombre": "PSG",
        "pais": "Francia",
        "nivelAtaque": 91,
        "nivelDefensa": 82
    }
]

json_equipos = json.dumps(equipos, indent=4, ensure_ascii=False)

print(json_equipos)