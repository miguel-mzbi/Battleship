# pylint: disable=C0103
# pylint: disable=C0301
# pylint: disable=C0111

# Project Battleship
# Authors Miguel Angel Montoya & Elno Casiel Guerrero on April 2015
# Refactored by Miguel Angel Montoya on March 2019

import random
import os

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

    def placeShip(self, x, y, direction, length):
        if direction == 0:
            for yT in range(y, y+length):
                self.setCoord(x, yT, "#")
        else:
            for xT in range(x, x+length):
                self.setCoord(xT, y, "#")

    def getShipSpacesRemaining(self):
        counter = 0
        for j in range(10):
            for i in range(10):
                if self.getCoord(i, j) == "#":
                    counter += 1
        return counter

    def printGrid(self):
        for j in range(-1, 10):
            if j == -1:
                if self.mapType == 0:
                    print("y\\x 0  1  2  3  4  5  6  7  8  9")
                else:
                    print("y\\x 0 1 2 3 4 5 6 7 8 9")
            else:
                row = ""
                for i in range(-1, 10):
                    if i == -1:
                        row += str(j) + "   "
                    else:
                        row += self.getCoord(i, j) + " "
                print(row)

class Player:
    def __init__(self, name):
        self.name = name
        self.map = Grid(1)
        self.radar = Grid(2)

    def getShipsRemaining(self):
        return self.map.getShipSpacesRemaining()

    def printMap(self):
        self.map.printGrid()

    def printRadar(self):
        self.radar.printGrid()

    def printBoth(self):
        print("Este es tu radar.")
        self.printRadar()
        print("Este es tu tablero.")
        self.printMap()

    def shipsSetup(self):
        clearTerminal(self.name)
        print(f"ASEGURATE QUE EL JUGADOR {self.name} ESTÁ VIENDO LA PANTALLA. ES SU TURNO DE ACOMODAR BARCOS.")
        autoShips = checkInputText(f"J{self.name}: Quiere que se acomoden sus barcos automaticamente?\nSi escribe no, usted los acomodara (si/no): ", ["si", "no"]) == "si"
        self.placeAllShips(autoShips)
        clearTerminal(self.name)
        self.printMap()
        input("PRESIONE CUALQUIER TECLA PARA CONTINUAR... ")

    def placeAllShips(self, isRandom=False):
        lengths = [5, 4, 3, 3, 2, 1]
        for length in lengths:
            if isRandom:
                self.placeShipRandom(length)
            else:
                self.placeShip(length)

    def placeShipRandom(self, length):
        def getRandomCoords(length):
            # Direction 0 = vertical, 1 = horizontal
            direction = random.randint(0, 1)
            # If ship is horizontal, leftmost coord for ship must be in range (0, 10-l) so the ship can fit
            x = random.randint(0, 10-(length if direction == 1 else 1))
            # If ship is vertical, upmost coord for ship must be in range (0, 10-l) so the ship can fit
            y = random.randint(0, 10-(length if direction == 0 else 1))
            return (x, y, direction)

        x, y, direction = getRandomCoords(length)

        available = False
        while not available:
            available = True
            if direction == 0:
                for yT in range(y, y+length):
                    if self.map.getCoord(x, yT) != "~":
                        available = False
                        break
            else:
                for xT in range(x, x+length):
                    if self.map.getCoord(xT, y) != "~":
                        available = False
                        break
            if not available:
                x, y, direction = getRandomCoords(length)

        self.map.placeShip(x, y, direction, length)

    def confirmShip(self, length, x, y, direction):
        available = True
        print()
        for t in range(y, y+length) if direction == 0 else range(x, x+length):
            if direction == 0:
                self.map.setCoord(x, t, "&")
            else:
                self.map.setCoord(t, y, "&")
        self.printMap()
        available = checkInputText("Confirmar posición (si/no): ", ["si", "no"]) == "si"
        if not available:
            for t in range(y, y+length) if direction == 0 else range(x, x+length):
                if direction == 0:
                    self.map.setCoord(x, t, "~")
                else:
                    self.map.setCoord(t, y, "~")
        return available

    def placeShip(self, length):

        clearTerminal(self.name)
        self.printMap()

        def getUserCoords(length):
            print("\nSeleccione la coordenada inicial y dirección para el barco de tamaño", length, ".\nLos barcos crecen a la derecha o hacia abajo de la coordenada inicial.")
            x = checkInputNumber("Por favor inserta la coordenada x: ", list(range(10)))
            y = checkInputNumber("Por favor inserta la coordenada y: ", list(range(10)))
            direction = checkInputNumber("Por favor selecciona la dirección (0 = Vertical/1 = Horizontal): ", list(range(2)))
            return (x, y, direction)

        x, y, direction = getUserCoords(length)

        available = False
        while not available:
            available = True
            if direction == 0:
                for yT in range(y, y+length):
                    if yT < 0 or yT > 9 or x < 0 or x > 9 \
                        or self.map.getCoord(x, yT) != "~":
                        available = False
                        print("\nPor favor, elija una coordenada dónde el barco pueda ser colocado.")
                        break

            else:
                for xT in range(x, x+length):
                    if xT < 0 or xT > 9 or y < 0 or y > 9 \
                        or self.map.getCoord(xT, y) != "~":
                        available = False
                        print("\nPor favor, elija una coordenada dónde el barco pueda ser colocado.")
                        break

            # Confirm position
            if available:
                available = self.confirmShip(length, x, y, direction)

            if not available:
                x, y, direction = getUserCoords(length)

        self.map.placeShip(x, y, direction, length)
        self.printMap()

    def shoot(self, otherPlayer):
        print("\nSeleccione la coordenada para disparar.")
        x = checkInputNumber("Por favor inserta la coordenada x: ", list(range(10)))
        y = checkInputNumber("Por favor inserta la coordenada y: ", list(range(10)))

        clearTerminal(self.name)
        # Success
        if otherPlayer.map.getCoord(x, y) == "#":
            otherPlayer.map.setCoord(x, y, "X")
            self.radar.setCoord(x, y, "X")
            print("ACIERTO!")
        elif otherPlayer.map.getCoord(x, y) == "X":
            print("YA HABÍAS ACERTADO AHÍ!!")
        else: # FAIL
            self.radar.setCoord(x, y, "O")
            print("FALLO!")

class PlayerAI(Player):
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

    def addCoord(self, x, y):
        self.usedCoords.append((x, y))

    def hasUsedCoord(self, mx, my):
        for x, y in self.usedCoords:
            if x == mx and y == my:
                return True
        return False

    def getRandomCoord(self):
        coordsNotUsed = False
        while not coordsNotUsed:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            coordsNotUsed = not self.hasUsedCoord(x, y)
        return (x, y)

    def shoot(self, otherPlayer):

        def cleanFail(x, y):
            self.radar.setCoord(x, y, "O")
            otherPlayer.map.setCoord(x, y, "O")
            print("FALLO DE LA IA!")

        def cleanSuccess(x, y):
            print("ACIERTO DE LA IA!")
            otherPlayer.map.setCoord(x, y, "X")
            self.radar.setCoord(x, y, "X")
            self.lastSuccessCoord = (x, y)
            self.isCompletingShip = True

        def getNextCoordToTry():
            lastX, lastY = self.lastSuccessCoord
            # Direction unknown
            if self.currentFoundLength == 1:
                # Try left
                if lastX > 0 and self.radar.getCoord(lastX-1, lastY) == "~":
                    return (lastX-1, lastY)
                # Try right
                if lastX < 9 and self.radar.getCoord(lastX+1, lastY) == "~":
                    return (lastX+1, lastY)
                # Try up
                if lastY > 0 and self.radar.getCoord(lastX, lastY-1) == "~":
                    return (lastX, lastY-1)
                # Try down
                if lastY < 9 and self.radar.getCoord(lastX, lastY+1) == "~":
                    return (lastX, lastY+1)
                # Surrounded, found ship of length 1
                self.isCompletingShip = False
                self.enemyFoundShips.append(1)
                return self.getRandomCoord()
            # If there can be still a bigger ship
            if self.currentFoundLength < 5:
                # If direction is horizontal
                if self.currentDirection == 1:
                    minX, minY = min(self.coordsCurrentFoundShip, key=lambda x: x[0])
                    maxX, maxY = max(self.coordsCurrentFoundShip, key=lambda x: x[0])
                    # Try one smaller x
                    if minX-1 >= 0 and self.radar.getCoord(minX-1, minY) == "~":
                        return (minX-1, minY)
                    # Try one bigger x
                    if maxX+1 <= 9 and self.radar.getCoord(maxX+1, maxY) == "~":
                        return (maxX+1, maxY)
                # If direction is vertical
                if self.currentDirection == 0:
                    minX, minY = min(self.coordsCurrentFoundShip, key=lambda x: x[1])
                    maxX, maxY = max(self.coordsCurrentFoundShip, key=lambda x: x[1])
                    # Try one smaller y
                    if minY-1 >= 0 and self.radar.getCoord(minX, minY-1) == "~":
                        return (minX, minY-1)
                    # Try one bigger y
                    if maxY+1 <= 9 and self.radar.getCoord(maxX, maxY+1) == "~":
                        return (maxX, maxY+1)
            # Try elsewhere
            self.enemyFoundShips.append(self.currentFoundLength)
            self.isCompletingShip = False
            return self.getRandomCoord()

        clearTerminal(otherPlayer.name)

        if not self.isCompletingShip:
            x, y = self.getRandomCoord()
        else:
            x, y = getNextCoordToTry()

        if not self.isCompletingShip:
            if otherPlayer.map.getCoord(x, y) == "#":
                cleanSuccess(x, y)
                self.currentFoundLength = 1
                self.coordsCurrentFoundShip = [(x, y)]
            else: # FAIL
                cleanFail(x, y)
        else:
            # Only found 1
            if self.currentFoundLength == 1:
                #If success, infer direction
                if otherPlayer.map.getCoord(x, y) == "#":
                    cleanSuccess(x, y)
                    self.currentDirection = 0 if self.lastSuccessCoord[0] - x == 0 else 1
                    self.currentFoundLength = 2
                    self.coordsCurrentFoundShip.append((x, y))
                # Else, keep looking on surrounding places
                else:
                    cleanFail(x, y)
            # Already found more than 1
            else:
                #If success, continue direction
                if otherPlayer.map.getCoord(x, y) == "#":
                    cleanSuccess(x, y)
                    self.currentFoundLength += 1
                    self.coordsCurrentFoundShip.append((x, y))
                # Else, keep looking on surrounding places
                else:
                    cleanFail(x, y)

        self.addCoord(x, y)

