#Proyecto Batalla Naval
#Autores Miguel Angel Montoya y Elno Casiel Guerrero

import random

def printGridCoord():
    gridCoord=[]
    for i in range(10):
        gridAux=[]
        for j in range(10):
            gridAux.append(str(i)+str(j))
        gridCoord.append(gridAux)
    print"\n"
    for fila in gridCoord:
        for coord in fila:
            print coord + "",
        print
    print"\n"



def crearGrid():
    grid=[]
    for i in range(11):
        gridAux=[]
        if i==0:
            gridAux=[" ","0","1","2","3","4","5","6","7","8","9"]
        else:
            for j in range(11):
                if j==0:
                    gridAux.append(str(i-1))
                else:
                    gridAux.append("~")
        grid.append(gridAux)
    return grid


        
def barcos(j,auto):
    for i in range(5,2,-1):
        coord(i,j,auto)
    for i in range(3,0,-1):
        coord(i,j,auto)


        
def coord(barco,j,auto):
    
    aprobacion=False
    while aprobacion==False:
        if auto=="si":
            coordx=random.randint(1,10)
            coordy=random.randint(1,10)
            drccn=random.randint(0,1) #drccn = direccion   1=horizontal 0=vertical
        else:
            correcto1=False
            correcto2=False
            
            while (correcto1==False):
                pregunta="\nEn que coordenadas quiere iniciar su barco de "+str(barco)+" de largo.\nEscriba en formato numerico xy.\n"
                coords=raw_input(str(pregunta).translate(None, ",").translate(None, "'").translate(None, "(").translate(None, ")"))
                
                if len(list(coords))!=2:
                    print "ESCRIBA UNA COORDENADA VALIDA"
                else:
                    list(coords)
                    coordx=(int(coords[0])+1)
                    coordy=(int(coords[1])+1)
                    correcto1=True
                    
                while ((correcto2==False) and (correcto1==True)):
                    drccn=errorNumerico("Escriba (1) si lo quiere vertical o (0) si lo quiere horizontal\n")
                    drccn=int(drccn)
                    if ((drccn==0) or (drccn)==1):
                        correcto2=True
                    else:
                        print "ESCRIBA UNA DIRECCION VALIDA"
        
        if coordx<=4:
            if coordy<=4: #C2
                
                cuadrante=2
                aprobacion=ponerBarco(barco,j,cuadrante,coordx,coordy,drccn,auto)
                
            elif coordy>4: #C3

                cuadrante=3
                aprobacion=ponerBarco(barco,j,cuadrante,coordx,coordy,drccn,auto)
                
        else:
            if coordy>4: #C4
                
                cuadrante=4
                aprobacion=ponerBarco(barco,j,cuadrante,coordx,coordy,drccn,auto)
                
            elif coordy<=4: #C1
                
                cuadrante=1
                aprobacion=ponerBarco(barco,j,cuadrante,coordx,coordy,drccn,auto)
      


def ponerBarco(barco,j,cuadrante,coordx,coordy,drccn,auto):
    
    q1=0    #q1 : x
    q2=0    #q2 : y        #1=horizontal 0=vertical

    if ((cuadrante==2) and (drccn==0)):
        q2=1
    elif ((cuadrante==2) and (drccn==1)):
        q1=1
    elif ((cuadrante==3) and (drccn==0)):
        q2=1
    elif ((cuadrante==3) and (drccn==1)):
        q1=-1
    elif ((cuadrante==4) and (drccn==0)):
        q2=-1
    elif ((cuadrante==4) and (drccn==1)):
        q1=-1
    elif ((cuadrante==1) and (drccn==0)):
        q2=-1
    elif ((cuadrante==1) and (drccn==1)):
        q1=1

    coordUsadasX=[]
    coordUsadasY=[]

    for n in range(barco):    #1=horizontal 0=vertical
        if drccn==1: 

            if (grid[j][coordy+(n*q1)][coordx])=="#":
                coordUsadasX=[]
                coordUsadasY=[]
            else:
                coordUsadasX.append(coordx)
                coordUsadasY.append(coordy+(n*q1))

        elif drccn==0:

            if grid[j][coordy][coordx+(n*q2)]=="#":
                coordUsadasX=[]
                coordUsadasY=[]
            else:
                coordUsadasX.append(coordx+(n*q2))
                coordUsadasY.append(coordy)
                
    if len(coordUsadasX)==barco:
        for z in range(barco):
            insertGrid(coordUsadasX[z],coordUsadasY[z],j)
        if auto=="no":
            prntGrid(j)
        return True

    else:
        if auto=="no":
            print "Se repetira el proceso de insertar coordenada debido a\nuna colision de sus barcos. Pruebe otra coordenada."
        return False



