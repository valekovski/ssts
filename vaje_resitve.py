#
# 1. sklop
#

# 1. Vsi po pet

vsota = 0.0         # v tej spremenljivki bomo hranili akumulirano vrednost artiklov

for i in range(5):
  cena = float(input("Cena artikla: "))
  vsota += cena

print("Vsota: ", vsota)

# Enako pravilno bi bilo, če bi namesto zanke uporabnika 5x vprašali po ceni.
# Prav tako bi lahko uporabili 5 različnih spremenljivk, ki bi jih na koncu sešteli,
# vendar pa je tako program daljši in manj pregleden. Kaj pa, če bi želeli prebrati
# cene 100 različnih artiklov?
izdelek1 = float(input("Cena artikla: "))
izdelek2 = float(input("Cena artikla: "))
izdelek3 = float(input("Cena artikla: "))
izdelek4 = float(input("Cena artikla: "))
izdelek5 = float(input("Cena artikla: "))

print("Vsota: ", izdelek1 + izdelek2 + izdelek3 + izdelek4 + izdelek5)

# Zakaj potrebujemo podatkovni tip float? Ali bi bil podatkovni tip int prav tako v redu?


# 2. Konkurenca

# Če smo program načrtovali premišljeno že v 1. nalogi, potem lahko z malenkostnimi spremembami
# ustrezno popravimo program še za to nalogo. Dodamo spremenljivko st_izdelkov, jo preberemo in
# njeno vrednost uporabimo pri štetju ponovitev zanke for
st_izdelkov = 0     # koliko izdelkov bomo prebrali
vsota = 0.0         # v tej spremenljivki bomo hranili akumulirano vrednost artiklov

st_izdelkov = int(input("Število izdelkov: "))
for i in range(st_izdelkov):
  cena = float(input("Cena artikla: "))
  vsota += cena

print("Vsota: ", vsota)

# Zakaj pa je bilo v tej nalogi ustrezno, da smo za spremenljivko st_izdelkov uporabili podatkovni
# tip int?


# 3. Top-shop

# Uporabimo lahko rešitev iz prve naloge. Dodati moramo zgolj en pogojni stavek, ki nam bo povedal,
# kdaj moramo izstopiti iz zanke. Ker ne vemo točnega števila ponovitev zanke (saj je odvisno od
# uporabnika programa, kdaj bo vpisal 0), je na mestu uporaba zanke while namesto zanke for.
vsota = 0.0         # v tej spremenljivki bomo hranili akumulirano vrednost artiklov

cena = float(input("Cena artikla: "))
while (cena != 0):
  vsota += cena
  cena = float(input("Cena artikla: "))

print("Vsota: ", vsota)

# Bi lahko program zapisali z zanko for in pogojnim stavkom IF za izstop iz zanke? Poskusite!
# Namig: na internetu poiščite, kaj počne krmilni stavek break



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


#
# 3. sklop
#

# 1. Fibonaccijevo zaporedje

st_clenov = 20            # št. členov zaporedja, ki jih bomo generirali
predzadnji_clen = 1       # inicializiramo začetna dva člena
zadnji_clen = 1

print(predzadnji_clen, " ", end="")
print(zadnji_clen, " ", end="")

# odštejemo 2, ker smo prva dva člena že izpisali
for i in range(st_clenov - 2):
  nasl_clen = predzadnji_clen + zadnji_clen
  print(nasl_clen, " ", end="")

  # pripravimo števila za naslednjo iteracijo
  predzadnji_clen = zadnji_clen
  zadnji_clen = nasl_clen


# 2. Tekmovanje iz poštevanke

tekmovalec1_tocke = 0
tekmovalec2_tocke = 0

# igra se ponavlja, dokler absolutna razlika med točkama tekmovalcev ni vsaj 2
while (abs(tekmovalec1_tocke - tekmovalec2_tocke) < 2):
  # dobra praksa narekuje, da vsako spremenljivko pred uporabo inicializiramo
  faktor1 = 0
  faktor2 = 0
  produkt = 0

  faktor1 = int(input("Tekmovalec 1, prvi faktor? "))
  faktor2 = int(input("Tekmovalec 1, drugi faktor? "))
  produkt = int(input("Tekmovalec 2, produkt?"))
  # pazite na uporabo primerjalnega operatorja == in ne priredilnega =
  if (produkt == (faktor1*faktor2)):
    tekmovalec2_tocke += 1

  print()
  faktor1 = int(input("Tekmovalec 2, prvi faktor? "))
  faktor2 = int(input("Tekmovalec 2, drugi faktor? "))
  produkt = int(input("Tekmovalec 1, produkt?"))
  if (produkt == (faktor1*faktor2)):
    tekmovalec1_tocke += 1

  # po vsaki iteraciji izpišemo trenutni rezultat
  print()
  print("Trenutni rezultat: ", tekmovalec1_tocke, " : ", tekmovalec2_tocke)
  print()

# na koncu še pohvalimo zmagovalca
if (tekmovalec1_tocke > tekmovalec2_tocke):
  print("Bravo prvi! Drugi, cvek!")
else:
  print("Bravo drugi! Prvi, cvek!")


#
# 4. sklop
#

# 1. Števke

# število lahko na števke razcepimo tako, da ga delimo z 10 in preverimo ostanek,
# nato ta ostanek odbijemo in postopek ponovimo, dokler nismo števila zdelili do konca
vhodno_st = int(input("Vnesite začetno število: "))

print()
print("Števke so: ")
while (vhodno_st > 0):
  print(vhodno_st%10)

  # ostanka se znebimo s celoštevilskim deljenjem //
  vhodno_st = vhodno_st//10


# 2. Operacija deljenja

# drugo število odštevamo od prvega toliko časa, dokler prvo ni manjše od drugega
# pri tem štejemo, kolikokrat smo drugega že odšteli od prvega
# to bo naš rezultat
prvo_st = int(input("Vnesite prvo število: "))
drugo_st = int(input("Vnesite drugo število: "))
rezultat = 0

# ohranimo začetni vrednosti števil, da ju bomo lahko na koncu izpisali
M = prvo_st
N = drugo_st

while (prvo_st >= drugo_st):
  rezultat += 1
  prvo_st -= drugo_st

print(M, "/", N, " = ", rezultat, ", ost. ", prvo_st)


# 3. Soda števila od 1 do 100

vsota_sodih = 0

for stevilo in range(100):
  # spomnimo: funkcija range vrne števila od 0 do 99, zato moramo številu prišteti 1
  # če je število sodo preverimo z ostankom pri deljenju z 2, če je ta 0, potem je število sodo
  if ((stevilo + 1)%2 == 0):
    vsota_sodih += (stevilo + 1)

print("Rezultat: ", vsota_sodih)


# 4. Najmanjša vrednost, razen 0

min_st = int(input("Vnesite število: "))        # v tej spremenljivki bomo hranili naše najmanjše število
trenutno_st = min_st

while (trenutno_st != 0):
  if (trenutno_st < min_st):
    min_st = trenutno_st

  trenutno_st = int(input("Vnesite število: "))

print("Najmanjše vnešeno število je ", min_st)
