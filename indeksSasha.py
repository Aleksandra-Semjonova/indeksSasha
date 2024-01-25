print("Tere! Olen sinu uus sober - Python!")
nimi = input("mis su nimi on?")
print(nimi ,", oi kui ilus nimi!")
int(input(nimi  ,"! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if answer==1:
    pikkus = int(input("Pikkus:"))
    mass = int(input("Mass:"))
    indeks = float(mass/0.01*pikkus**2)
    print(float(nimi ,"! Sinu keha indeks on:", indeks))
elif indeks<16:
    print("Tervisele ohtlik alakaal")
elif indeks>16:
    print("Alakaal")
elif indeks>19:
    print("Normaalkaal")
elif indeks>25:
    print("Ülekaal")
elif indeks>30:
    print("Ülekaal")
elif indeks>35:
    print("Tugev rasvumine")
elif indeks>40:
    print("Tervisele ohtlik rasvumine")
else:
    print("Kahju! See on väga kasulik info!")
print()
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
