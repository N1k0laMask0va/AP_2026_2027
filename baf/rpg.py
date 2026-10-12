#ahoj jmenuji se micheal jackson ano jsem tom opravdu ja, posli mi 566 dolaru pls. hee hee
import random

class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi
    def predstav_se(self):
        return f"Jmenuji se {self.jmeno} z linie šlechty, tzv. Přemyslovců. Mé aktuální zdraví je {self.zdravi}. Nebojím se padnout pro tuto vlast."
    def utok(self, utok = 0):
        return f"V tento moment nejsem dostatečně silný, můj útok je {utok}."

class Rytir(Postava):
    def __init__(self,jmeno,zdravi,brneni):
        super().__init__(jmeno,zdravi)
        self.brneni = brneni
        pass
    def predstav_se(self):
        return f"Jmenuji se {self.jmeno} z linie šlechty, tzv. Přemyslovců. Mé aktuální zdraví je {self.zdravi}. Nebojím se padnout pro tuto vlast."
    def utok(self):
        sila = (random.randint(10,20))
        return f"Zaútočil jsem na nepřítele, můj útok na něj je {sila}. Nepřítel zemřel."
        #return f"Zaútočil jsem na nepřítele, můj útok na něj je {self.utok}. Nepřítel utekl."
    def zablokuj(self):
        return f"Já, {self.jmeno}, jsem v boji o život dokázal zablokovat útok mým brněním ze {self.brneni}."
        
class Mag(Postava):
    def __init__(self, jmeno, zdravi, mana):
        super().__init__(jmeno,zdravi)
        self.mana = mana
    def predstav_se(self):
        return f"Jmenuji se {self.jmeno} z linie šlechty, tzv. Přemyslovců. Mé aktuální zdraví je {self.zdravi}. Pro tuto vlast Já zabit nebudu."
    def utok(self):
        magie = (random.randint(10,50))
        if(magie >=10):
            return f"Díky síle schované v mé duši jsem castnul {self.mana-10} manu a zbavil nepřítele o {random.randint(25,40)} zdraví. Proti kouzelníkům typický voják nic nemá."
        else:
            return f"Než se mi dobila mana, nepřítel na mě zaútočil a bránil jsem se holí od mého pradědy. Nepřítel přišel o -5 zdraví."



Artur = Postava("Artur z Litomyšle, budoucí rytíř a neskutečně dobrý bojovník.", 100)
print(Artur.predstav_se())
print(Artur.utok())


Harold = Rytir("Harold Modrozub, rytíř a královský ochránce", 90, "železa")
print(Harold.predstav_se())
print(Harold.utok())
print(Harold.zablokuj())

Majhor = Mag("Majhor Lušteník Obřízub, kouzelník a vražedník síly panovníka.", 80, 50)
print(Majhor.predstav_se())
print(Majhor.utok())