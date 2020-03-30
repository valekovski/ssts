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
