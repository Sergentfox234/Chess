class Pawn:
    value = 1

    #def __init__(self, position, isP, board):
    #    self.pos = position
    #    self.isPlayer = isP
    #    self.clicked = False
     #   self.firstMove = True
     #   self.enPessentable = False
     #   self.possibleMoves = []
     #   self.FindPossibleMoves(board)

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.firstMove = True
        self.enPessentable = False
        self.possibleMoves = []
        self.FindFirstMoves()

    def MoveTo(self, position, board, oppositePieces):
        # Check for enpessentability
        if self.isPlayer and self.firstMove and position[0] == self.pos[0] - 2:
            self.enPessentable = True
            print("enPessentable!!")
        elif self.isPlayer:
            self.enPessentable = False
            print("Nope")
        elif not(self.isPlayer) and self.firstMove and position[0] == self.pos[0] + 2:
            self.enPessentable = True
            print("enPessentable!!")
        elif not(self.isPlayer):
            self.enPessentable = False
            print("Nope")

        self.pos = position
        self.clicked = False
        self.firstMove = False
        
        for piece in oppositePieces:
            if piece.pos == self.pos:
                oppositePieces.remove(piece)

        self.FindPossibleMoves(board, oppositePieces)

    def FindFirstMoves(self):
        self.possibleMoves = []

        # Starting board, no blocking pieces
        if self.firstMove:
            if self.isPlayer:
                self.possibleMoves.append([self.pos[0] - 2, self.pos[1]])
            else:
                self.possibleMoves.append([self.pos[0] + 2, self.pos[1]])
        
        if self.isPlayer:
            self.possibleMoves.append([self.pos[0] - 1, self.pos[1]])
        else:
            self.possibleMoves.append([self.pos[0] + 1, self.pos[1]])
    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []

        # If first move && there is nothing blocking
        if self.firstMove:
            if self.isPlayer and board[self.pos[0] - 1, self.pos[1]] == 0 and board[self.pos[0] - 2, self.pos[1]] == 0:
                self.possibleMoves.append([self.pos[0] - 2, self.pos[1]])
            elif not(self.isPlayer) and board[self.pos[0] + 1, self.pos[1]] == 0 and board[self.pos[0] + 2, self.pos[1]] == 0:
                self.possibleMoves.append([self.pos[0] + 2, self.pos[1]])
        
        # If not first move && there is nothing blocking
        if self.isPlayer and board[self.pos[0] - 1, self.pos[1]] == 0:
            self.possibleMoves.append([self.pos[0] - 1, self.pos[1]])
        elif not(self.isPlayer) and board[self.pos[0] + 1, self.pos[1]] == 0:
            self.possibleMoves.append([self.pos[0] + 1, self.pos[1]])
        
        # If the pawn can ATTACK to the left
        if self.isPlayer and self.pos[1] > 0 and board[self.pos[0] - 1, self.pos[1] - 1] >= 10:
            self.possibleMoves.append([self.pos[0] - 1, self.pos[1] - 1])

        # If the pawn can ATTACK to the right 
        if self.isPlayer and self.pos[1] < 7 and board[self.pos[0] - 1, self.pos[1] + 1] >= 10:
            self.possibleMoves.append([self.pos[0] - 1, self.pos[1] + 1])

        # If enpessent to the left
        if self.isPlayer and board[self.pos[0], self.pos[1] - 1] == 11:
            for possPiece in oppositePieces:
                if possPiece.pos == [self.pos[0], self.pos[1] - 1] and possPiece.enPessentable:
                    self.possibleMoves.append([self.pos[0] - 1, self.pos[1] - 1])
            
class Rook:
    value = 2

    def __init__(self, position):
        self.pos = position
        self.clicked = False
        self.possibleMoves = []
        self.FindPossibleMoves()

    def FindPossibleMoves(self):
        self.possibleMoves = []

class Knight:
    value = 3

    def __init__(self, position):
        self.pos = position
        self.clicked = False
        self.possibleMoves = []
        self.FindPossibleMoves()
    
    def FindPossibleMoves(self):
        self.possibleMoves = []

class Bishop:
    value = 4

    def __init__(self, position):
        self.pos = position
        self.clicked = False
        self.possibleMoves = []
        self.FindPossibleMoves()

    def FindPossibleMoves(self):
        self.possibleMoves = []

class Queen:
    value = 5

    def __init__(self, position):
        self.pos = position
        self.clicked = False
        self.possibleMoves = []
        self.FindPossibleMoves()
    
    def FindPossibleMoves(self):
        self.possibleMoves = []

class King:
    value = 6

    def __init__(self, position):
        self.pos = position
        self.clicked = False
        self.possibleMoves = []
        self.FindPossibleMoves()
    
    def FindPossibleMoves(self):
        self.possibleMoves = []