def prntGrid(j):
    print "\n"
    for fila in grid[j]:
        for coord in fila:
            print coord + "",
        print
    print "\n"



def insertGrid(x,y,j):
    grid[j][y][x]="#"



def errorNumerico(a):
    while True:
        try:
            z=raw_input(a)
            q=int(z)
            break
        except ValueError:
            print "CARACTER INAVLIDO: Debe ser un numero"
    return z


def numBarcos(j):
    numBarc=0
    for b,d in enumerate(grid[j]):
        for m,w in enumerate(d):
            if w=="#":
                numBarc+=1
    return numBarc



def disparoIA(j):
    global coordx #Ultima coordenada x usada por la IA
    global coordy #Ultima coordenada y usada por la IA
    global coordsIA #Variable que almacena todas las coordenadas xy usadas por IA
    global coordIAxacierto #Variable que almacena primer coordenada x usada por IA en caso de acierto
    global coordIAyacierto #Variable que almacena primer coordenada y usada por IA en caso de acierto
    global verhorIA #Variable que almacena direccion en caso de acierto
    global numfalloverhor#Variable que almacena cuantas veces se ha equivocado de direccion, solo puede ocurrir si es despues del primer acierto y el maximo numero es 3, ya que habria dado toda l avuelta
    global primeraciertoIA #Variable que almacena si la IA acerto por primera vez. Usada para despues crear una direccion
    global aciertosseguidosIA #Variable que almacena el numero de aciertos seguidos. En caso de ser mayor a 1, convierte el primer acierto en falso
    global verhorA #Almacena opciones verhor (0,1,2)
    global verhorB #Almacena opciones verhor (0,2,3)
    global verhorC #Almacena opciones verhor (1,2,3)
    global verhorD #Almacena opciones verhor (0,1,3)
    global verhorZ #Almacena opciones verhor (1,2)
    global verhorY #Almacena opciones verhor (2,3)
    global verhorX #Almacena opciones verhor (0,3)
    global verhorW #Almacena opciones verhor (0,1)
    global verhorFull #Alamacena opciones verhor (0,1,2,3)
    global verhornuevo #Almacena si se ha cambiado el sentido debido a fin del barco
    global finbarco #Almacena si se ha llegado al fin del barco y hay que cambiar el sentido o si se ha llegado al fin del barco por segunda vez y hay que hacer nuevas coordenadas
    global listabarcos #Lista de barcos existentes
    global specialverhor #Almacena si se esta usando una direccion con rango especial

    if ((aciertosseguidosIA==0)or(finbarco==2)):
        aprobCoords=False
        finbarco=0
        while aprobCoords==False:
            coords=random.randint(1,99)
            if len(list(str(coords)))==1:
                coords=("0"+str(coords))
                
            coords=(str(coords))
            if coords in coordsIA:
                aprobCoords=False
            else:
                coordsIA.append(coords)
                coords=list(coords) 
                coordx=(int(coords[0])+1)
                coordy=(int(coords[1])+1)
                print coordsIA
                aprobCoords=True
        verhorFull=[0,1,2,3]
        verhorA=[0,1,2]
        verhorB=[0,2,3]
        verhorC=[1,2,3]
        verhorD=[0,1,3]
        verhorZ=[1,2]
        verhorY=[2,3]
        verhorX=[0,3]
        verhorW=[0,1]
            
    
    elif aciertosseguidosIA==1:
        #Crear direccion y checar si no esta al borde
        #0=Vertical arriba 1=Horizontal derecha 2=Vertical abajo 3=Horizontal izquierda


        if ((coordIAxacierto==1)and (coordIAyacierto==1)): #Izquierda y arriba no existe
            n=random.randint(0,(1-numfalloverhor)) 
            verhorIA=verhorZ.pop(n)
            specialverhor==2
            
        elif ((coordIAxacierto==10)and (coordIAyacierto==1)): #Derecha y arriba no existe
            n=random.randint(0,(1-numfalloverhor)) 
            verhorIA=verhorY.pop(n)
            specialverhor==2
              
        elif ((coordIAxacierto==10)and (coordIAyacierto==10)): #Derecha y abajo no existe
            n=random.randint(0,(1-numfalloverhor)) 
            verhorIA=verhorX.pop(n)
            specialverhor==2
            
        elif ((coordIAxacierto==1)and (coordIAyacierto==10)): #Izquierda y abajo no existe
            n=random.randint(0,(1-numfalloverhor)) 
            verhorIA=verhorW.pop(n)
            specialverhor==2
              
        elif coordIAxacierto==1: #Horizontal izquierda no existe por estar hasta la izquierda del mapa          
            verhorIA=random.randint(0,(2-numfalloverhor))
            verhor=verhorA.pop(n)
            specialverhor=1

        elif coordIAxacierto==10: #Horizontal derecha no existe por estar hasta la derecha del mapa
            n=random.randint(0,(2-numfalloverhor)) 
            verhorIA=verhorB.pop(n)
            specialverhor==1
                
        elif coordIAyacierto==1: #Vertical arriba no existe por estar hasta arriba del mapa
            n=random.randint(0,(2-numfalloverhor)) 
            verhorIa=verhorC.pop(n)
            specialverhor==1
                
        elif coordIAyacierto==10: #Vertical abajo no existe por estar hasta abajo del mapa
            n=random.randint(0,(2-numfalloverhor)) 
            verhorIA=verhorD.pop(n)
            specialverhor==1
        else: #Todas las opciones ya que no esta en el borde
            n=random.randint(0,(3-numfalloverhor))
            print n
            
            verhorIA=verhorFull.pop(n)
            specilaverhor=0


        if verhorIA==0:
            coordx=coordIAxacierto
            coordy=coordIAyacierto-1
        elif verhorIA==1:
            coordx=coordIAxacierto+1
            coordy=coordIAyacierto
        elif verhorIA==2:
            coordx=coordIAxacierto
            coordy=coordIAyacierto+1
        elif verhorIA==3:
            coordx=coordIAxacierto-1
            coordy=coordIAyacierto

        coords=str(coordx-1)+str(coordy-1)
        coordsIA.append(coords)
        print coordsIA

        

    elif aciertosseguidosIA>1:
        check=False
        while check==False:
            if (finbarco==0)or(verhornuevo==True):
                if verhorIA==0:
                    coordx=coordx
                    coordy=coordy-1
                elif verhorIA==1:
                    coordx=coordx+1
                    coordy=coordy
                elif verhorIA==2:
                    coordx=coordx
                    coordy=coordy+1
                elif verhorIA==3:
                    coordx=coordx-1
                    coordy=coordy
            elif finbarco==1:

                                
                if verhorIA==0:
                    verhorIA=2
                    coordx=coordIAxacierto
                    coordy=coordIAyacierto+1
                elif verhorIA==1:
                    verhorIA=3
                    coordx=coordIAxacierto-1
                    coordy=coordIAyacierto
                elif verhorIA==2:
                    verhorIA=0
                    coordx=coordIAxacierto
                    coordy=coordIAyacierto-1
                elif verhorIA==3:
                    verhorIA=1
                    coordx=coordIAxacierto+1
                    coordy=coordIAyacierto
                verhornuevo=True
                coords=str(coordx-1)+str(coordy-1)

                if coords in coordsIA:
                    finbarco=2

            if finbarco==2:
                print coords
                finbarco=0
                aprobCoords=False
                while aprobCoords==False:
                    coords=random.randint(1,99)
                    if len(list(str(coords)))==1:
                        coords=("0"+str(coords))
                        
                    coords=(str(coords))
                    if coords in coordsIA:
                        aprobCoords=False
                    else:
                        coords=list(coords)

                        
                        coordx=(int(coords[0])+1)
                        coordy=(int(coords[1])+1)

                        numfalloverhor=0
                        aprobCoords=True
                    
                verhorFull=[0,1,2,3]
                verhorA=[0,1,2]
                verhorB=[0,2,3]
                verhorC=[1,2,3]
                verhorD=[0,1,3]
                verhorZ=[1,2]
                verhorY=[2,3]
                verhorX=[0,3]
                verhorW=[0,1]
                            
                            
            if ((coordx==0)or(coordx==11)or(coordy==0)or(coordy==11)):
                if verhornuevo==True:
                    finbarco=2
                else:
                    finbarco=1
            else:
                check=True

                
        coords=str(coordx-1)+str(coordy-1)
        coordsIA.append(coords)


    #Fallo
    if grid[j] [coordy] [coordx]=="~": #Tablero enemigo
        grid[j] [coordy] [coordx]="O"

        print "La IA ha fallado"

        if finbarco==1: #Si se equivoca cuando ya se habia equivocado 3 veces en la direccion, o cuando llega al fin del barco y el inicio era otro extremo, genera nuevas coordenadas
            finbarco+=1
            listabarcos.remove(aciertosseguidosIA)
            aciertosseguidosIA=0
                
        else:
            if aciertosseguidosIA>=2: #Si falla pero habia acertado dos o mas veces, se considera que es el fin del barco, y se prueba en la direccion opuesta
                finbarco=1
            elif aciertosseguidosIA==1: #Si falla despues del primer acierto, se agrega un error al intentar hayar la direccion
                numfalloverhor+=1

        raw_input()
        return True

    #Acierto
    elif grid[j] [coordy] [coordx]=="#": #Tablero enemigo
        grid[j] [coordy] [coordx]="X"   #Tablero enemigo

        print"La IA a acertado"
        
        aciertosseguidosIA+=1
        if aciertosseguidosIA==1: #Si es el primer acierto se guarda como la coordenada de primer acierto
            coordIAxacierto=coordx
            coordIAyacierto=coordy
        if (numfalloverhor==3): #Si ya se equivoco 3 veces en la direccion, y acierta resetea los errores de direccion y sigue probando
            numfalloverhor=0
        if aciertosseguidosIA==max(listabarcos): #Si los aciertos seguidos son iguales al barco mas grande que reste, genera nuevas coordenadas
            listabarcos.remove(aciertosseguidosIA)
            aciertosseguidosIA=0
            numfalloverhor=0
        
        raw_input()
        return True
    else:
        finbarco=1
        return False
    

            

