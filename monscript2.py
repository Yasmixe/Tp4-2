dictio = [
    {"matricule": 1000, "name": "john", "username": "doe", "note": 15},
    {"matricule": 1000, "name": "john", "username": "doe", "note": 8},
    {"matricule": 1000, "name": "bob leponge", "username": "doe", "note": 15},
]


def estadmissible(i):
    return i["note"] >= 10


for i in dictio:
    if estadmissible(i) == True:
        print(i["name"])
