from shop.proizvodi import Proizvod, dodaj_proizvod
from shop.narudzbe import Narudzba, napravi_narudzbu

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for proizvod in proizvodi:
    dodaj_proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])
    p = Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])
    p.ispis()


narudzba = napravi_narudzbu(lista_proizvoda=proizvodi)
narudzba.ispis_narudzbe()