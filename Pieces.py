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
    
    def MoveTo(self, position, board, oppositePieces):
        # Move the piece to the position
        self.pos = position
        self.clicked = False
        
        for piece in oppositePieces:
            if piece.pos == self.pos:
                oppositePieces.remove(piece)
        
        self.FindPossibleMoves(board, oppositePieces)
        return board

    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []

        #Up
        if self.pos[0] > 0:
            for space in range(0, self.pos[0]):
                if board[self.pos[0] - 1 - space, self.pos[1]] == 0:
                    self.possibleMoves.append([self.pos[0] - 1 - space, self.pos[1]])
                elif self.isPlayer and board[self.pos[0] - 1 - space, self.pos[1]] > 10:
                    self.possibleMoves.append([self.pos[0] - 1 - space, self.pos[1]])
                    break
                elif not(self.isPlayer) and board[self.pos[0] - 1 - space, self.pos[1]] < 10:
                    self.possibleMoves.append([self.pos[0] - 1 - space, self.pos[1]])
                    break
                else:
                    break
        #Down
        if self.pos[0] < 7:
            x = 0
            for space in range(self.pos[0] + 1, 8):
                if board[self.pos[0] + 1 + x, self.pos[1]] == 0:
                    self.possibleMoves.append([self.pos[0] + 1 + x, self.pos[1]])
                    x += 1
                elif self.isPlayer and board[self.pos[0] + 1 + x, self.pos[1]] > 10:
                    self.possibleMoves.append([self.pos[0] + 1 + x, self.pos[1]])
                    x += 1
                    break
                elif not(self.isPlayer) and board[self.pos[0] + 1 + x, self.pos[1]] < 10:
                    self.possibleMoves.append([self.pos[0] + 1 + x, self.pos[1]])
                    x += 1
                    break
                else:
                    break
        #Left
        if self.pos[1] > 0:
            for space in range(0, self.pos[1]):
                if board[self.pos[0], self.pos[1] - 1 - space] == 0:
                    self.possibleMoves.append([self.pos[0], self.pos[1] - 1 - space])
                elif self.isPlayer and board[self.pos[0], self.pos[1] - 1 - space] > 10:
                    self.possibleMoves.append([self.pos[0], self.pos[1] - 1 - space])
                    break
                elif not(self.isPlayer) and board[self.pos[0], self.pos[1] - 1 - space] < 10:
                    self.possibleMoves.append([self.pos[0], self.pos[1] - 1 - space])
                    break
                else:
                    break
        #Right
        if self.pos[1] < 7:
            x = 0
            for space in range(self.pos[1] + 1, 8):
                if board[self.pos[0], self.pos[1] + 1 + x] == 0:
                    self.possibleMoves.append([self.pos[0], self.pos[1] + 1 + x])
                    x += 1
                elif self.isPlayer and board[self.pos[0], self.pos[1] + 1 + x] > 10:
                    self.possibleMoves.append([self.pos[0], self.pos[1] + 1 + x])
                    x += 1
                    break
                elif not(self.isPlayer) and board[self.pos[0], self.pos[1] + 1 + x] < 10:
                    self.possibleMoves.append([self.pos[0], self.pos[1] + 1 + x])
                    x += 1
                    break
                else:
                    break

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

        if self.isPlayer:
            self.possibleMoves.append([self.pos[0] - 2, self.pos[1] + 1])
            self.possibleMoves.append([self.pos[0] - 2, self.pos[1] - 1])
        else:
            self.possibleMoves.append([self.pos[0] + 2, self.pos[1] + 1])
            self.possibleMoves.append([self.pos[0] + 2, self.pos[1] - 1])
    
    def MoveTo(self, position, board, oppositePieces):
        # Move the piece to the position
        self.pos = position
        self.clicked = False
        
        for piece in oppositePieces:
            if piece.pos == self.pos:
                oppositePieces.remove(piece)
        
        self.FindPossibleMoves(board, oppositePieces)
        return board

    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []

        #Up-left
        if self.pos[0] > 1 and self.pos[1] > 0:
            if board[self.pos[0] - 2, self.pos[1] - 1] == 0:
                self.possibleMoves.append([self.pos[0] - 2, self.pos[1] - 1])
            elif self.isPlayer and board[self.pos[0] - 2, self.pos[1] - 1] > 10:
                self.possibleMoves.append([self.pos[0] - 2, self.pos[1] - 1])
            elif not(self.isPlayer) and board[self.pos[0] - 2, self.pos[1] - 1] < 10:
                self.possibleMoves.append([self.pos[0] - 2, self.pos[1] - 1])

        #Up-right
        if self.pos[0] > 1 and self.pos[1] < 7:
            if board[self.pos[0] - 2, self.pos[1] + 1] == 0:
                self.possibleMoves.append([self.pos[0] - 2, self.pos[1] + 1])
            elif self.isPlayer and board[self.pos[0] - 2, self.pos[1] + 1] > 10:
                self.possibleMoves.append([self.pos[0] - 2, self.pos[1] + 1])
            elif not(self.isPlayer) and board[self.pos[0] - 2, self.pos[1] + 1] < 10:
                self.possibleMoves.append([self.pos[0] - 2, self.pos[1] + 1])
        
        #Left-up
        if self.pos[0] > 0 and self.pos[1] > 1:
            if board[self.pos[0] - 1, self.pos[1] - 2] == 0:
                self.possibleMoves.append([self.pos[0] - 1, self.pos[1] - 2])
            elif self.isPlayer and board[self.pos[0] - 1, self.pos[1] - 2] > 10:
                self.possibleMoves.append([self.pos[0] - 1, self.pos[1] - 2])
            elif not(self.isPlayer) and board[self.pos[0] - 1, self.pos[1] - 2] < 10:
                self.possibleMoves.append([self.pos[0] - 1, self.pos[1] - 2])
        
        #Left-down
        if self.pos[0] < 7 and self.pos[1] > 1:
            if board[self.pos[0] + 1, self.pos[1] - 2] == 0:
                self.possibleMoves.append([self.pos[0] + 1, self.pos[1] - 2])
            elif self.isPlayer and board[self.pos[0] + 1, self.pos[1] - 2] > 10:
                self.possibleMoves.append([self.pos[0] + 1, self.pos[1] - 2])
            elif not(self.isPlayer) and board[self.pos[0] + 1, self.pos[1] - 2] < 10:
                self.possibleMoves.append([self.pos[0] + 1, self.pos[1] - 2])

        #Down-left
        if self.pos[0] < 6 and self.pos[1] > 0:
            if board[self.pos[0] + 2, self.pos[1] - 1] == 0:
                self.possibleMoves.append([self.pos[0] + 2, self.pos[1] - 1])
            elif self.isPlayer and board[self.pos[0] + 2, self.pos[1] - 1] > 10:
                self.possibleMoves.append([self.pos[0] + 2, self.pos[1] - 1])
            elif not(self.isPlayer) and board[self.pos[0] + 2, self.pos[1] - 1] < 10:
                self.possibleMoves.append([self.pos[0] + 2, self.pos[1] - 1])

        #Down-right
        if self.pos[0] < 6 and self.pos[1] < 7:
            if board[self.pos[0] + 2, self.pos[1] - 1] == 0:
                self.possibleMoves.append([self.pos[0] + 2, self.pos[1] + 1])
            elif self.isPlayer and board[self.pos[0] + 2, self.pos[1] + 1] > 10:
                self.possibleMoves.append([self.pos[0] + 2, self.pos[1] + 1])
            elif not(self.isPlayer) and board[self.pos[0] + 2, self.pos[1] + 1] < 10:
                self.possibleMoves.append([self.pos[0] + 2, self.pos[1] + 1])

        #Right-up
        if self.pos[0] > 0 and self.pos[1] < 6:
            if board[self.pos[0] - 1, self.pos[1] + 2] == 0:
                self.possibleMoves.append([self.pos[0] - 1, self.pos[1] + 2])
            elif self.isPlayer and board[self.pos[0] - 1, self.pos[1] + 2] > 10:
                self.possibleMoves.append([self.pos[0] - 1, self.pos[1] + 2])
            elif not(self.isPlayer) and board[self.pos[0] - 1, self.pos[1] + 2] < 10:
                self.possibleMoves.append([self.pos[0] - 1, self.pos[1] + 2])

        #Right-down
        if self.pos[0] < 7 and self.pos[1] < 6:
            if board[self.pos[0] + 1, self.pos[1] + 2] == 0:
                self.possibleMoves.append([self.pos[0] + 1, self.pos[1] + 2])
            elif self.isPlayer and board[self.pos[0] + 1, self.pos[1] + 2] > 10:
                self.possibleMoves.append([self.pos[0] + 1, self.pos[1] + 2])
            elif not(self.isPlayer) and board[self.pos[0] + 1, self.pos[1] + 2] < 10:
                self.possibleMoves.append([self.pos[0] + 1, self.pos[1] + 2])

