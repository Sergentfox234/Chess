import pygame
import random as rnd
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
debugButton = pygame.image.load('source/debugButton.png')
resetButton = pygame.image.load('source/resetButton.png')
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

# Setting the background
def PlaceBoard():
    window.blit(chessBoard, (150, 0))
    window.blit(debugButton, (0, 0))
    window.blit(resetButton, (800 - 64, 0))

playerPieces = []                  # The list of the players (bottom side) pieces
botPieces = []                     # The list of the bots (top side) pieces
pawns = []                         # List of pawns for quick removal of enpassantability every turn
enPassant = [False]                # Boolean indicator if an enPassant can happen
resetPass = False                  # Boolean catcher for if the turn needs to reset it's enpessant ability
pieceClicked = False               # Boolean for if there is a piece currently selected
thePiece = []                      # The piece that is currently selected (in hand)
debugMode = False                  # The debug mode
playerTurn = True                  # The turn dictator
playerWhite = True                 # The player's color

# Initialize the board
# 1 - Pawn
# 2 - Rook
# 3 - Knight
# 4 - Bishop
# 5 - Queen
# 6 - King
# 1 will be placed in front for bot pieces ie 16 is bot king
board = np.array([])
def InitializeBoard(board):
    board = np.zeros((8, 8), dtype= np.int16)
    #Rooks
    board[0][0] = 12
    botPieces.append(pc.Rook([0, 0], False))
    board[0][7] = 12
    botPieces.append(pc.Rook([0, 7], False))
    board[7][0] = 2
    playerPieces.append(pc.Rook([7, 0], True))
    board[7][7] = 2
    playerPieces.append(pc.Rook([7, 7], True))
    #Knights
    board[0][1] = 13
    botPieces.append(pc.Knight([0, 1], False))
    board[0][6] = 13
    botPieces.append(pc.Knight([0, 6], False))
    board[7][1] = 3
    playerPieces.append(pc.Knight([7, 1], True))
    board[7][6] = 3
    playerPieces.append(pc.Knight([7, 6], True))
    #Bishops
    board[0][2] = 14
    botPieces.append(pc.Bishop([0, 2], False))
    board[0][5] = 14
    botPieces.append(pc.Bishop([0, 5], False))
    board[7][2] = 4
    playerPieces.append(pc.Bishop([7, 2], True))
    board[7][5] = 4
    playerPieces.append(pc.Bishop([7, 5], True))
    #Queens
    board[0][3] = 15
    botPieces.append(pc.Queen([0, 3], False))
    board[7][3] = 5
    playerPieces.append(pc.Queen([7, 3], True))
    #Kings
    board [0][4] = 16
    botPieces.append(pc.King([0, 4], False))
    board [7][4] = 6
    playerPieces.append(pc.King([7, 4], True))
    #Pawns
    for x in range(8):
        board[1][x] = 11
        pawns.append(pc.Pawn([1, x], False))
        botPieces.append(pawns[2 * x])
        
        board[6][x] = 1
        pawns.append(pc.Pawn([6, x], True))
        playerPieces.append(pawns[2 * x + 1])
    
    return board
board = InitializeBoard(board)

# Faster way compare elements of tuples
def lessAll(tuple1, tuple2):
    result = all(x < y for x, y in zip(tuple1, tuple2))
    return result
def greAll(tuple1, tuple2):
    result = all(x > y for x, y in zip(tuple1, tuple2))
    return result

# Draw the board
def DrawBoardW(board):
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
def DrawBoardB(board):
    x = 0
    y = 0
    
    for row in board:
        x = 0
        for piece in row:
            if piece == 1:
                window.blit(blackPawn, (64 * x + 152, 64 * y + 2))
            elif piece == 11:
                window.blit(whitePawn, (64 * x + 152, 64 * y + 2))
            elif piece == 2:
                window.blit(blackRook, (64 * x + 152, 64 * y + 2)) 
            elif piece == 12:
                window.blit(whiteRook, (64 * x + 152, 64 * y + 2))
            elif piece == 3:
                window.blit(blackKnight, (64 * x + 152, 64 * y + 2))
            elif piece == 13:
                window.blit(whiteKnight, (64 * x + 152, 64 * y + 2))
            elif piece == 4:
                window.blit(blackBishop, (64 * x + 152, 64 * y + 2))
            elif piece == 14:
                window.blit(whiteBishop, (64 * x + 152, 64 * y + 2))
            elif piece == 5:
                window.blit(blackQueen, (64 * x + 152, 64 * y + 2))
            elif piece == 15:
                window.blit(whiteQueen, (64 * x + 152, 64 * y + 2))
            elif piece == 6:
                window.blit(blackKing, (64 * x + 152, 64 * y + 2))
            elif piece == 16:
                window.blit(whiteKing, (64 * x + 152, 64 * y + 2))

            x += 1
        y += 1

# Reset the game
def ResetBoard():
    pawns.clear()
    botPieces.clear()
    playerPieces.clear()
    thePiece.clear()
    board = InitializeBoard(np.array([]))
    
    return board
# Reset the first turn
def ResetTurn():
    choice = rnd.randint(0, 1)
    if choice == 0:
        playerTurn = True
        playerWhite = True
    else:
        playerTurn = False
        playerWhite = False

    return [playerTurn, playerWhite]

# Debugger
def Debugger(debug):
    print(botPieces)
    print(playerPieces)
    print(board)
    debugMode = not(debug)
    return debugMode

# Draw possible moves
def DrawPossibleMoves(piece):
    for move in piece.possibleMoves:
        pygame.draw.circle(window, (100, 100, 100, 0), [152 + move[1] * 64 + 32, 2 + move[0] * 64 + 32], 15)

