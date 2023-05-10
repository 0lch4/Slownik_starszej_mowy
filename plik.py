dane = None
slownik = []
slowniczek = {}

def import_data(dane):
    with open('slowniczek.txt','r',encoding='utf-8') as f:
        dane = f.read()
    dane = dane.split('\n')
    return dane

def tuples(dane,slownik,slowniczek):
    for linia in dane:
        slowa = linia.split('-')
        slowo1 = slowa[0].strip()
        slowo2 = slowa[1].strip()
        krotka = (slowo1, slowo2)
        
        pierwsza_litera = slowo1[0]
        if pierwsza_litera in slowniczek:
            slowniczek[pierwsza_litera].append(krotka)
        else:
            slowniczek[pierwsza_litera] = [krotka]
        
        slownik.append(krotka)
        
def make_files(slowniczek):
    for litera, slowa in slowniczek.items():
        with open(f"slowniki\{litera}.txt", "w", encoding="utf-8") as f:
            f.write('\n'.join([f"{slowo[0]} - {slowo[1]}" for slowo in slowa]))
            
dane = import_data(dane)
tuples(dane,slownik,slowniczek)
make_files(slowniczek)
