from shop.proizvodi import Proizvod

class Narudzba:
    def __init__(self):
        self.proizvodi = []
        self.ukupna_cijena = 0

    def ispis_narudzbe(self):
        naruceni_proizvodi = ', '.join([f'{p.naziv} x {p.kolicina}' for p in self.proizvodi])
        print(f'Naručeni proizvodi: {naruceni_proizvodi}, Ukupna cijena: {self.ukupna_cijena} eur')

narudzbe = []

def napravi_narudzbu(lista_proizvoda):
    if not isinstance(lista_proizvoda, list):
        raise ValueError("argument  proizvodi  mora biti lista")
    if not all(isinstance(p, dict) for p in lista_proizvoda):
        raise ValueError(" svaki element u listi mora biti rječnik")
    if not all('naziv' in p and 'cijena' in p and 'kolicina' in p for p in lista_proizvoda):
        raise ValueError("svaki rječnik mora sadržavati ključeve  naziv ,  cijena  i  kolicina")
    if not lista_proizvoda:
        raise ValueError("lista ne smije biti prazna")

    narudzba = Narudzba()
    for p in lista_proizvoda:
        proizvod = Proizvod(p['naziv'], p['cijena'], p['kolicina'])
        if proizvod.kolicina <= 0:
            print(f"Proizvod {proizvod.naziv} nije dostupan!")
            return None
        narudzba.proizvodi.append(proizvod)
        narudzba.ukupna_cijena += proizvod.cijena * proizvod.kolicina

    narudzbe.append({
        'proizvodi': narudzba.proizvodi,
        'ukupna_cijena': narudzba.ukupna_cijena
    })

    return narudzba