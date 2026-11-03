class NPC:
    def __init__(self, jmeno:str, energie:int):
        self.jmeno = jmeno
        self.energie = energie    
        pass
    def predstav_se(self):
        return f"Zde NPC {self.jmeno}."
    
    def vyraz_na(self, cil:str):
        if self.energie >= 10:
            self.energie -= 10
        #self.energie = self.energie - 10
            return f"{self.jmeno} se přesunul na {cil}. Zbývá energie: {self.energie}"
        else:
            return f"{self.jmeno} nemá dostatek energie na přesun!"
        
class CHODEC(NPC):
    def __init__(self,jmeno, energie,domovska_ctvrt:str):
        super().__init__(jmeno, energie)
        self.domovska_ctvrt = domovska_ctvrt

    def predstav_se(self):
        return f"Zde chodec {self.jmeno}, rajón {self.domovska_ctvrt}. Yo yo so whassup my mannn"
    
    def vyraz_na(self, cil: str):
        if self.energie >= 30:
            self.energie -= 30
            return f"Zahajuji náročný pěší chod na cíl {cil}. Zbývá energie: {self.energie}."
        else:
            return f"Nikam nemůže. Sorráč"
        
class POLICI(NPC):
    def __init__(self, jmeno, energie, zbran_tasena: bool = False):
        super().__init__(jmeno,energie)
        self.zbran_tasena = zbran_tasena
    
    def predstav_se(self):
        return f"Zde policista LSPD {self.jmeno}. baguette baguette"
    
    def tas_nebo_skryj_zbran(self):
        self.zbran_tasena = not self.zbran_tasena
        if self.zbran_tasena:
            return f"{self.jmeno}: Zbraň tasená."
        else:
            return f"{self.jmeno}: Zbraň skrytá v pouzdře."
        
class RIDIC(NPC):
    def __init__(self, jmeno, energie):
        super().__init__(jmeno,energie)
        self.cestujici = []

    def naber_cestujici(self, jmeno_cestujiciho):
        self.cestujici.append(jmeno_cestujiciho)
        return f"Do autobudu řidiče {self.jmeno} nastoupili cestující: {jmeno_cestujiciho}!"
        pass

npc = NPC("Johan Tichošlápek", 15)
print(npc.predstav_se())
print(npc.vyraz_na("Srbsko"))
print("="*40)

jurij = CHODEC("Jurij Gagarin", 40, "Grove street")
print(jurij.predstav_se())
print(jurij.vyraz_na("čtvrť Ballas"))
print(jurij.vyraz_na("gunshop"))
print("="*40)

fizl = POLICI("Burbon žu Vás", 100)
print(fizl.predstav_se())
print(fizl.tas_nebo_skryj_zbran())
print(fizl.tas_nebo_skryj_zbran())
print(fizl.tas_nebo_skryj_zbran())
print("="*40)

bus = RIDIC("Trevor z Taverny", 20)
print(bus.naber_cestujici("Doktor Advokát"))
print(bus.naber_cestujici("Zemana Advokátská"))
print(bus.naber_cestujici("Majhor Mujir"))
print(bus.naber_cestujici("Lokyn Lock-in"))
print(bus.cestujici)
print("="*40)

skupina_npc = [npc,jurij,fizl]
spolecny_cil = "Vice City"

for postava in skupina_npc:
    #for led in leds btw..... soráč já zapomněla co jsme minulý rok dělali laughing emoji
    print(postava.predstav_se())
    print(postava.vyraz_na(spolecny_cil))
    print("="*40)