def disparo(j):   
    try:
        coords=errorNumerico("coordenadas de disparo!: ")
        list(coords)
        coordx=(int(coords[0])+1)
        coordy=(int(coords[1])+1)
    except IndexError:
        print "CARACTER INAVLIDO: Debe ser dos coordenadas"
        
    if len(coords)!=2:
        print "ESCRIBA UNA COORDENADA VALIDA"
        return False

    #Fallo
    elif grid[j] [coordy] [coordx]=="~": #Tablero enemigo
        grid[j+1] [coordy] [coordx]="O" #Radar atacante
        print "\n"*60
        print "FALLO!"
        return True
    #Acierto
    elif grid[j] [coordy] [coordx]=="#": #Tablero enemigo
        grid[j] [coordy] [coordx]="X"   #Tablero enemigo
        grid[j+1] [coordy] [coordx]="X" #Radar atacante
        print "\n"*60
        print "ACIERTO!!!"
        return True

    else:
        print "Ya habia disparado en este lugar!"
        return False



        
#def funciondesconocida():
    #for n,i in enumerate(grid):
        #for m,j in enumerate(i):
            #if j=="#":
                #grid [n][m]="X"



#INICIA EL PROGRAMA   INICIA EL PROGRAMA   INICIA EL PROGRAMA   INICIA EL PROGRAMA   
grid=[0,1,2,3] #Item 0 = Mapa J1 || Item 1 = Radar J2 || Item 2 = Mapa J2 || Item 3 = Radar J1
rep="si"

