import copy
from math import sqrt

m:int
n:int
covek:bool

def unesiDim():
    s=input("Unesite dimenzije table: x,y ")
    return list(s.split(","))
q = unesiDim()
m=int(q[0])
n=int(q[1])

def izborIgraca():
    p=input("Unesite da li igru pocinje covek ili racunar: H/C ")
    if(p=='C' or p=='c'):
        return False
    elif(p=='H' or p=='h'):
        return True
    else:
        print("Pogresan unos")
        return izborIgraca()

def izborIgre():
    p=input("Unesite da li igraju 2 igraca(1) ili covek protiv racunara(0): ")
    if(p=="0"):
        return False
    elif(p=="1"):
        return True
    else:
        print("Pogresan unos")
        return izborIgre()

#---------------------
# X igrac je True, a O je False
#---------------------

def prikazTabla(tabla):
    slovo='A'  #pocetak prikaza slova
    print("    ",end=" ") #razmak od pocetka
    for x in range(0,n):
        print(chr(ord(slovo)+x),end="   ")
    print()  # kraj slova, novi red za ===
    print("   ",end=" ")
    for x in range(0,n):
            print("===",end=" ")
    print() #stampa === pomereno za odredjeni broj mesta i ide u novi red za matricu
    for x in range(0,m-1): #obilaze se sve vrste osim poslednje, a prikazuju sve osim prve
        print(m-x,"||", end="")
        for y in range(0,n):
            print(" ",end="")
            print(tabla[m-x-1][y],"|",end="")
        print("|",m-x)
        print("   ",end=" ")
        for y in range(0,n):
            print("---",end=" ")
        print()
    print(1,"||", end=" ")
    for y in range(0,n-1):
        print(tabla[0][y],"|",end=" ")
    print(tabla[0][n-1],"|",end="")
    print("|",1)
    #stampa === i slova na dnu
    print("   ",end=" ")
    for x in range(0,n):
            print("===",end=" ")
    print()
    print("    ",end=" ")
    for x in range(0,n):
        print(chr(ord(slovo)+x),end="   ")
    print()

def praznaTabla(dim1,dim2):
    val = ['-'] * dim1
    for x in range (dim1):
        val[x] = ['-'] * dim2
    return val

def zavrsenaPartija(igrac,tabla):
    if(igrac==True):
        for x in range(m-1):
            for y in range(n):
                if(tabla[x][y]=='-' and tabla[x+1][y]=='-'):
                    return 1   
        return -100 
    else:
        for x in range(m):
            for y in range(n-1):
                if(tabla[x][y]=='-' and tabla[x][y+1]=='-'):
                    return 1    
        return 100 

def potezValjan(igrac, potez):
     x=int(potez[0])
     y = potez[1] 
     if (ord(y)>90):
        y=ord(y)-65-32
     else:
         y = ord(y)-65 
     if(x <= 0 or x > m or y < 0 or y >= n):
          print('Uneli ste pogresan potez, pokusajte ponovo')
          return False
     elif(igrac == True):
          if(x==m):
               print('Uneli ste pogresan potez, pokusajte ponovo')
               return False
          elif(tabla[x-1][y]=='-' and tabla[x][y]=='-'):
               return True
          else:
               print('Uneli ste pogresan potez, pokusajte ponovo')
               return False
     else:
          if((y+1) == n):
               print('Uneli ste pogresan potez, pokusajte ponovo')
               return False
          elif(tabla[x-1][y]=='-' and tabla[x-1][y+1]=='-'):
               return True
          else:
               print('Uneli ste pogresan potez, pokusajte ponovo')
               return False

def igrajPotez(igrac,potez,tabla):
    x=int(potez[0])
    y=potez[1]
    if (ord(y)>90):
        y=ord(y)-65-32
    else:
         y = ord(y)-65
    if(potezValjan(igrac,potez)):
        if(igrac):
            tabla[x][y] = 'X'
            tabla[x-1][y] = 'X'
        else:
            tabla[x-1][y] = 'O'
            tabla[x-1][y+1] = 'O'
    return tabla

def igraj(igrac):
    if(zavrsenaPartija(igrac,tabla)==100):
        print("Pobednik je igrac X")
        return
    elif(zavrsenaPartija(igrac,tabla)==-100):
        print("Pobednik je igrac O")
        return 
    if(igrac):   
        potez=input("Igrac X: Unesite potez(primer: 1,A): ").split(",")
    else:
        potez=input("Igrac O: Unesite potez(primer: 1,A): ").split(",")
    while(not potezValjan(igrac,potez)):
        potez=input("Unesite potez ponovo(primer: 1,A): ").split(",")
    igrajPotez(igrac,potez,tabla)
    prikazTabla(tabla)
    igraj(not igrac)

def sviPotezi(igrac,tabla):   #vraca sva moguca stanja
    a=[]
    if(igrac):
        for x in range(m-1):
            for y in range(n):
                if(tabla[x][y]=='-' and tabla[x+1][y]=='-'):
                    potez=((x,y))
                    a.append(potez)
    else:
        for x in range(m):
            for y in range(n-1):
                if(tabla[x][y]=='-' and tabla[x][y+1]=='-'):
                    potez=((x,y))    
                    a.append(potez) 
    return a   

