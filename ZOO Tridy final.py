class Zvire:
    def __init__(self, jmeno, druh, vaha):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha  = vaha
    def __str__(self):
        return f"{self.druh} se jmenuje {self.jmeno} a vazi {self.vaha} kg."
    def export_to_dict(self):
        return {"jmeno":self.jmeno, "druh":self.druh, "vaha":self.vaha}  

class Zamestnanec:
    def __init__(self, cele_jmeno, rocni_plat, pozice):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice
    def __str__(self):
        return f"{self.cele_jmeno} pracuje jako {self.pozice} a ma rocni plat {self.rocni_plat}."    

class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno, rocni_plat, oblibene_zvire):
        super().__init__(cele_jmeno, rocni_plat, pozice = "Reditel") 
        self.oblibene_zvire = oblibene_zvire
    def __str__(self):
        return super().__str__() + f"Jeho oblibene zvire je {self.oblibene_zvire}"

class Zoo:
    def __init__(self, nazev, adresa, reditel, list_of_employees, list_of_animals):
        self.nazev = nazev
        self.adresa = adresa
        self.reditel = reditel
        self.list_of_employees = list_of_employees
        self.list_of_animals = list_of_animals

zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},
]

pavouk = Zvire
pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)
print(pavouk.__dict__) 

list_of_animals = []
for i in zvirata_dict:
    zvire = Zvire(i["jmeno"], i["druh"], i["vaha"])
    list_of_animals.append(zvire)

print(list_of_animals[0])   
print(list_of_animals[1]) 
print(list_of_animals[2])
print(list_of_animals[3]) 
 
zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

list_of_employees = []
for i in zamestnanci_dict:
    zamestnanec = Zamestnanec(i["cele_jmeno"], i["rocni_plat"], i["pozice"])
    list_of_employees.append(zamestnanec)

print(list_of_employees[0])   
print(list_of_employees[1]) 
print(list_of_employees[2])

# ziskej inicialy skrze indexy"
print(list_of_employees[0].cele_jmeno[0],list_of_employees[0].cele_jmeno[-6])   
print(list_of_employees[1].cele_jmeno[0],list_of_employees[1].cele_jmeno[-6])  
print(list_of_employees[2].cele_jmeno[0],list_of_employees[2].cele_jmeno[-6])  

         
zvire = Zvire('Adolf', 'Tarantule Velká', 0.1)        
reditel = Reditel(cele_jmeno='Karel Velky', rocni_plat=800_000, oblibene_zvire=zvire)

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, list_of_employees, list_of_animals)
print(zoo.reditel)

#rocni_plat_zamestnancu_zoo#
zoo_zamestnanci = [reditel, list_of_employees[0], list_of_employees[1], list_of_employees[2]]
rocni_plat_zoo = sum(i.rocni_plat for i in zoo_zamestnanci)
print("Rocni plat zamestnancu v ZOO je", rocni_plat_zoo, "Kc.")

#mesicni_naklady_na_zamestnance
mesicni_naklady_na_zamestnance = round(rocni_plat_zoo/12,2)
print("Mesicni naklady na zamestnance jsou", mesicni_naklady_na_zamestnance, "Kc.")  

#celkova_vaha_zvirat_zoo#
zoo_zvirata = [pavouk, list_of_animals[0], list_of_animals[1], list_of_animals[2], list_of_animals[3]]
celkova_vaha_zvirat_zoo = sum(i.vaha for i in zoo_zvirata)  
print("Vsechna zvirata vazi", celkova_vaha_zvirat_zoo,"kg.")

## Asserty pro vlastní kontrolu
# Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}

# Zamestnanec class
# zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
# assert hasattr(zamestnanec, 'cele_jmeno')
# assert hasattr(zamestnanec, 'rocni_plat')
# assert hasattr(zamestnanec, 'pozice')
# assert isinstance(zamestnanec.cele_jmeno, str)
# assert isinstance(zamestnanec.rocni_plat, int)
# assert isinstance(zamestnanec.pozice, str)
# assert zamestnanec.ziskej_inicialy() == 'P.N.'

# Funkci inicialy jsem udelala takto: viz vyse
""" print(list_of_employees[0].cele_jmeno[0],list_of_employees[0].cele_jmeno[-6])   
print(list_of_employees[1].cele_jmeno[0],list_of_employees[1].cele_jmeno[-6])  
print(list_of_employees[2].cele_jmeno[0],list_of_employees[2].cele_jmeno[-6])   """
# Nevadi ?

# Reditel class
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

# Zoo class
zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'nazev')
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'list_of_employees')
assert hasattr(zoo, 'list_of_animals')
assert isinstance(zoo.nazev, str)
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.list_of_employees, list)
assert isinstance(zoo.list_of_animals, list)
""" assert zoo.celkova_vaha_zvirat_zoo() == 150 """
# Celkovou vahu zvirat mam spocitanou na radku 88 jako "celkova_vaha_zvirat_zoo"#
""" assert zoo.mesicni_naklady_na_zamestnance() == (rocni_plat_zoo) / 12 """
# Mesicni naklady na zamestnance mam spocitane na radku 85 #