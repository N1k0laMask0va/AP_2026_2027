import random
from datetime import datetime

class Animal:
    def __init__(self, species:str, name:str, bYear:int, checkupY:int, energy = 100):
        self.species = species
        self.name = name
        self.bYear = bYear
        self.checkupY = checkupY
        self.energy = energy

    def __str__(self):
        return f"{self.species} s jménem {self.name}, narozen roku  {self.bYear} - energie {self.energy}%"
    
    def play(self):
        usage = random.randint(5,20)
        if self.energy >= usage:
            self.energy -= usage
            return f"Zvíře {self.species}, jménem {self.name}, spotřeboval při hře {usage} % energie a a zbývá mu {self.energy} % energie."
        else:
            return f"Zvíře {self.species}, jménem {self.name}, je moc unavený. Potřebuje {usage} % energie a má pouze {self.energy} % energie."
        #pass
    
    def feed(self):
        plny = 100 - self.energy
        self.energy = 100
        return f"Zvíře {self.species}, jménem {self.name}, bylo nakrmeno a doplnil {plny} % energie."
    
    def vetcheck(self):
        if self.checkupY < datetime.now().year:
            return f"Zvíře {self.species}, jménem {self.name}, musí jít k veterináři - platnost prohlídky skončila v roce {self.checkupY}."
        else:    
            rozdil = self.checkupY - datetime.now().year
            return f"Zvíře {self.species}, jménem {self.name}, má prohlídku v pořádku. Další prohlídka bude za následujíciích počet let: {rozdil}"

fenek = Animal("Fenek", "Sunamono", 2016, 2026, 85)
print(fenek)
print(fenek.play())
print(fenek.feed())
print(fenek.vetcheck())
print("----"*40)

krysarik = Animal("Pražský krysařík", "Kejtyna", 2018, 2025, 100)
print(krysarik)
print(krysarik.play())
print(krysarik.feed())
print(krysarik.vetcheck())
print("----"*40)

kocour = Animal("Kočka domácí", "Kocour", 2016, 2020, 75)
print(kocour)
print(kocour.play())
print(kocour.feed())
print(kocour.vetcheck())
print("----"*40)

surikata = Animal("Surikata", "Johan Teplický", 2010, 2015, 60)
print(surikata)
print(surikata.play())
print(surikata.feed())
print(surikata.vetcheck())
print("----"*40)

class Zoo:
    def __init__(self,nazev):
        self.nazev = nazev
        self.animals = []

    def addanimal(self, animal: Animal):
        self.animals.append(animal)
        print(f"Do {self.nazev} bylo přidano zvíře: {animal.species}, aka {animal.name}.") 
