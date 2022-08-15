# # string.count(iskani_niz)
# # string.lower()
# # string.upper()
# # len(polje/string)
# # string.find(iskani_niz)
# # string.split(separator)
# # separator.join(polje)
# # string.isdigit()
# # string.isalnum()
# # string.isalpha()
# # string.replace(iskani_niz, zamenjava)
# # string.strip(znaki_za_odstraniti_iz_zacetka_in_konca)
# # range(koncni_indeks)
# # range(zacetni_indeks, koncni_indeks)
# # range(zacetni_indeks, koncni_indeks, korak)

# import random

# # poiščimo najmanjše število v seznamu
# def najmanjsi_elem(seznam):
#   najmanjse = seznam[0]
#   for element in seznam:
#     if (element < najmanjse):
#       najmanjse = element

#   return najmanjse

# def generiraj_seznam():
#   seznam = []
#   for i in range(20):
#     seznam.append(random.randint(5,50))

#   return seznam

# def izpisi_najmanjse(seznam):
#   iskano_stevilo = najmanjsi_elem(seznam)
#   print(seznam)
#   print("Najmanjsi element v seznamu je", iskano_stevilo)


# moj_seznam = generiraj_seznam()
# moj_seznam2 = generiraj_seznam()

# izpisi_najmanjse(moj_seznam)
# izpisi_najmanjse(moj_seznam2)



# def zanimivaVsotaStevk(stevilo):
#   leva_polovica = stevilo//100
#   desna_polovica = stevilo%100
# 
#   return leva_polovica + desna_polovica

# print(zanimivaVsotaStevk(1234))


# privzete vrednosti parametrov oz. opcijski parametri
# def inkrement(stevec, korak=1):
#   return stevec + korak

# stevilo = 0
# print(stevilo)
# stevilo = inkrement(stevilo,2)
# print(stevilo)
# stevilo = inkrement(stevilo)
# print(stevilo)

# rekurzivnost oz. rekurzivne funkcije



# slovarji (angl. Dictionary) ali asociativne tabele/polja (lahko tudi zgoščevalne tabele)
# slovar = {
#   "kljuc": "vrednost",
#   "monitor": "je naprava za prikazovanje slike",
#   "jabolko": "je sadez obicajno rdece barve"
# }

# imenik = {
#   "Janez Peteršiljček": {
#     "mobilna": "041123222",
#     "domaca": "052273389"
#   },
#   "Janez Novak": ["0402223333", "042282277"]
# }
# imenik["Tom Kamin"] = "031555222"


# # print("Ključi: ", imenik.keys())
# # print("Vrednosti: ", imenik.values())
# # print("Elementi: ", imenik.items())

# # for kljuc in imenik:
# #   print(kljuc, ":", imenik[kljuc])

# # imenik.pop("Janez Novak")
# # if "Janez Novak" in imenik:
# #   print(imenik["Janez Novak"])

# imenik2 = imenik.copy()     # imenik je objekt tipa/razreda Dictionary, copy() je metoda tega razreda

# # print(id(imenik))
# # print(id(imenik2))



# # objektno orientirano programiranje - OOP

# # podatke in operacije nad njimi združimo v abstraktne podatkovne strukture imenovane razred
# class Oseba:
#   # ime
#   # priimek
#   # letnik
#   # kraj

#   # lastni konstruktor
#   def __init__(self, ime, priimek):
#     self.ime = ime
#     self.priimek = priimek

#   def pozdrav(self):
#     print("Pozdravljeni ", self.ime, self.priimek)

# # oseba1 = Oseba()        # oseba1 je objekt tipa Oseba oz. instanca razreda Oseba
# # oseba2 = Oseba()
# # oseba2.ime = "Janez"    # do atributov dostopamo s piko za imenom objekta
# # oseba2.priimek ="Peteršiljček"

# oseba3 = Oseba("Janez", "Novak")
# oseba4 = Oseba("Janez", "Peteršiljček")
# oseba5 = Oseba("Tom", "Novak")

# oseba5.pozdrav()
# print(oseba5.priimek)




# class Pravokotnik:
#   def __init__(self, a, b):
#     self.a = a
#     self.b =  b

#   def ploscina(self):
#     return self.a*self.b

#   def obseg(self):
#     return 2*a + 2*b


# lik1 = Pravokotnik(5, 10)
# lik2 = Pravokotnik(4, 12)

# print(lik1.ploscina())
# print(lik2.ploscina())


class Naselje:
  # naselje
  # postnaSt
  # povrsina
  # statRegija

  def __init__(self, naselje, postnaSt, povrsina, statRegija):
    self.naselje = naselje
    self.postnaSt = postnaSt
    self.povrsina = povrsina
    self.statRegija = statRegija

naselja = []
naselja.append(Neselje("Trbovlje", 1420, 10.232, "Zasavska"))
naselja.append(Neselje("Trbovlje", 1420, 10.232, "Zasavska"))
naselja.append(Neselje("Trbovlje", 1420, 10.232, "Zasavska"))
naselja.append(Neselje("Trbovlje", 1420, 10.232, "Zasavska"))
naselja.append(Neselje("Trbovlje", 1420, 10.232, "Zasavska"))