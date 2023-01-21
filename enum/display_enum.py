from enum import Enum

class Country(Enum):
    India=100
    Pakistan=0
    Afghanistan=2

for i in sorted(Country):
    print(i.name)