class Bishop:
    value = 4

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.possibleMoves = []

    def MoveTo(self, position, board, oppositePieces):
        # Move the piece to the position
        self.pos = position
        self.clicked = False
        
        for piece in oppositePieces:
            if piece.pos == self.pos:
                oppositePieces.remove(piece)
        
        self.FindPossibleMoves(board, oppositePieces)
        return board

    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []

        #Up-right
        if self.pos[0] > 0 and self.pos[1] < 7:
            x = self.pos[1]
            y = self.pos[0]
            while x < 7 and y > 0:
                if board[y - 1, x + 1] == 0:
                    self.possibleMoves.append([y - 1, x + 1])
                elif self.isPlayer and board[y - 1, x + 1] > 10:
                    self.possibleMoves.append([y - 1, x + 1])
                    break
                elif not(self.isPlayer) and board[y - 1, x + 1] < 10:
                    self.possibleMoves.append([y - 1, x + 1])
                    break
                else:
                    break
                
                x += 1
                y -= 1

        #Bottom-right
        if self.pos[0] < 7 and self.pos[1] < 7:
            x = self.pos[1]
            y = self.pos[0]
            while x < 7 and y < 7:
                if board[y + 1, x + 1] == 0:
                    self.possibleMoves.append([y + 1, x + 1])
                elif self.isPlayer and board[y + 1, x + 1] > 10:
                    self.possibleMoves.append([y + 1, x + 1])
                    break
                elif not(self.isPlayer) and board[y + 1, x + 1] < 10:
                    self.possibleMoves.append([y + 1, x + 1])
                    break
                else:
                    break
                
                x += 1
                y += 1

        #Bottom-left
        if self.pos[0] < 7 and self.pos[1] > 0:
            x = self.pos[1]
            y = self.pos[0]
            while x > 0 and y < 7:
                if board[y + 1, x - 1] == 0:
                    self.possibleMoves.append([y + 1, x - 1])
                elif self.isPlayer and board[y + 1, x - 1] > 10:
                    self.possibleMoves.append([y + 1, x - 1])
                    break
                elif not(self.isPlayer) and board[y + 1, x - 1] < 10:
                    self.possibleMoves.append([y + 1, x - 1])
                    break
                else:
                    break
                
                x -= 1
                y += 1

        #Up-left
        if self.pos[0] > 0 and self.pos[1] > 0:
            x = self.pos[1]
            y = self.pos[0]
            while x > 0 and y > 0:
                if board[y - 1, x - 1] == 0:
                    self.possibleMoves.append([y - 1, x - 1])
                elif self.isPlayer and board[y - 1, x - 1] > 10:
                    self.possibleMoves.append([y - 1, x - 1])
                    break
                elif not(self.isPlayer) and board[y - 1, x - 1] < 10:
                    self.possibleMoves.append([y - 1, x - 1])
                    break
                else:
                    break
                
                x -= 1
                y -= 1

