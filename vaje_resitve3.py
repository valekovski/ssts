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
