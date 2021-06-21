import pygame
import numpy as np
import Pieces as pc

# initialize pygame module
pygame.init()

# Create the screen
window = pygame.display.set_mode((800, 600))

# Editing the window
pygame.display.set_caption("Chess")
icon = pygame.image.load('source/icon.png')
pygame.display.set_icon(icon)

# Setting images
chessBoard = pygame.image.load('source/chessboard.png')
whitePawn = pygame.image.load('source/whitepawn.png')
blackPawn = pygame.image.load('source/blackpawn.png')
whiteRook = pygame.image.load('source/whiterook.png')
blackRook = pygame.image.load('source/blackrook.png')
whiteKnight = pygame.image.load('source/whiteknight.png')
blackKnight = pygame.image.load('source/blackknight.png')
whiteBishop = pygame.image.load('source/whitebishop.png')
blackBishop = pygame.image.load('source/blackBishop.png')
whiteQueen = pygame.image.load('source/whitequeen.png')
blackQueen = pygame.image.load('source/blackqueen.png')
whiteKing = pygame.image.load('source/whiteking.png')
blackKing = pygame.image.load('source/blackking.png')

# Setting the board's position
def PlaceBoard():
    window.blit(chessBoard, (150, 0))

whitePieces = []
blackPieces = []

# Initialize the board
# 1 - Pawn
# 2 - Rook
# 3 - Knight
# 4 - Bishop
# 5 - Queen
# 6 - King
# 1 will be placed in front for black pieces ie 16 is black king
board = np.array([])
def InitializeBoard(board):
    board = np.zeros((8, 8), dtype= np.int16)
    #Rooks
    board[0][0] = 12
    blackPieces.append(pc.Rook([0, 0]))
    board[0][7] = 12
    blackPieces.append(pc.Rook([0, 7]))
    board[7][0] = 2
    whitePieces.append(pc.Rook([7, 0]))
    board[7][7] = 2
    whitePieces.append(pc.Rook([7, 7]))
    #Knights
    board[0][1] = 13
    board[0][6] = 13
    board[7][1] = 3
    board[7][6] = 3
    #Bishops
    board[0][2] = 14
    board[0][5] = 14
    board[7][2] = 4
    board[7][5] = 4
    #Queens
    board[0][3] = 15
    board[7][3] = 5
    #Kings
    board [0][4] = 16
    board [7][4] = 6
    #Pawns
    for x in range(8):
        board[1][x] = 11
        blackPieces.append(pc.Pawn([1, x], False))
        board[6][x] = 1
        whitePieces.append(pc.Pawn([6, x], True))
    
    return board
board = InitializeBoard(board)

board[3][4] = 1
whitePieces.append(pc.Pawn([3, 3], True))
whitePieces[10].firstMove = False
whitePieces[10].FindPossibleMoves()

for piece in whitePieces:
    print(piece)
    print(piece.pos)
    print(piece.possibleMoves)

#Faster way to force all numbers to be greater or less than
def lessAll(tuple1, tuple2):
    result = all(x < y for x, y in zip(tuple1, tuple2))
    return result
def greAll(tuple1, tuple2):
    result = all(x > y for x, y in zip(tuple1, tuple2))
    return result

# Draw the board
def DrawBoard(board):
    x = 0
    y = 0
    
    for row in board:
        x = 0
        for piece in row:
            if piece == 1:
                window.blit(whitePawn, (64 * x + 152, 64 * y + 2))
            elif piece == 11:
                window.blit(blackPawn, (64 * x + 152, 64 * y + 2))
            elif piece == 2:
                window.blit(whiteRook, (64 * x + 152, 64 * y + 2)) 
            elif piece == 12:
                window.blit(blackRook, (64 * x + 152, 64 * y + 2))
            elif piece == 3:
                window.blit(whiteKnight, (64 * x + 152, 64 * y + 2))
            elif piece == 13:
                window.blit(blackKnight, (64 * x + 152, 64 * y + 2))
            elif piece == 4:
                window.blit(whiteBishop, (64 * x + 152, 64 * y + 2))
            elif piece == 14:
                window.blit(blackBishop, (64 * x + 152, 64 * y + 2))
            elif piece == 5:
                window.blit(whiteQueen, (64 * x + 152, 64 * y + 2))
            elif piece == 15:
                window.blit(blackQueen, (64 * x + 152, 64 * y + 2))
            elif piece == 6:
                window.blit(whiteKing, (64 * x + 152, 64 * y + 2))
            elif piece == 16:
                window.blit(blackKing, (64 * x + 152, 64 * y + 2))

            x += 1
        y += 1

# The game loop
running = True  
while running:
    # Manage the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            
            while pygame.MOUSEBUTTONDOWN:
                print(mouse)
             
            if greAll(mouse, (152, 2)) and lessAll(mouse, (152 + 64, 2 + 64)):
                board[3][3] = 16
            else:
                board[3][3] = 0
    
    #Change the background
    window.fill((0, 100, 0))

    # Update the display
    PlaceBoard()
    DrawBoard(board)
    pygame.display.update()