def sveTable(igrac,listaPoteza,tabla):
    table=[]
    for potez in listaPoteza:
        novaTabla=copy.deepcopy(tabla)
        if(igrac):
            novaTabla[potez[0]][potez[1]]='X'
            novaTabla[potez[0]+1][potez[1]]='X'
        else:
            novaTabla[potez[0]][potez[1]]='O'
            novaTabla[potez[0]][potez[1]+1]='O'
        table.append(novaTabla)
    return table

def brojPoteza(lista):
    br=0
    for x in lista:
        br=br+1
    return br

def brojSigurnihPoteza(igrac,tabla):
    br=0
    x=0
    y=0
    if(igrac):
        while y<n:
            while x<m-1:
                if(tabla[x][y]=='-' and tabla[x+1][y]=='-' and ((y==0 and (tabla[x][y+1]!='-'and tabla[x+1][y+1]!='-')) or (y==n-1 and (tabla[x][y-1]!='-'and tabla[x+1][y-1]!='-'))or(0<y<n-1 and tabla[x][y-1]!='-'and tabla[x+1][y-1]!='-'and tabla[x][y+1]!='-'and tabla[x+1][y+1]!='-'))):
                    br+=1
                    x+=1    
                x+=1  
            y+=1
            x=0          
    else:
        while x<m:
            while y<n-1:
                if(tabla[x][y]=='-' and tabla[x][y+1]=='-' and ((x==0 and (tabla[x+1][y]!='-'and tabla[x+1][y+1]!='-')) or (x==m-1 and (tabla[x-1][y]!='-'and tabla[x-1][y+1]!='-'))or(0<x<m-1 and tabla[x+1][y]!='-'and tabla[x+1][y+1]!='-'and tabla[x-1][y]!='-'and tabla[x-1][y+1]!='-'))):
                    br+=1
                    y+=1
                y+=1
            x+=1
            y=0                  
    return br

def procenaVrednosti(igrac,tabla):
    brPoteza=brojPoteza(sviPotezi(igrac,tabla))
    brSigurnihPoteza=brojSigurnihPoteza(igrac,tabla)
    return brPoteza+brSigurnihPoteza

def procena(tabla):
    return procenaVrednosti(True,tabla)-procenaVrednosti(False,tabla)


def max_value(tabla,igrac, dubina, alpha, beta, potez=None):
    lista_poteza = sviPotezi(igrac,tabla)
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        return (potez, procena(tabla))
    else:
        table=sveTable(igrac,lista_poteza,tabla)
        for s,t in zip(lista_poteza,table):
            s1=(s[0]+1,chr(s[1]+65))
            alpha = max(alpha, min_value(t,igrac, dubina - 1,alpha, beta, s1), key=lambda x: x[1])
    if alpha[1] >= beta[1]:
        return beta
    return alpha

def min_value(tabla,igrac, dubina, alpha, beta, potez=None):
    lista_poteza = sviPotezi(igrac,tabla)
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        return (potez, procena(tabla))
    else:
        table=sveTable(igrac,lista_poteza,tabla)
        for s,t in zip(lista_poteza,table):
            s1=(s[0]+1,chr(s[1]+65))
            beta = min(beta, max_value(t,igrac, dubina - 1,alpha, beta, s1), key=lambda x: x[1])
    if alpha[1] >= beta[1]:
        return alpha
    return beta



def minimax_alpha_beta(stanje, dubina,moj_potez, alpha=(None, -100), beta=(None, 100)):
    if moj_potez:
        return max_value(stanje,moj_potez, dubina, alpha, beta)
    else:
        return min_value(stanje,moj_potez, dubina, alpha, beta)

def partija():
    if(izborIgre()):
        igraj(True)
    else:
        covek=izborIgraca()
        igra(True,covek)


def igra(igrac,covek):
    if(zavrsenaPartija(igrac,tabla)==100):
        print("Pobednik je igrac X")
        return
    elif(zavrsenaPartija(igrac,tabla)==-100):
        print("Pobednik je igrac O")
        return
    else: 
        if(covek):     
            potez=input("Unesite potez(primer: 1,A): ").split(",")
            while(not potezValjan(igrac,potez)):
                potez=input("Unesite potez(primer: 1,A): ").split(",")
            igrajPotez(igrac,potez,tabla)
            prikazTabla(tabla)
            covek=not covek
            igra(not igrac,covek)
        else:
            tuplePotez=minimax_alpha_beta(tabla,3,igrac)
            if(tuplePotez[0]!=None):
                igrajPotez(igrac,tuplePotez[0],tabla)
                prikazTabla(tabla)
                print("Potez racunara: "+ str(tuplePotez[0]))
                covek=not covek
                igra(not igrac,covek)
            else:
                igra(igrac,covek)
tabla=praznaTabla(m,n)
prikazTabla(tabla)
partija()