
class VesmirnaLod:
    def __init__(self, nazev:str, palivo:int):
        self.nazev = nazev
        self.palivo = palivo

    def predstav_se(self):
        return f"Zde loď {self.nazev}."
    def let_na(self, cil:str):

        if self.palivo >= 10:
            self.palivo -= 10
            return f"Zahajuji podsvětelný let na {cil}. Zbývá paliva: {self.palivo}%."
        else:
            return f"Nedostatek paliva pro let!"
        
class PozemskyKriznik(VesmirnaLod):
    def __init__(self, nazev, palivo, velitel:str):
        self.velitel = velitel
        super().__init__(nazev, palivo)

    def predstav_se(self):
        return f"Zde pozemský křižník {self.nazev}, velí {self.velitel}."
    
    def let_na(self, cil:str):

        if self.palivo >= 30:
            self.palivo -= 30
            return f"Otevírám hyperprostorové okno k cíli {cil}. Zbývá: {self.palivo}%."
        else:
            return f"Chyba. Nedostatek paliva. Sebedestrukce za 3...2...1..."
        
class PuddleJumper(VesmirnaLod):
    def __init__(self,nazev,palivo, maskovani_aktivni:bool):
        super().__init__(nazev,palivo)
        self.maskovani_aktivni = maskovani_aktivni 

    def predstav_se(self):
        return f"Zde antický Jumper {self.nazev}."
    
    def let_na(self, cil:str):
        return super().let_na(cil)
    
    def zamaskuj_se(self):
        if self.maskovani_aktivni == True:
            self.maskovani_aktivni = False
            return f"Jumper 1: Maskování DEAKTIVOVÁNO."
        else:
            self.maskovani_aktivni = True
            return f"Jumper 1: Maskování AKTIVOVÁNO!"
        
class Teltak(VesmirnaLod):
    def __init__(self, nazev, palivo, naklad:str):
        super().__init__(nazev,palivo)
        self.naklad = naklad

    def predstav_se(self):
        return super().predstav_se()
    
    def let_na(self, cil):
        return super().let_na(cil)
    
    def naloz_naklad(self, polozka:str):
        return f"Na loď {self.nazev} bylo naloženo: {polozka}."
    
Autob = VesmirnaLod("Auto126B", 5)
print(Autob.predstav_se())
print(Autob.let_na("Měsíc"))

Vyprava = PozemskyKriznik("Křížová výprava", 20, "Jahmur Želnický XII.")
print(Vyprava.predstav_se())
print(Vyprava.let_na("Měsíc"))

Skokan = PuddleJumper("Skokan obecný", 100, False)
print(Skokan.predstav_se())
print(Skokan.let_na("Měsíc"))
print(Skokan.zamaskuj_se())

Tyran = Teltak("Tyran všech tyranů", 34, "Banány")
print(Tyran.predstav_se())
print(Tyran.let_na("Měsíc"))
print(Tyran.naloz_naklad("Voda"))