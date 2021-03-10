#
# 2. sklop
#

# 1. Državna agencija za varstvo potrošnikov

# Uporabimo lahko rešitev iz zadnje naloge. Če želimo izračunati povprečno ceno, moramo nekako
# beležiti tudi število izdelkov (povrečje = vsota/st_izdelkov). V predzadnji nalogi to že počnemo,
# kaj pa v zadnji?
vsota = 0.0         # v tej spremenljivki bomo hranili akumulirano vrednost artiklov
st_izdelkov = 0     # inicializiramo število izdelkov

cena = float(input("Cena artikla: "))
while (cena != 0):
  vsota += cena
  st_izdelkov += 1
  cena = float(input("Cena artikla: "))

print("Vsota: ", vsota)
print("Povprečna cena: ", vsota/st_izdelkov)


# 2. Ajavost nizov

niz = input("Vnesite besedilo: ")

print("Število a-jev v vnešenem besedilu je: ", niz.count("a"))


# 3. Delitelji števil

# Naivni algoritem za vsako število med 1 in vnešenim številom preverja, če je vnešeno število z njim
# deljivo. Kako vemo, če je neko število deljivo z drugim?
# Namig: Pazite na pričetek štetja z 0!
stevilo = int(input("Vnesite število: "))

for i in range(stevilo):
  trenutno_st = i + 1                 # ker smo zaceli steti z 0 in koncamo pri 1 manj, kot je stevilo
  if (stevilo%trenutno_st == 0):      # ce je ostanek pri deljenju 0
    print(trenutno_st)


# 4. Praštevilo

# Kdaj rečemo številu, da je praštevilo? Ko je deljivo samo z 1 in s samim seboj. Uporabimo lahko prejšnji
# program. Beležiti moramo, če je bilo število deljivo s katerimkoli številom, ki ni 1 ali število samo.
# Kateri podatkovni lahko za to uporabimo? (Namig: preberite si o logičnih operatorjih, ki jih pri pouku
# še nismo obravnavali - https://www.w3schools.com/python/python_operators.asp )
stevilo = int(input("Vnesite število: "))
prastevilo = True                     # predvidevamo, da je število praštevilo, dokler mu ne dokažemo nasprotno,
                                      # tj., dokler ne najdemo delitelja različnega od 1 in števila samega

for i in range(stevilo):
  trenutno_st = i + 1                 # ker smo zaceli steti z 0 in koncamo pri 1 manj, kot je stevilo
  if (trenutno_st != 1 and
      trenutno_st != stevilo and
      stevilo%trenutno_st == 0):

    prastevilo = False
    break

if (prastevilo):
  print("Vnešeno število je praštevilo.")
else:
  print("Vnešeno število ni praštevilo.")

# Naloge bi se lahko lotili tudi drugače. Sprehodimo se po vseh številih med 1 in številom in preverjamo.
stevilo = int(input("Vnesite število: "))
prastevilo = True                     # predvidevamo, da je število praštevilo, dokler mu ne dokažemo nasprotno,
                                      # tj., dokler ne najdemo delitelja različnega od 1 in števila samega

trenutni_delitelj = 2                 # 1 preskočimo
while (trenutni_delitelj < stevilo):
  if (stevilo%trenutni_delitelj == 0):
    prastevilo = False
    break
  trenutni_delitelj += 1              # ne pozabimo povišati števca!

if (prastevilo):
  print("Vnešeno število je praštevilo.")
else:
  print("Vnešeno število ni praštevilo.")
