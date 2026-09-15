class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass #nemusíme fuknci dopsat, nehází chybu 
    def zvuk(self):
        return "???"
    def predstav_se(self):
        return f"jsem {self.jmeno} a je mi {self.vek} let."
    def kde_jsi(self):
        return f"jsem na místě zvaném {self.misto}! Pomoc!"
    def jdi_na(self, n_misto:str):
        self.misto = n_misto
        return f"šel jsem na/ do {n_misto}"

zvire = Zvire("Šoral", 50)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)

print(zvire.zvuk())
print(zvire.predstav_se())
print(zvire.kde_jsi())
print(zvire.jdi_na("Les"))
print(zvire.kde_jsi())

zvire2 = Zvire("Wolfram", 32, "Prasečák")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)

print(zvire2.predstav_se())
print(zvire2.kde_jsi())
print(zvire2.jdi_na("Autobus"))
print(zvire2.kde_jsi())