class Queen:
    value = 5

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.possibleMoves = []
    
    def MoveTo(self, position, board, oppositePieces):
        # Move the piece to the position
        self.pos = position
        self.clicked = False
        
        for piece in oppositePieces:
            if piece.pos == self.pos:
                oppositePieces.remove(piece)
        
        self.FindPossibleMoves(board, oppositePieces)
        return board

    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []

        #Up
        if self.pos[0] > 0:
            for space in range(0, self.pos[0]):
                if board[self.pos[0] - 1 - space, self.pos[1]] == 0:
                    self.possibleMoves.append([self.pos[0] - 1 - space, self.pos[1]])
                elif self.isPlayer and board[self.pos[0] - 1 - space, self.pos[1]] > 10:
                    self.possibleMoves.append([self.pos[0] - 1 - space, self.pos[1]])
                    break
                elif not(self.isPlayer) and board[self.pos[0] - 1 - space, self.pos[1]] < 10:
                    self.possibleMoves.append([self.pos[0] - 1 - space, self.pos[1]])
                    break
                else:
                    break
        #Down
        if self.pos[0] < 7:
            x = 0
            for space in range(self.pos[0] + 1, 8):
                if board[self.pos[0] + 1 + x, self.pos[1]] == 0:
                    self.possibleMoves.append([self.pos[0] + 1 + x, self.pos[1]])
                    x += 1
                elif self.isPlayer and board[self.pos[0] + 1 + x, self.pos[1]] > 10:
                    self.possibleMoves.append([self.pos[0] + 1 + x, self.pos[1]])
                    x += 1
                    break
                elif not(self.isPlayer) and board[self.pos[0] + 1 + x, self.pos[1]] < 10:
                    self.possibleMoves.append([self.pos[0] + 1 + x, self.pos[1]])
                    x += 1
                    break
                else:
                    break
        #Left
        if self.pos[1] > 0:
            for space in range(0, self.pos[1]):
                if board[self.pos[0], self.pos[1] - 1 - space] == 0:
                    self.possibleMoves.append([self.pos[0], self.pos[1] - 1 - space])
                elif self.isPlayer and board[self.pos[0], self.pos[1] - 1 - space] > 10:
                    self.possibleMoves.append([self.pos[0], self.pos[1] - 1 - space])
                    break
                elif not(self.isPlayer) and board[self.pos[0], self.pos[1] - 1 - space] < 10:
                    self.possibleMoves.append([self.pos[0], self.pos[1] - 1 - space])
                    break
                else:
                    break
        #Right
        if self.pos[1] < 7:
            x = 0
            for space in range(self.pos[1] + 1, 8):
                if board[self.pos[0], self.pos[1] + 1 + x] == 0:
                    self.possibleMoves.append([self.pos[0], self.pos[1] + 1 + x])
                    x += 1
                elif self.isPlayer and board[self.pos[0], self.pos[1] + 1 + x] > 10:
                    self.possibleMoves.append([self.pos[0], self.pos[1] + 1 + x])
                    x += 1
                    break
                elif not(self.isPlayer) and board[self.pos[0], self.pos[1] + 1 + x] < 10:
                    self.possibleMoves.append([self.pos[0], self.pos[1] + 1 + x])
                    x += 1
                    break
                else:
                    break
        #Up-right
        if self.pos[0] > 0 and self.pos[1] < 7:
            x = self.pos[1]
            y = self.pos[0]
            while x < 7 and y > 0:
                if board[y - 1, x + 1] == 0:
                    self.possibleMoves.append([y - 1, x + 1])
                elif self.isPlayer and board[y - 1, x + 1] > 10:
                    self.possibleMoves.append([y - 1, x + 1])
                    break
                elif not(self.isPlayer) and board[y - 1, x + 1] < 10:
                    self.possibleMoves.append([y - 1, x + 1])
                    break
                else:
                    break
                
                x += 1
                y -= 1
        #Bottom-right
        if self.pos[0] < 7 and self.pos[1] < 7:
            x = self.pos[1]
            y = self.pos[0]
            while x < 7 and y < 7:
                if board[y + 1, x + 1] == 0:
                    self.possibleMoves.append([y + 1, x + 1])
                elif self.isPlayer and board[y + 1, x + 1] > 10:
                    self.possibleMoves.append([y + 1, x + 1])
                    break
                elif not(self.isPlayer) and board[y + 1, x + 1] < 10:
                    self.possibleMoves.append([y + 1, x + 1])
                    break
                else:
                    break
                
                x += 1
                y += 1
        #Bottom-left
        if self.pos[0] < 7 and self.pos[1] > 0:
            x = self.pos[1]
            y = self.pos[0]
            while x > 0 and y < 7:
                if board[y + 1, x - 1] == 0:
                    self.possibleMoves.append([y + 1, x - 1])
                elif self.isPlayer and board[y + 1, x - 1] > 10:
                    self.possibleMoves.append([y + 1, x - 1])
                    break
                elif not(self.isPlayer) and board[y + 1, x - 1] < 10:
                    self.possibleMoves.append([y + 1, x - 1])
                    break
                else:
                    break
                
                x -= 1
                y += 1
        #Up-left
        if self.pos[0] > 0 and self.pos[1] > 0:
            x = self.pos[1]
            y = self.pos[0]
            while x > 0 and y > 0:
                if board[y - 1, x - 1] == 0:
                    self.possibleMoves.append([y - 1, x - 1])
                elif self.isPlayer and board[y - 1, x - 1] > 10:
                    self.possibleMoves.append([y - 1, x - 1])
                    break
                elif not(self.isPlayer) and board[y - 1, x - 1] < 10:
                    self.possibleMoves.append([y - 1, x - 1])
                    break
                else:
                    break
                
                x -= 1
                y -= 1

class King:
    value = 6

    def __init__(self, position, isP):
        self.pos = position
        self.isPlayer = isP
        self.clicked = False
        self.possibleMoves = []

    def MoveTo(self, position, board, oppositePieces):
        # Move the piece to the position
        self.pos = position
        self.clicked = False
        
        for piece in oppositePieces:
            if piece.pos == self.pos:
                oppositePieces.remove(piece)
        
        self.FindPossibleMoves(board, oppositePieces)
        return board

    def FindPossibleMoves(self, board, oppositePieces):
        self.possibleMoves = []