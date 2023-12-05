handleliste = { }

def leggTilVare():

    vare= input( "skriv varen: ")
    pris= input( "skriv inn pris: ")
    handleliste [vare]= pris
    print("varen har blitt lagt til")

def fjernVare():
    input= ("skriv inn navnet på varen som skal fjernes: " )
    handleliste.pop (input)


def seListe():
   for vare in handleliste: 
      print(f"{vare} {handleliste[vare]}")
      
def sePris():
   sum-0
   for vare in handleliste:
      sum=sum+handleliste[vare]
      print(f"summen er: {sum} kr/n")


def meny():
    print("1.legg til vare")
    print("2.fjern vare")
    print("3.se liste")
    menyvalg= int (input("skriv inn valg: "))

    if menyvalg== 1:
        leggTilVare()
    elif menyvalg== 2:
       fjernVare() 
    elif menyvalg==3:
       seListe()    
    elif menyvalg==4:
       sePris()
  

while True: 
 meny()