while rep=="si":
    print "Bienvenido! Programa creado por Miguel Angel Montoya y Elno Casiel Guerrero", " \n"*2
    print "EN ESTE AVANCE SOLO FUNCIONA EL MODO CON DOS JUGADORES. EL MODO DE UN JUGADOR NO FUNCIONA CORRECTAMENTE(ERRORES CON AI EN DISPAROS)"
    print "Este es un juego de batalla naval, similar al buscaminas", " \n"*2,"Este es el tablero de coordenadas"

    check=False
    while check==False:
        AIJ=errorNumerico("De cuantos jugadores humanos sera el juego? (1/2)\n")
        if ((AIJ=="1")or(AIJ=="2")):
            check=True
        else:
            print "Ponga un numero valido"

    #Barcos J1
    j=0
    grid[j]=crearGrid()
    autoBarco=raw_input("J1: Quiere que se acomoden sus barcos automaticamente?\nEscriba si o no. Si escribe no, usted los acomodara\n").lower()
    if autoBarco=="si":
        barcos(j,"si")
    else:
        reacomodo="no"
        while reacomodo=="no":
            barcos(j,"no")
            reacomodo=raw_input("J1: Esta seguro de esta colococacion?, escriba si o no\n")
            if reacomodo=="no":
                grid[j]=crearGrid()
    prntGrid(j)
        
    #Con IA
    if AIJ=="1":
        raw_input("J1: Escriba OK para comenzar")
        j=2
        grid[j]=crearGrid()
        barcos(j,"si")

    #Con humano
    elif AIJ=="2":
        raw_input("Presione ENTER y asegurese de que el J2 este enfrente de la pantalla\n")
        print "\n"*60
    
        #BarcosJ2
        raw_input("Presione ENTER")
        print "\n"*60
        j=2
        grid[j]=crearGrid()
        autoBarco=raw_input("J2: Quiere que se acomoden sus barcos automaticamente?\nEscriba si o no. Si escribe no, usted los acomodara\n").lower()
        if autoBarco=="si":
            barcos(j,"si")
        else:
            printGridCoord()
            reacomodo="no"
            while reacomodo=="no":
                barcos(j,"no")
                reacomodo=raw_input("J2: Esta seguro de esta colococacion?, escriba si o no\n")
                if reacomodo=="no":
                    grid[j]=crearGrid()
        print"J2: Este es su tablero"
        prntGrid(j)

        ##
        ADMIN=raw_input("Escriba OK y asegurese de que el J1 este enfrente de la pantalla\n") #Terminar ADMIN
        if ADMIN=="end":
                for n,i in enumerate(grid[0]):
                    for m,j in enumerate(i):
                        if j=="#":
                            grid[0][n][m]="X"
        ##
                            
        print "\n"*60
        raw_input("Presione ENTER")
        print "\n"*60

    grid[3]=crearGrid()
    grid[1]=crearGrid()

    
    #Disparos
    coordx=0
    coordy=0
    coordsIA=[] #Variable que almacena todas las coordenadas xy usadas por la IA
    coordIAxacierto=0 #Variable que almacena coordenada x usada por IA en caso de acierto
    coordIAyacierto=0 #Variable que almacena coordenada y usada por IA en caso de acierto
    verhorIA=0 #Variable que almacena direccion en caso de acierto
    numfalloverhor=0#Variable que almacena cuantas veces se ha equivocado de direccion, solo puede ocurrir si es despues del primer acierto y el maximo numero es 3, ya que habria dado toda l avuelta
    primeraciertoIA=False #Variable que almacena si la IA acerto por primera vez. Usada para despues crear una direccion
    aciertosseguidosIA=0 #Variable que almacena el numero de aciertos seguidos. En caso de ser mayor a 1, convierte el primer acierto en falso
    verhorA=[0,1,2] #Almacena opciones verhor (0,1,2)
    verhorB=[0,2,3] #Almacena opciones verhor (0,2,3)
    verhorC=[1,2,3] #Almacena opciones verhor (1,2,3)
    verhorD=[0,1,3] #Almacena opciones verhor (0,1,3)
    verhorZ=[1,2] #Almacena opciones verhor (1,2)
    verhorY=[2,3] #Almacena opciones verhor (2,3)
    verhorX=[0,3] #Almacena opciones verhor (0,3)
    verhorW=[0,1] #Almacena opciones verhor (0,1)
    verhorFull=[0,1,2,3] #Alamacena opciones verhor (0,1,2,3)
    verhornuevo=False #Almacena si se ha cambiado el sentido debido a fin del barco
    finbarco=0 #Almacena si se ha llegado al fin del barco y hay que cambiar el sentido o si se ha llegado al fin del barco por segunda vez y hay que hacer nuevas coordenadas
    listabarcos=[1,2,3,3,4,5] #Lista de barcos existentes
    specialverhor=False #Almacena si se esta usando una direccion con rango especial
    turnos=0
    

    
    while (numBarcos(0)!=0 and numBarcos(2)!=0):
        J1=False
        J2=False
        
        if (numBarcos(2)!=0):
            print "\n"*10+"J1   J1   J1   J1   J1   J1   J1   J1   J1   J1"
            j=2
            print "Este es tu radar:"
            prntGrid(j+1)
            print "Este es tu tablero:"
            prntGrid(j-2)

            while J1==False:
                J1=disparo(j)

            print "Este es tu radar:"
            prntGrid(j+1)

            print "Este es tu tablero:"
            prntGrid(j-2)
            if AIJ=="2":
                raw_input("Escriba OK y asegurese de que el J2 este enfrente de la pantalla.\n")
                print "\n"*60
                raw_input("Presione ENTER")
                print "\n"*60
            


        if (numBarcos(0)!=0):
            j=0
            if AIJ=="2":
                print "J2   J2   J2   J2   J2   J2   J2   J2   J2   J2"
                
                print "Este es tu radar:"
                prntGrid(j+1)
                print "Este es tu tablero:"
                prntGrid(j+2)
                while J2==False:
                    J2=disparo(j)

                print "Este es tu radar:"
                prntGrid(j+1)

                print "Este es tu tablero:"
                prntGrid(j+2)
                raw_input("Escriba OK y asegurese de que el J1 este enfrente de la pantalla.\n")
                print "\n"*60
                raw_input("Presione ENTER")
                print "\n"*60
            else:
                while J2==False:
                    J2=disparoIA(j)
                    turnos+=1
                    print turnos

                
    if numBarcos(0)==0:
        if AIJ=="1":
            print "La Inteligencia Artificial ha ganado!"
        else:
            print "FELICIDADES J2, GANASTE!!!"
            print " \n","J2"*100
    else:
        print "FELICIDADES J1, GANASTE!!!"
        print " \n","J1"*100
    rep=raw_input("Quiere volver a jugar? Escriba si o no").lower()