def clearTerminal(playerName):
    os.system('cls' if os.name == 'nt' else 'clear')
    if playerName == 1:
        print("J1\tJ1\tJ1\tJ1\tJ1\tJ1")
    else:
        print("J2\tJ2\tJ2\tJ2\tJ2\tJ2")

def checkInputNumber(text, options):
    valid = False
    while not valid:
        res = input(text)
        try:
            res = int(res)
            if res in options:
                valid = True
        except ValueError:
            pass
    return res

def checkInputText(text, options):
    valid = False
    while not valid:
        res = input(text).lower()
        if res in options:
            valid = True
    return res


#INICIA EL PROGRAMA   INICIA EL PROGRAMA   INICIA EL PROGRAMA   INICIA EL PROGRAMA
if __name__ == "__main__":
    clearTerminal(1)
    player1 = Player(1)

    playAgain = True
    while playAgain:

        print("Bienvenido! Programa creado por Miguel Angel Montoya y Elno Casiel Guerrero\nEste es un juego de batalla naval, donde puede jugar contra otro humano o una IA\n\nEste es el tablero del coordenadas:")
        Grid(0).printGrid()

        print()
        isPlayerAI = checkInputText("Planea jugar contra una IA (si/no): ", ["si", "no"]) == "si"
        player2 = PlayerAI(2) if isPlayerAI else Player(2)

        # Player 1 ship setup
        player1.shipsSetup()

        if isPlayerAI:
            clearTerminal(1)
            print("ACOMODANDO BARCOS DE IA AUTOMATICAMENTE...")
            player2.placeAllShips(True)
        else:
            player2.shipsSetup()

        player1Turn = True
        playerPlaying = None
        playerOther = None
        while player1.getShipsRemaining() > 0 and player2.getShipsRemaining() > 0:

            if player1Turn:
                playerPlaying = player1
                playerOther = player2
            else:
                playerPlaying = player2
                playerOther = player1

            if not isPlayerAI:
                clearTerminal(playerPlaying.name)
                print(f"ASEGURATE QUE EL JUGADOR {playerPlaying.name} ESTÁ VIENDO LA PANTALLA. ES SU TURNO DE DISPARAR.")
                input("PRESIONE CUALQUIER TECLA PARA CONTINUAR... ")
                clearTerminal(playerPlaying.name)

            if player1Turn or not isPlayerAI:
                playerPlaying.printBoth()
            playerPlaying.shoot(playerOther)

            if player1Turn or not isPlayerAI:
                playerPlaying.printBoth()
                input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR... ")

            if playerPlaying.getShipsRemaining() == 0:
                print(f"VICTORIA DEL JUGADOR {playerPlaying.name}!")
                clearTerminal(playerOther.name)
                break

            player1Turn = not player1Turn

        playAgain = checkInputText("Desea jugar de nuevo? (si/no): ", ["si", "no"]) == "si"
        if playAgain:
            player1 = Player(1)
