# rs_zad5

## Zadatak 5: Moduli i paketi
Definirajte paket shop koji će sadržavati module proizvodi.py i narudzbe.py.

Modul proizvodi.py :
- definirajte klasu Proizvod s atributima naziv , cijena i kolicina . Dodajte metodu ispis koja će
ispisivati sve atribute proizvoda.
- u listu proizvodi dodajte 2 objekta klase Proizvod s proizvoljnim vrijednostima atributa.
- definirajte funkciju dodaj_proizvod van definicije klase koja će dodavati novi Proizvod u listu
proizvodi .

U main.py datoteci učitajte modul proizvodi.py iz paketa shop i pozovite pozovite funkciju
dodaj_proizvod za svaki element iz sljedeće liste:
```proizvodi = [
  {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
  {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
  {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
  {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]
```

Nakon što to napravite, pozovite metodu ispis za svaki proizvod iz liste proizvodi .

Modul narudzbe.py :
- definirajte klasu Narudzba s atributima: proizvodi i ukupna_cijena.
- dodajte funkciju napravi_narudzbu` van definicije klase koja prima listu proizvoda kao argument i
vraća novu instancu klase Narudzba .
- dodajte provjeru u funkciju napravi_narudzbu koja će provjeravati dostupnost proizvoda prije nego
što se napravi narudžba. Ako proizvoda nema na stanju, ispišite poruku "Proizvod {naziv} nije
dostupan!" i ne stvarajte narudžbu.
- dodajte provjere u funkciju napravi_narudzbu koja će provjeriti sljedeća 4 uvjeta:
  - argument proizvodi mora biti lista
  - svaki element u listi mora biti rječnik
  - svaki rječnik mora sadržavati ključeve naziv , cijena i kolicina
  - lista ne smije biti prazna
- izračunajte ukupnu cijenu narudžbe koju ćete pohraniti u ukupna_cijena u jednoj liniji koda.
- narudžbe pohranite u listu rječnika narudzbe .
- u klasu Narudzba dodajte metodu ispis_narudzbe koja će ispisivati nazive svih naručenih proizvoda,
količine te ukupnu cijenu narudžbe. (npr. "Naručeni proizvodi: Laptop x 2, Monitor x 1, Ukupna cijena: 11000 eur".)

U main.py datoteci učitajte modul narudzbe.py iz paketa shop i pozovite funkciju napravi_narudzbu s
listom proizvoda iz prethodnog zadatka.