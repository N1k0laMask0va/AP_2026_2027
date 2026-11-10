#from random import randint
import random
from datetime import datetime

class Car:
    def __init__(self, brand:str, model:str, year:int, stkyear:int, palivo:int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.stkyear = stkyear
        self.palivo = palivo
        

    def __str__(self):
        #už nemusíme volat fuknce jako představ se, atd. --> metoda, která se volá jako zakládní pro výpis vlastnosti! 
        return f"{self.brand}: {self.model} ({self.year}), palivo: {self.palivo}%"
    
    def move(self):
        usage = random.randint(5,20)
        if self.palivo >= usage:
            #self.fuel = self.fuel - usage
            self.palivo -= usage
            return f"{self.brand}: {self.model} spotřeboval {usage}% a zbývá mu {self.palivo}%"
        else:
            return f"{self.brand}: {self.model} by do cíle nedojel. Potřebuje {usage}% paliva, ale má jenom {self.palivo}%"
        
    def fullfill(self):
        filled = 100 - self.palivo
        self.palivo = 100
        return f"{self.brand}: {self.model} natankoval {filled}% paliva!"  

    def STK(self):
        if self.stkyear < datetime.now().year:
            return f"{self.brand}: {self.model} musí na technickou. Technická skončila v roce {self.stkyear}."
        else:
            return f"{self.brand}: {self.model} má technickou v pořádku. Na technickou bude muset jít za následujících počet let: {self.stkyear - datetime.now().year}"
        pass 
    
achto = Car("Škoda auto", "Octavia 3", 2016, 2026, 85)
achto2 = Car("ŽumplerPr ", "D.", 1885, 2021, 10)
achto3 = Car("Banán", "banán", 2010, 2014, 3)

print(achto)
print(achto.move())
print(achto.fullfill())
print(achto.STK())
print("--------------------------"*3)
print(achto2)
print(achto2.move())
print(achto2.fullfill())
print(achto2.STK())
print("--------------------------"*3)
print(achto3)
print(achto3.move())
print(achto3.fullfill())
print(achto3.STK())
print("--------------------------"*3)


class Garage:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def addcar(self, car: Car):
        self.cars.append(car)
        return f"Do garáže {self.name} bylo přidáno auto: {car.brand}: {car.model}."
    def showCars(self):
        if len(self.cars)==0:
            print(f"Garáž {self.name} je prázdná!")
        else:
            print(f"Auta v garáži {self.name}:")
            for car  in self.cars:
                print("--->",car)

    def oldestcar(self):
        if len(self.cars) == 0:
            return None
        else: 
            oldest = min(self.cars, key= lambda a: a.year)
            return oldest
    
    def avgpalivo(self):
        if len(self.cars) == 0:
            return 0
        return sum(car.palivo for car in self.cars) / len(self.cars)
    
garage = Garage("Šusterdeník AU-Umbrella")
print(garage.addcar(achto))
print(garage.addcar(achto2))
print(garage.addcar(achto3))

oldest = garage.oldestcar()
garage.showCars()
if oldest:
    print(f"Nejstarší auto v garáži je {oldest.brand}: {oldest.model} {(oldest.year)}")

print(f"{garage.avgpalivo(): .1f}%")

print(garage.cars[2].move())

for brambora in garage.cars:
    print(brambora.STK())