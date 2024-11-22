


class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f'{self.naziv} - {self.cijena} - {self.kolicina}')


def dodaj_proizvod(naziv, cijena, kolicina):
    proizvodi.append(Proizvod(naziv, cijena, kolicina))

proizvodi = [
    Proizvod('kapuz', 5, 10),
    Proizvod('jabuke', 7, 5)
]


dodaj_proizvod('pomidori', 5, 1)

for proizvod in proizvodi:
    proizvod.ispis()
print(f'\n***********\n')