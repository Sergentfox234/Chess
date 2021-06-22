class Pawn:
    value = 1

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.firstMove = True
        self.possibleMoves = []
        self.FindPossibleMoves()

    def FindPossibleMoves(self):
        self.possibleMoves = []

        if (self.firstMove):
            if (self.isPlayer):
                self.possibleMoves.append([self.pos[0] - 2, self.pos[1]])
            else:
                self.possibleMoves.append([self.pos[0] + 2, self.pos[1]])
        
        if (self.isPlayer):
            self.possibleMoves.append([self.pos[0] - 1, self.pos[1]])
        else:
            self.possibleMoves.append([self.pos[0] + 1, self.pos[1]])
            
class Rook:
    value = 2
    pos = [0, 0]
    possibleMoves = []

    def __init__(self, position):
        self.pos = position
        self.clicked = False
        self.possibleMoves = []
        self.FindPossibleMoves()

    def FindPossibleMoves(self):
        self.possibleMoves = []

    def PrintMoves(self):
        print(self.possibleMoves)

class Knight:
    value = 3

class Bishop:
    value = 4

class Queen:
    value = 5

class King:
    value = 6