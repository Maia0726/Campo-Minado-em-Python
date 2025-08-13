import os, sys
from random import*

c1 = 0
c2 = 0
contadorPos00 = 0

matriz = [["-" for x in range(20)] for x in range(20)]

bombas = [[randint(0,19) for x in range(2)] for x in range (40)]

for i in range(len(bombas)):
    v = 0
    for j in range(len(bombas)):
        if bombas [i][0] == bombas[j][0] and bombas [i][1] == bombas [j][1]:
            v+=1
        if v == 2:
            bombas = [[randint(0,19) for x in range(2)] for x in range (40)]
            

cont = 1
fim = False

def jogar():
    print("~~~~~~Campo Minado~~~~~~")
    os.system('pause')
    campo(20,20)
    
def campo(x,y):
    fim = False
    global cont
    contador = 0
    os.system('cls')
    for c in range(len(bombas)):
        if bombas[c][0] == x and bombas[c][1] == y:
            for e in range(len(bombas)):
                matriz[bombas[e][0]][bombas[e][1]] = "X"
                fim = True
                
        else:
            
            if x > 0 and y > 0 and x < 19 and y < 19:
                if bombas[c][0] == x-1 and bombas[c][1] == y-1:
                    contador += 1
                elif bombas [c][0] == x-1 and bombas [c][1] == y:
                    contador += 1
                elif bombas [c][0] == x-1 and bombas [c][1] == y+1:
                    contador += 1
                elif bombas [c][0] == x and bombas [c][1] == y-1:
                    contador += 1
                elif bombas [c][0] == x and bombas [c][1] == y+1:
                    contador += 1
                elif bombas [c][0] == x+1 and bombas [c][1] == y-1:
                    contador += 1
                elif bombas [c][0] == x+1 and bombas [c][1] == y:
                    contador += 1
                elif bombas [c][0] == x+1 and bombas [c][1] == y+1:
                    contador += 1
                matriz[x][y] = contador
                
            elif x == 0 or y == 0  or x ==19 or y == 19:
                
                if x == 0 and y == 0:
                    if bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas [c][0] == x+1 and bombas [c][1] == y:
                        contador += 1
                    elif bombas [c][0] == x+1 and bombas [c][1] == y+1:
                        contador += 1
                    matriz[x][y] = contador                   
                    
                elif x == 0 and y > 0 and y < 19:
                    if bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas [c][0] == x+1 and bombas [c][1] == y-1:
                        contador += 1
                    elif bombas [c][0] == x+1 and bombas [c][1] == y:
                        contador += 1
                    elif bombas [c][0] == x+1 and bombas[c][1] == y+1:
                        contador += 1
                    matriz[x][y] = contador
                    
                elif y == 0 and x > 0 and x < 19:
                    if bombas[c][0] == x-1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y+1:
                        contador += 1    
                    matriz[x][y] = contador
                        
                elif x == 0 and y == 19:
                    if bombas[c][0] == x-1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1  
                    matriz[x][y] = contador
                    
                elif y == 0 and x == 19:
                    if bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1  
                    matriz[x][y] = contador
                    
                elif y == 19 and x == 19:
                    if bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1  
                    matriz[x][y] = contador
                    
                elif x > 0 and x < 19 and y == 19:
                    if bombas[c][0] == x-1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1  
                    matriz[x][y] = contador
                    
                elif y > 0 and y < 19 and x == 19:
                    if bombas[c][0] == x-1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1   
                    elif bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1  
                    matriz[x][y] = contador
                    
    if fim == True:
        matriz[x][y] = "X"
    print("\t=====Campo Minado======\n   \033[34m0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19\033[m")
    
    for i in range (0,len(matriz),1):  
        if(i < 10):     
            print (" \033[34m%s\033[m" %i, end= "") 
        else: 
            print ("\033[34m%s\033[m" %i, end= " ") 
        for j in range(0,len(matriz),1):
            if( i < 10):
                print(" %s "%matriz[i][j], end = "")
            else:
                print("%s "%matriz[i][j], end = " ")
        #print ("%s\n" %i, end= " ")
        print("\n", end="")
    if fim == True:
        print ("\nVocê Perdeu! :C")
        os.system("pause")
        sys.exit(0)
    else:
        if cont >= 360:
            print("\n Você Venceu! :)")
            os.system("pause")
            sys.exit(0)
            
    loops()
    
    
def loop():
    global c1
    global c2  
    if matriz[c1][c2] == "-":
        campo(c1,c2)
    else:
        print("Está casa já esta ocupada!")
        loops()
    c1 += 1
    c2 += 2
    
def loops():
    
    vazio = False
    i = 0
    while i == 0:
        
        posX = input("\nDigite a posicao da Horizontal de ( 0 ) a ( 19 ): ")
        
        try:
            x = int(posX)
            if(x >= 0 and x <= 19):
                i=1
        except:
            print("Jogada invalida")
        
        
        posY = input("\nDigite a posicao da Vertical de ( 0 ) a ( 19 ): ")
            
    j = 0
    while j == 0:
        try:
            y = int(posY)
            if(y >= 0 and y <= 19):
                j = 1
        except:
            print("Jodada Invalida")
    if matriz[x][y] == "-":
        vazio = True
    if vazio:
        campo(x,y)
    else:
        print("Está casa já está ocupada!")
        loop()
def menu():
    print('''
          |============MENU============|
          |[1]Jogar
          |[2]sair
          ''')
    str(input("Escolha uma opção: "))
    
play = 1
sair = 2

menu()
if play: 
    jogar()

if sair:
    print("Você saiu do jogo")
    