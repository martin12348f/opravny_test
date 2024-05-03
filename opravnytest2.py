print("Vítejte v obchodě s ovocem")
print("Vyberte si vaše zboží")

zbozi = ["jablko", "hruska", "citron", "pomeranc", "banan"]
kosik = []

def vypis_zbozi():
    print("Výpis zboží")

def vypis_kosik():
    print("Výpis košíku")

def vypis_pole(prvek):
    for x in range(len(prvek)):
        print(f"Ovoce s číslem {x+1}: {prvek[x]}")

while True:
    vypis_zbozi()
    vypis_pole(zbozi)
    vyber = input("Zadej číslo ovoce: ")

    if vyber.lower() == "konec":
        break
    vyber = int(vyber)
    if 0 < vyber <= (len(zbozi)):
        kosik.append(zbozi.pop(vyber-1))
        vypis_kosik()
        vypis_pole(kosik)
    else:
        print("Špatné číslo")
