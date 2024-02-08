print("Obchod s kalkulackami")
class Kalkulacka:
    def __init__(self,funkce,cena, vyrobce,vaha):
        self.funkce = funkce
        self.cena = cena
        self.vyrobce = vyrobce
        self.vaha = vaha
    def info(self):
        print(self.funkce,self.cena,self.vyrobce,self.vaha)

CASIO200 = Kalkulacka(funkce="zakladni", cena=200,vyrobce= "TOSHIBA", vaha=35) 
CASIO300 = Kalkulacka(funkce="zakladni", cena=500,vyrobce= "TOSHIBA", vaha=35) 
CASIO400 = Kalkulacka(funkce="zakladni", cena=600,vyrobce= "TOSHIBA", vaha=35) 
seznam = [CASIO200,CASIO300,CASIO400]

osoba = input("abc")


for j in seznam:
    print(j.info())
