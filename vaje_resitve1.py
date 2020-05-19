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
