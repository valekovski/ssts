#
# Seznami 1. sklop
#

# 1. Napišite program, ki ustvari poljubno polje stotih celih (naključnih) števil z vrednostmi od 10 do 100 ter izpiše le tiste člene, ki so večji od zadnjega elementa v tem seznamu.

import random

ST_ELEMENTOV = 100

# naredimo seznam 100 naključnih števil z vrednostjo med 10 in 100
seznam = []
for i in range(ST_ELEMENTOV):
    nakljucno_st = random.randint(10, 100)
    seznam.append(nakljucno_st)

# ponovno se sprehodimo čez seznam,
# izpišemo element, če je večji od zadnjega elementa seznama
vrednost_zadnjega_elem = seznam[-1]
for i in range(len(seznam)):
    if (seznam[i] > vrednost_zadnjega_elem):
        print(seznam[i], " ", end="")

# po potrebi med izvajanjem programa izpišite vrednosti, ki vas zanimajo
# (npr. seznam, ali trenutni element, ali zadnji element v seznamu, ipd.)


# 2. Napišite program, ki generira 50 naključnih števil (vrednosti od 1 do 1000), nato pa izpiše največje izmed vseh generiranih števil.
#    Pri zapisu algoritma ne smete uporabiti vnaprej definiranih metod/funkcij za iskanje največje vrednosti.

import random

ST_ELEMENTOV = 50

# naredimo seznam 50 naključnih števil z vrednostjo med 1 in 1000
seznam = []
for i in range(ST_ELEMENTOV):
    nakljucno_st = random.randint(1, 1000)
    seznam.append(nakljucno_st)

# ponovno se sprehodimo čez seznam,
# če je trenutni element večji od do zdaj najdenega največjega števila, ga shranimo
najvecji_element = -1                           # inicializiramo na minimalno vrednost
for i in range(len(seznam)):
    if (seznam[i] > najvecji_element):
        najvecji_element = seznam[i]

# na koncu le še izpišemo največjo shranjeno vrednost
print("Največje število v seznamu je ", najvecji_element)

# po potrebi med izvajanjem programa izpišite vrednosti, ki vas zanimajo
# (npr. seznam, ali trenutni element, ali trenutni največji element, ipd.)


# 2. Napišite program, ki simulira met kocke – generira naključna števila od 1 do 6.
#    Algoritem naj generira tovrstno naključno število 100-krat in na koncu poda statistiko, kolikokrat je bilo izžrebano število 1, kolikokrat 2, itd.

import random

ST_METOV = 100

# naredimo seznam metov kocke
seznam_metov = []
for i in range(ST_METOV):
    nakljucno_st = random.randint(1, 6)
    seznam_metov.append(nakljucno_st)

# sprehodimo se čez možne vrednosti kocke (tj. 1-6) in za vsako vrednost zabeležimo,
# kolikokrat je bila dobljeno ob metu kocke
for i in range(6):
    vrednost_kocke = i + 1          # ker funkcija range vrne števila od 0 do 5
    st_metov = 0                    # kolikokrat smo vrgli to vrednost

    for vrednost_meta in seznam_metov:
        if (vrednost_meta == vrednost_kocke):
            st_metov += 1

    # ne pozabimo izpisati št. metov te vrednosti
    print(vrednost_kocke, " smo vrgli ", st_metov, "x")

# namig: poizkusite povišati število metov na 10000. Kaj opazite?
# Če kocko vržemo velikokrat, kakšen rezultat bi pričakovali?


# Precej elegantnejša rešitev je možna z uporabo slovarjev. Npr. takole:
import random

ST_METOV = 100

# inicializiramo slovar metov kocke
# vsak element ima dve vrednosti, to sta ključ in vrednost
# ključ je vrednost meta, vrednost pa je število metov te vrednosti
# npr. vnos v slovarju (4, 23) bi pomenil, da smo 4 vrgli 23x
meti_kocke = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

# generiramo mete kocke
for i in range(ST_METOV):
    nakljucno_st = random.randint(1, 6)
    meti_kocke[nakljucno_st] += 1               # povišamo št. metov ustrezne vrednosti

# izpišemo rezultate
for vrednost_meta in meti_kocke:
    print(vrednost_meta, " smo vrgli ", meti_kocke[vrednost_meta], "x")


# 4. Napišite program, ki bo ustvaril polje 10 celih števil. Števila morajo biti liha in imeti vrednost med 1 in 100. Na koncu to polje izpišite.

import random

ST_ELEMENTOV = 10

# naredimo seznam 10 naključnih števil z vrednostjo med 1 in 100
# paziti moramo, da so števila liha! Ker ne moremo vedeti vnaprej
# koliko števil izmed generiranih naključnih števil bo lihih,
# ne moremo uporabiti zanke for.
seznam = []
while (len(seznam) < 10):
    nakljucno_st = random.randint(1, 1000)

    # če je število liho, ga dodamo v seznam
    if (nakljucno_st%2 != 0):
        seznam.append(nakljucno_st)

# na koncu le še izpišemo naš seznam in se prepričamo, da so vrednosti ustrezne
print(seznam)
