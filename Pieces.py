class Pawn:
    value = 1

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.firstMove = True
        self.enPessentable = False
        self.possibleMoves = []
        self.FindFirstMoves()

    def MoveTo(self, position, board, oppositePieces, enPassant):
        # Check for enpessentability
        if self.isPlayer and self.firstMove and position[0] == self.pos[0] - 2:
            self.enPessentable = True
            print("enPessentable!!")
            enPassant[0] = True
        elif self.isPlayer:
            self.enPessentable = False
            print("Nope")
        elif not(self.isPlayer) and self.firstMove and position[0] == self.pos[0] + 2:
            self.enPessentable = True
            enPassant[0] = True
            print("enPessentable!!")
        elif not(self.isPlayer):
            self.enPessentable = False
            print("Nope")

        # Check if move done was an en passant
        leftSpot = [self.pos[0] - 1, self.pos[1] - 1]
        bLeftSpot = [self.pos[0] + 1, self.pos[1] + 1]
        rightSpot = [self.pos[0] - 1, self.pos[1] + 1]
        bRightSpot = [self.pos[0] + 1, self.pos[1] - 1]

        if self.isPlayer and position == leftSpot:
            for piece in oppositePieces:
                if piece.pos == [self.pos[0], self.pos[1] - 1]:
                    oppositePieces.remove(piece)
                    board[self.pos[0], self.pos[1] - 1] = 0
        elif self.isPlayer and position == rightSpot:
            for piece in oppositePieces:
                if piece.pos == [self.pos[0], self.pos[1] + 1]:
                    oppositePieces.remove(piece)
                    board[self.pos[0], self.pos[1] + 1] = 0
        elif not(self.isPlayer) and position == bLeftSpot:
            for piece in oppositePieces:
                if piece.pos == [self.pos[0], self.pos[1] + 1]:
                    oppositePieces.remove(piece)
                    board[self.pos[0], self.pos[1] + 1] = 0
        elif not(self.isPlayer) and position == bRightSpot:
            for piece in oppositePieces:
                if piece.pos == [self.pos[0], self.pos[1] - 1]:
                    oppositePieces.remove(piece)
                    board[self.pos[0], self.pos[1] - 1] = 0

        # Move the piece to the position
        self.pos = position
        self.clicked = False
        self.firstMove = False
        
        for piece in oppositePieces:
            if piece.pos == self.pos:
                oppositePieces.remove(piece)

        self.FindPossibleMoves(board, oppositePieces)
        return board

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
        elif not(self.isPlayer) and self.pos[0] < 7 and board[self.pos[0] + 1, self.pos[1]] == 0:
            self.possibleMoves.append([self.pos[0] + 1, self.pos[1]])
        
        # If the pawn can ATTACK to the left
        if self.isPlayer and self.pos[1] > 0 and board[self.pos[0] - 1, self.pos[1] - 1] >= 10:
            self.possibleMoves.append([self.pos[0] - 1, self.pos[1] - 1])
        elif not(self.isPlayer) and self.pos[0] < 7 and self.pos[1] < 7 and board[self.pos[0] + 1, self.pos[1] + 1] < 10 and board[self.pos[0] + 1, self.pos[1] + 1] > 0:
            self.possibleMoves.append([self.pos[0] + 1, self.pos[1] + 1])

        # If the pawn can ATTACK to the right 
        if self.isPlayer and self.pos[1] < 7 and board[self.pos[0] - 1, self.pos[1] + 1] >= 10:
            self.possibleMoves.append([self.pos[0] - 1, self.pos[1] + 1])
        elif not(self.isPlayer) and self.pos[0] < 7 and self.pos[1] > 0 and board[self.pos[0] + 1, self.pos[1] - 1] < 10 and board[self.pos[0] + 1, self.pos[1] - 1] > 0:
            self.possibleMoves.append([self.pos[0] + 1, self.pos[1] - 1])

        # If enpessent to the left
        if self.isPlayer and self.pos[1] > 0 and board[self.pos[0], self.pos[1] - 1] == 11:
            for possPiece in oppositePieces:
                if possPiece.pos == [self.pos[0], self.pos[1] - 1] and possPiece.enPessentable:
                    self.possibleMoves.append([self.pos[0] - 1, self.pos[1] - 1])
        elif not(self.isPlayer) and self.pos[0] < 7 and self.pos[1] < 7 and board[self.pos[0], self.pos[1] + 1] == 1:
            for possPiece in oppositePieces:
                if possPiece.pos == [self.pos[0], self.pos[1] + 1] and possPiece.enPessentable:
                    self.possibleMoves.append([self.pos[0] + 1, self.pos[1] + 1])

        # If enpessent to the right
        if self.isPlayer and self.pos[1] < 7 and board[self.pos[0], self.pos[1] + 1] == 11:
            for possPiece in oppositePieces:
                if possPiece.pos == [self.pos[0], self.pos[1] + 1] and possPiece.enPessentable:
                    self.possibleMoves.append([self.pos[0] - 1, self.pos[1] + 1])
        elif not(self.isPlayer) and self.pos[0] > 0 and self.pos[1] > 0 and board[self.pos[0], self.pos[1] - 1] == 1:
            for possPiece in oppositePieces:
                if possPiece.pos == [self.pos[0], self.pos[1] - 1] and possPiece.enPessentable:
                    self.possibleMoves.append([self.pos[0] + 1, self.pos[1] - 1])
            
class Rook:
    value = 2

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.possibleMoves = []
        self.FindFirstMoves()
    
    def FindFirstMoves(self):
        self.possibleMoves = []

    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []

class Knight:
    value = 3

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.possibleMoves = []
        self.FindFirstMoves()
    
    def FindFirstMoves(self):
        self.possibleMoves = []
    
    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []

class Bishop:
    value = 4

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.possibleMoves = []
        self.FindFirstMoves()

    def FindFirstMoves(self):
        self.possibleMoves = [[0, 0]]

    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = [[0, 0]]

class Queen:
    value = 5

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.possibleMoves = []
        self.FindFirstMoves()
    
    def FindFirstMoves(self):
        self.possibleMoves = []

    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []

class King:
    value = 6

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.possibleMoves = []
        self.FindFirstMoves()
    
    def FindFirstMoves(self):
        self.possibleMoves = []

    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []