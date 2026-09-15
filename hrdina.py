class Hrdina:
    def __init__(self, jmeno:str, LVL:int, lokace:str = "Pod mostem"):
        self.jmeno = jmeno
        self.LVL = LVL
        self.lokace = lokace
    def pokrik(self):
        return f"Nikdy mě nezastavíte! Zachráním vaše duše a pak budu oslavován!"
    def predstav_se(self):
        return f"Mé jméno? Nazívám se {self.jmeno}. Můj LVL je {self.LVL}. Vaším ochráncem budu a oslavy očekávané jsou."
    def kde_jsi(self):
        return f"Ocitl jsem se na místě v královstím Děkuvzdaném, tzv. {self.lokace}."
    def presun_se(self, n_lokace:str):
        self.lokace = n_lokace
        return f"Jak pobožský jsem, odvážil jsem se přesunout na místo zvaném {n_lokace}"
    
hrdina = Hrdina("Princ Otakar VII. ze vzdálené země Ortikupse", 50)

print(hrdina.jmeno)
print(hrdina.LVL)
print(hrdina.lokace)

print(hrdina.pokrik())
print(hrdina.predstav_se())
print(hrdina.kde_jsi())
print(hrdina.presun_se("Západoseverní vodopád ve Svatých lázní mého otce, Jindřicha X."))


class Robot:
    def __init__(stroj, oznaceni:str, baterie:int,ukol:str = "výpočet komplexních počtů"):
        stroj.oznaceni = oznaceni
        stroj.baterie = baterie
        stroj.ukol = ukol
    def zvuk(stroj):
        return f"Bíp bůp bápity báp."
    def diagnostika(stroj):
        return f"Dobrý den, člověče, mé jméno je {stroj.oznaceni} a má baterka je {stroj.baterie}."
    def aktual_ukol(stroj):
        return f"Můj úkol je {stroj.ukol}. Rád Vás obsloužím."
    def zadej_ukol(stroj, novy_ukol:str):
        stroj.ukol = novy_ukol
        return f"Nastala změna úkolu, pozor, pozor. Vypočítávám... Můj nový úkol je {novy_ukol}."
    
robot = Robot("model 6324P-X2108Z", 100)

print(robot.oznaceni)
print(robot.baterie)
print(robot.ukol)

print(robot.zvuk())
print(robot.diagnostika())
print(robot.aktual_ukol())
print(robot.zadej_ukol("úklid palubek"))

class Motorka:
    def __init__(masina, znacka:str, kategorie:str, stav_nadrze:int, stav_stojanku:str = "postavený"):
        masina.znacka = znacka
        masina.kategorie = kategorie
        masina.stav_nadrze = stav_nadrze
        masina.stav_stojanku = stav_stojanku
    def zatoc_plyn(masina):
        return f"Vrum vrum!"
    def popis_moto(masina):
        return f"Popis tohot stroje je {masina.znacka} a {masina.kategorie}."
    def stav_stoj_vypis(masina):
        return f"Stojánek tohoto stroje je {masina.stav_stojanku}."
    def popojed(masina):
        pass
    def vypis_palivo(masina):
        pass
    def natankuj_danr_mnozstvi(masina):
        pass