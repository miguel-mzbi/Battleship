# Assignment: Refactoring

Miguel Angel Montoya - A01226045

## Basic steps

The first thing to do was to upgrade the code from python 2 to python 3.

## Renaming of variables

There are simply no words to define the mess the pre-refactored code had regarding naming of functions and variables.
Not even the simple convention of naming i and j (Player index over the array was j for 'jugador'.
This issue of the array containing everything it's explained later) for iteration over x and y was followed.

```Python
# SELECTED PARTS OF THE PRE-REFACTORED CODE
verhorA=[0,1,2] #Almacena opciones verhor (0,1,2)
verhorB=[0,2,3] #Almacena opciones verhor (0,2,3)
verhorC=[1,2,3] #Almacena opciones verhor (1,2,3)
verhorD=[0,1,3] #Almacena opciones verhor (0,1,3)
verhorZ=[1,2] #Almacena opciones verhor (1,2)
verhorY=[2,3] #Almacena opciones verhor (2,3)
verhorX=[0,3] #Almacena opciones verhor (0,3)
verhorW=[0,1] #Almacena opciones verhor (0,1)
```

Now variables hae for informative names, which also makes the necessity for uninformative comments disappear.

```Python
# SELECTED PARTS OF THE REFACTORED CODE
self.enemyFoundShips = []
self.usedCoords = []
# Either if looking for a ship on an area a shot was successful
self.isCompletingShip = False
self.currentFoundLength = 0
self.coordsCurrentFoundShip = []
self.currentDirection = -1
self.lastSuccessCoord = ()
```

## Creation of classes

In the previous code there wasn't any type of classes to store the grids that belong to a player, neither methods to apply over those grids.
Grids were store in an array that contained in radar and map for both players.

```Python
# SELECTED PARTS OF THE PRE-REFACTORED CODE
grid=[0,1,2,3] #Item 0 = Mapa J1 || Item 1 = Radar J2 || Item 2 = Mapa J2 || Item 3 = Radar J1

j=0
grid[j]=crearGrid()

if grid[j][coordy][coordx]=="~": #Tablero enemigo
    grid[j][coordy][coordx]="O"
    print "La IA ha fallado"

def prntGrid(j):
    print "\n"
    for fila in grid[j]:
        for coord in fila:
            print coord + "",
        print
    print "\n"
```

The variable grid was global, contained data about different types of data about different players.
It was basically a 3D array were the first dimension was the player and type, then the y and finally the x.
Those grids were modified by functions that received the index of the array to modify.
Now the class player has a map and a radar as attributes, and functions that already know what grid to apply the changes.
Also The class grid exists, it has a print, and multiple setters and getters. Previously the changes were applied directly onto the grid.

```Python
# SELECTED PARTS OF THE REFACTORED CODE
class Grid:
    def __init__(self, mapType):
        self.mapType = mapType # 0 = coords, 1 = map, 2 = radar
        self.grid = [["~" for _ in range(10)] for _ in range(10)]
        for i in range(10):
            for j in range(10):
                self.setCoord(i, j, str(i) + str(j) if mapType == 0 else "~")

    def setCoord(self, i, j, val):
        self.grid[j][i] = val

    def getCoord(self, i, j):
        return self.grid[j][i]

class Player:
    def __init__(self, name):
        self.name = name
        self.map = Grid(1)
        self.radar = Grid(2)

    def printMap(self):
        self.map.printGrid()

    def printRadar(self):
        self.radar.printGrid()
```

## Extension of classes

Python it's not the best language to demonstrate OOP concepts. But still, extension of classes and overriding was used when refactoring.
Previously there wasn't any kind of distinction between a player and the AI (Mainly because the players were indexes of an array).
When doing functions that were available only to the AI the logic was separated via if else conditions.

```Python
# SELECTED PARTS OF THE PRE-REFACTORED CODE
# Global variables simulating what would be attributes of the PlayerAI class.
# There are +40 like these in the complete
global aciertosseguidosIA #Variable que almacena el numero de aciertos seguidos. En caso de ser mayor a 1, convierte el primer acierto en falso
global verhorA #Almacena opciones verhor (0,1,2)
global verhorB #Almacena opciones verhor (0,2,3)
global verhorC #Almacena opciones verhor (1,2,3)
global verhorD #Almacena opciones verhor (0,1,3)
# . . .

if AIJ=="2": # I'm guessing that when AIJ was equal to 2 it meant player 2 was an AI
   # Code for player 2
else:
    # Code for player 2 AI
    # Actual functionality of the while loop is unknown
    while J2==False:
        J2=disparoIA(j)
        turnos+=1
        print turnos
```

In the refactored code there is a class called PlayerAI that extends Player and overrides some player methods.
It also adds some attributes to store data about the shotting behavior. Previously these attributes were stored via global variables.
These new attributes weren't needed by the regular player.

```Python
# SELECTED PARTS OF THE REFACTORED CODE
class Player:
    def __init__(self, name):
        # Init
    def shoot(self, otherPlayer):
        # Player A shoots player B
class PlayerAI(Player):
    # Note that all of the +40 variables were substituted by 7 attributes.
    def __init__(self, name):
        super().__init__(name)
        self.enemyFoundShips = []
        self.usedCoords = []
        # Either if looking for a ship on an area a shot was successful
        self.isCompletingShip = False
        self.currentFoundLength = 0
        self.coordsCurrentFoundShip = []
        self.currentDirection = -1
        self.lastSuccessCoord = ()
    def shoot(self, otherPlayer):
        # AI shoots other player
```

## Creation of functions

Code that was being repeated now it's being executed by multiple functions.
One of the pieces of code that was used the most was the validate input. It was badly implemented and used differently everywhere.

In some cases if the user didn't select an exact option, it was used for him.
For example, if the user didn't write "si", it was assumed it was a "no".

In other cases the input wasn't even being processed. The input didn't matter, the code was going to get executed either way.

```Python
# SELECTED PARTS OF THE PRE-REFACTORED CODE
autoBarco=input("J1: Quiere que se acomoden sus barcos automaticamente?\nEscriba si o no. Si escribe no, usted los acomodara\n").lower()
if autoBarco=="si":
    barcos(j,"si")
else:
    reacomodo="no"
    # Code when autoBarco isn't equal to "si"

input("J1: Escriba OK para comenzar")
barcos(j,"si")

while rep=="si":
    # Code for the game
    rep=input("Quiere volver a jugar? Escriba si o no").lower()
```

Now there is a unique function fro making sure the input corresponds to one of the options.
The function return a selected valid option that can be tested to produce a true/false value.

```Python
# SELECTED PARTS OF THE REFACTORED CODE
def checkInputText(text, options):
    valid = False
    while not valid:
        res = input(text).lower()
        if res in options:
            valid = True
    return res

playAgain = checkInputText("Desea jugar de nuevo? (si/no): ", ["si", "no"]) == "si"
```

## Results

It's not the best option to evaluate the success of the refactoring, but after translating the pre-refactor code to python 3,
I run it through pylint. It got a -4.8/10 score. After doing the refactoring, the code obtained a 9.93/10.
The only rules not taking into account for both codes were the "lines longer than x characters", "missing docstrings over functions"
and variable names not corresponding to a case standard.