# Reset Enpassantability (since it can only happen IMMEDIATELY after)
def ResetEnPass(pawns):
    for piece in pawns:
        piece.enPessentable = False

choice = rnd.randint(0, 1)
if choice == 0:
    playerTurn = True
    playerWhite = True
else:
    playerTurn = False
    playerWhite = False

# The game loop
running = True  
while running:
    # Manage the events
    for event in pygame.event.get():
        # If the close button is pressed
        if event.type == pygame.QUIT:
            running = False
            break
        
        #If the mouse button is pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print (mouse)
            
            # If you click on the debugger button
            if greAll(mouse, (0, 0)) and lessAll(mouse, (64, 64)):
                debugMode = Debugger(debugMode)

            # If you click on the reset button
            if greAll(mouse, (800 - 64, 0)) and lessAll(mouse, (800, 64)):
                board = ResetBoard()
                boolList = ResetTurn()
                playerTurn = boolList[0]
                playerWhite = boolList[1]
                pieceClicked = False
                continue

            # If you click on your own piece, pick it up (show possible moves)
            if playerTurn:
                for piece in playerPieces:
                    if greAll(mouse, (152 + piece.pos[1] * 64, 2 + piece.pos[0] * 64)) and lessAll(mouse, (152 + piece.pos[1] * 64 + 64, 2 + piece.pos[0] * 64 + 64)):
                        print(piece)
                        print("Piece pos: ", piece.pos)
                        print("Poss moves: ", piece.possibleMoves)
                        print("Piece value: ", piece.value)
                        piece.FindPossibleMoves(board, botPieces)

                        # If the piece can't be clicked (has no moves), skip it
                        if piece.possibleMoves.__len__() == 0 and thePiece.__len__() == 0:
                            continue
                        # then if a piece can't be clicked and there was a piece in hand
                        #elif piece.possibleMoves.__len__() == 0:
                        #   thePiece[0].clicked = False
                        #    thePiece.clear()
                        #   pieceClicked = False
                        # then if a piece is not clicked and the piece has moves    
                        elif pieceClicked == False and piece.possibleMoves.__len__() > 0:
                            piece.clicked = True
                            pieceClicked = True
                            thePiece.append(piece)
                        # then if this piece is in your hand or if you deselected    
                        else:
                            if piece.clicked == True:
                                piece.clicked = False
                                pieceClicked = False
                                thePiece.clear()
                            elif not(debugMode):
                                thePiece[0].clicked = False
                                thePiece.clear()
                                pieceClicked = False

            # If bot's turn
            else:
                for piece in botPieces:
                    if greAll(mouse, (152 + piece.pos[1] * 64, 2 + piece.pos[0] * 64)) and lessAll(mouse, (152 + piece.pos[1] * 64 + 64, 2 + piece.pos[0] * 64 + 64)):
                        print(piece)
                        print("Piece pos: ", piece.pos)
                        print("Poss moves: ", piece.possibleMoves)
                        print("Piece value: ", piece.value)
                        piece.FindPossibleMoves(board, playerPieces)

                        # If the piece can't be clicked (has no moves), skip it
                        if piece.possibleMoves.__len__() == 0 and thePiece.__len__() == 0:
                            continue
                        # then if a piece can't be clicked and there was a piece in hand
                        #elif piece.possibleMoves.__len__() == 0:
                        # thePiece[0].clicked = False
                        # thePiece.clear()
                        # pieceClicked = False
                        # then if a piece is not clicked and the piece has moves    
                        elif pieceClicked == False and piece.possibleMoves.__len__() > 0:
                            piece.clicked = True
                            pieceClicked = True
                            thePiece.append(piece)
                        # then if this piece is in your hand or if you deselected    
                        else:
                            if piece.clicked == True:
                                piece.clicked == False
                                pieceClicked = False
                                thePiece.clear()
                            else:
                                thePiece[0].clicked = False
                                thePiece.clear()
                                pieceClicked = False

            # If you have already clicked on your piece, and you want to move it
            if pieceClicked:
                for move in thePiece[0].possibleMoves:
                    bottomLeft = (152 + move[1] * 64, 2 + move[0] * 64)
                    topRight = (152 + move[1] * 64 + 64, 2 + move[0] * 64 + 64)
                    if greAll(mouse, bottomLeft) and lessAll(mouse, topRight):
                        board[thePiece[0].pos[0], thePiece[0].pos[1]] = 0

                        # If a piece can be enPassanted this turn, then turn it off for next turn
                        if enPassant[0]:
                            resetPass = True

                        # Move the piece
                        if thePiece[0].isPlayer:
                            if thePiece[0].value == 1:
                                board = thePiece[0].MoveTo(move, board, botPieces, enPassant)
                            else:
                                board = thePiece[0].MoveTo(move, board, botPieces)
                        else:
                            if thePiece[0].value == 1:
                                board = thePiece[0].MoveTo(move, board, playerPieces, enPassant)
                            else:
                                board = thePiece[0].MoveTo(move, board, playerPieces)

                        board[move[0], move[1]] = thePiece[0].value

                        if not(thePiece[0].isPlayer):
                            board[move[0], move[1]] += 10

                        if resetPass:
                            ResetEnPass(pawns)
                            enPassant[0] = False
                            resetPass = False

                        playerTurn = not(playerTurn)
                        pieceClicked = False
                        thePiece.clear()

    #Change the background
    window.fill((0, 100, 0))

    # Update the display
    PlaceBoard()
    if playerWhite:
        DrawBoardW(board)
    else:
        DrawBoardB(board)
    
    #If a piece is clicked, display it's possible moves
    if pieceClicked:
        DrawPossibleMoves(thePiece[0])

    pygame.display.update()