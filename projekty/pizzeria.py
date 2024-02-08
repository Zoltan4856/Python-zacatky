print("Dobre din co si date")

seznam = ["Durum","Doner","Box"]
seznam1 = ["S","M","L","XXL"]

print(f"{seznam}")

x = False

while not x:

    menu  = input("Co si date")
    if menu in seznam:
        print(seznam1)
        velikost = input("Jak velke to chcete")
        if velikost in seznam:
            print("dobre") 
    elif menu or velikost == 'Konec':
        x = True
        print("To je vse ")