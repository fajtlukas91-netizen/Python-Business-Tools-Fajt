vejce = int(input("Zadejte počet vajec: "))

velikost_plata= 6
pocet_plat = vejce // velikost_plata
zbytek_vajec = vejce % velikost_plata 

print(f"Počet vajec je:{vejce}, počet platje: {pocet_plat}, a zbyde{zbytek_vajec}.")
