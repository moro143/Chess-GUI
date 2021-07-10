import tkinter as tk
from PIL import Image
from PIL import ImageTk
import numpy as np

window = tk.Tk()

board = []
for i in range(8):
    row = []
    for j in range(8):
        row.append(0)
    board.append(row)

def on_board(x):
    if x>=0 and x<8:
        return True
    else:
        return False

class Pawn:
    def __init__(self, wimg, himg, color='white'):
        if color=='white':
            img = Image.open('mats/wPawn.png')
        else:
            img = Image.open('mats/bPawn.png')
        img = img.resize((int(wimg), int(himg)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        self.color = color
        self.name = 'Pawn'

    def possible_moves(self, posx, posy):
        possible = []
        if self.color == 'white':
            if board[posx-1][posy]==0:
                if posx-1>=0:
                    possible.append([posx-1, posy])
                if posx==6 and board[posx-2][posy]==0:
                    possible.append([posx-2, posy])
            if on_board(posx-1) and on_board(posy-1) and board[posx-1][posy-1]!=0 and board[posx-1][posy-1].color!=self.color:
                possible.append([posx-1, posy-1])
            if on_board(posx-1) and on_board(posy+1) and board[posx-1][posy+1]!=0 and board[posx-1][posy+1].color!=self.color:
                possible.append([posx-1, posy+1])
        else:
            if on_board(posx+1) and on_board(posy) and board[posx+1][posy]==0:
                if posx+1<8:
                    possible.append([posx+1, posy])
                if posx==1 and board[posx+2][posy]==0:
                    possible.append([posx+2, posy])
            if on_board(posx+1) and on_board(posy-1) and board[posx+1][posy-1]!=0 and board[posx+1][posy-1].color!=self.color:
                possible.append([posx+1, posy-1])
            if on_board(posx+1) and on_board(posy+1) and board[posx+1][posy+1]!=0 and board[posx+1][posy+1].color!=self.color:
                possible.append([posx+1, posy+1])
        return possible

class King:
    def __init__(self, wimg, himg, color='white'):
        if color=='white':
            img = Image.open('mats/wKing.png')
        else:
            img = Image.open('mats/bKing.png')
        img = img.resize((int(wimg), int(himg)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        self.color = color
        self.name = 'King'

    def possible_moves(self, posx, posy):
        possible = []
        for i in range(-1,2):
            for j in range(-1,2):
                if i==j==0:
                    pass
                else:
                    if posx+i>=0 and posx+i<8 and posy+j>=0 and posy+j<8:
                        if board[posx+i][posy+j]==0 or board[posx+i][posy+j].color!=self.color:
                            possible.append([posx+i, posy+j])
        return possible

class Bishop:
    def __init__(self, wimg, himg, color='white'):
        if color=='white':
            img = Image.open('mats/wBishop.png')
        else:
            img = Image.open('mats/bBishop.png')
        img = img.resize((int(wimg), int(himg)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        self.color = color
        self.name = 'Bishop'

    def possible_moves(self, posx, posy):
        possible = []
        oneFlag = True
        twoFlag = True
        threeFlag = True
        fourFlag = True
        for i in range(1,8):
            if on_board(posx+i) and on_board(posy+i) and oneFlag:
                if board[posx+i][posy+i]==0:
                    possible.append([posx+i, posy+i])
                elif board[posx+i][posy+i].color!=board[posx][posy].color:
                    possible.append([posx+i, posy+i])
                    oneFlag = False
                else:
                    oneFlag = False
            if on_board(posx+i) and on_board(posy-i) and twoFlag:
                if board[posx+i][posy-i]==0:
                    possible.append([posx+i, posy-i])
                elif board[posx+i][posy-i].color!=board[posx][posy].color:
                    possible.append([posx+i, posy-i])
                    twoFlag = False
                else:
                    twoFlag = False
            if on_board(posx-i) and on_board(posy+i) and threeFlag:
                if board[posx-i][posy+i]==0:
                    possible.append([posx-i, posy+i])
                elif board[posx-i][posy+i].color!=board[posx][posy].color:
                    possible.append([posx-i, posy+i])
                    threeFlag = False
                else:
                    threeFlag = False
            if on_board(posx-i) and on_board(posy-i) and fourFlag:
                if board[posx-i][posy-i]==0:
                    possible.append([posx-i, posy-i])
                elif board[posx-i][posy-i].color!=board[posx][posy].color:
                    possible.append([posx-i, posy-i])
                    fourFlag = False
                else:
                    fourFlag = False
        return possible
            
class Knight:
    def __init__(self, wimg, himg, color='white'):
        if color=='white':
            img = Image.open('mats/wKnight.png')
        else:
            img = Image.open('mats/bKnight.png')
        img = img.resize((int(wimg), int(himg)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        self.color = color
        self.name = 'Knight'
    def possible_moves(self, posx, posy):
        pos = []
        pos.append([posx+2, posy+1])
        pos.append([posx+2, posy-1])
        pos.append([posx-2, posy+1])
        pos.append([posx-2, posy-1])
        pos.append([posx+1, posy+2])
        pos.append([posx+1, posy-2])
        pos.append([posx-1, posy+2])
        pos.append([posx-1, posy-2])
        possible = []
        for i in pos:
            if on_board(i[0]) and on_board(i[1]):
                if board[i[0]][i[1]]==0:
                    possible.append(i)
                elif board[i[0]][i[1]].color != self.color:
                    possible.append(i)
        return possible
 
class Rook:
    def __init__(self, wimg, himg, color='white'):
        if color=='white':
            img = Image.open('mats/wRook.png')
        else:
            img = Image.open('mats/bRook.png')
        img = img.resize((int(wimg), int(himg)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        self.color = color
        self.name = 'Rook'

    def possible_moves(self, posx, posy):
        possible = []
        for i in range(posx+1, 8):
            if board[i][posy]==0:
                possible.append([i, posy])
            elif board[i][posy].color!=self.color:
                possible.append([i, posy])
                break
            else:
                break
        for i in range(0, posx):
            if board[posx-i-1][posy]==0:
                possible.append([posx-i-1, posy])
            elif board[posx-i-1][posy].color!=self.color:
                possible.append([posx-i-1, posy])
                break
            else:
                break
        for i in range(posy+1, 8):
            if board[posx][i]==0:
                possible.append([posx, i])
            elif board[posx][i].color!=self.color:
                possible.append([posx, i])
                break
            else:
                break
        for i in range(0, posy):
            if board[posx][posy-i-1]==0:
                possible.append([posx, posy-i-1])
            elif board[posx][posy-i-1].color!=self.color:
                possible.append([posx, posy-i-1])
                break
            else:
                break
        return possible

class Queen:
    def __init__(self, wimg, himg, color='white'):
        if color=='white':
            img = Image.open('mats/wQueen.png')
        else:
            img = Image.open('mats/bQueen.png')
        img = img.resize((int(wimg), int(himg)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(img)
        self.color = color
        self.name = 'Queen'

    def possible_moves(self, posx, posy):
        possible = []
        for i in range(posx+1, 8):
            if board[i][posy]==0:
                possible.append([i, posy])
            elif board[i][posy].color!=self.color:
                possible.append([i, posy])
                break
            else:
                break
        for i in range(0, posx):
            if board[posx-i-1][posy]==0:
                possible.append([posx-i-1, posy])
            elif board[posx-i-1][posy].color!=self.color:
                possible.append([posx-i-1, posy])
                break
            else:
                break
        for i in range(posy+1, 8):
            if board[posx][i]==0:
                possible.append([posx, i])
            elif board[posx][i].color!=self.color:
                possible.append([posx, i])
                break
            else:
                break
        for i in range(0, posy):
            if board[posx][posy-i-1]==0:
                possible.append([posx, posy-i-1])
            elif board[posx][posy-i-1].color!=self.color:
                possible.append([posx, posy-i-1])
                break
            else:
                break
        oneFlag = True
        twoFlag = True
        threeFlag = True
        fourFlag = True
        for i in range(1,8):
            if on_board(posx+i) and on_board(posy+i) and oneFlag:
                if board[posx+i][posy+i]==0:
                    possible.append([posx+i, posy+i])
                elif board[posx+i][posy+i].color!=board[posx][posy].color:
                    possible.append([posx+i, posy+i])
                    oneFlag = False
                else:
                    oneFlag = False
            if on_board(posx+i) and on_board(posy-i) and twoFlag:
                if board[posx+i][posy-i]==0:
                    possible.append([posx+i, posy-i])
                elif board[posx+i][posy-i].color!=board[posx][posy].color:
                    possible.append([posx+i, posy-i])
                    twoFlag = False
                else:
                    twoFlag = False
            if on_board(posx-i) and on_board(posy+i) and threeFlag:
                if board[posx-i][posy+i]==0:
                    possible.append([posx-i, posy+i])
                elif board[posx-i][posy+i].color!=board[posx][posy].color:
                    possible.append([posx-i, posy+i])
                    threeFlag = False
                else:
                    threeFlag = False
            if on_board(posx-i) and on_board(posy-i) and fourFlag:
                if board[posx-i][posy-i]==0:
                    possible.append([posx-i, posy-i])
                elif board[posx-i][posy-i].color!=board[posx][posy].color:
                    possible.append([posx-i, posy-i])
                    fourFlag = False
                else:
                    fourFlag = False
        return possible


def import_board_fen(text):
    global board
    board = []
    for _ in range(8):
        row = []
        for _ in range(8):
            row.append(0)
        board.append(row)
    
    row = 0
    col = 0
    for i in text:
        if i == "/":
            col+=1
            row=0
        elif i == 'r':
            board[col][row]=Rook(wPiece, hPiece, 'black')
            row+=1
        elif i == 'R':
            board[col][row]=Rook(wPiece, hPiece, 'white')
            row+=1
        elif i == 'n':
            board[col][row]=Knight(wPiece, hPiece, 'black')
            row+=1
        elif i == 'N':
            board[col][row]=Knight(wPiece, hPiece, 'white')
            row+=1
        elif i == 'q':
            board[col][row]=Queen(wPiece, hPiece, 'black')
            row+=1
        elif i == 'Q':
            board[col][row]=Queen(wPiece, hPiece, 'white')
            row+=1
        elif i == 'k':
            board[col][row]=King(wPiece, hPiece, 'black')
            row+=1
        elif i == 'K':
            board[col][row]=King(wPiece, hPiece, 'white')
            row+=1
        elif i == 'p':
            board[col][row]=Pawn(wPiece, hPiece, 'black')
            row+=1
        elif i == 'P':
            board[col][row]=Pawn(wPiece, hPiece, 'white')
            row+=1
        elif i == 'b':
            board[col][row]=Bishop(wPiece, hPiece, 'black')
            row+=1
        elif i == 'B':
            board[col][row]=Bishop(wPiece, hPiece, 'white')
            row+=1
        else:
            row += int(i)
        draw_board()

def import_board_fen_GUI():
    text = inputBoardText.get(1.0, "end-1c")
    import_board_fen(text)

def create_board(canvas, canvas_width, canvas_height, num=8):
    w = canvas_width/num
    h = canvas_height/num
    color1 = '#6abd22'
    color2 = '#e4ebc7'

    for i in range(num):
        for j in range(num):
            if (i+j)%2==0:
                canvas.create_rectangle(i*w, j*h, (i+1)*w, (j+1)*h, fill=color1, width=0)
            else:
                canvas.create_rectangle(i*w, j*h, (i+1)*w, (j+1)*h, fill=color2, width=0)
    return w, h

canvasFrame = tk.Frame(window)
canvasFrame.grid(column=1, row=0)
canvas_width = 500
canvas_height = 500
board_canvas = tk.Canvas(canvasFrame, width=canvas_width, height=canvas_height)
board_canvas.pack()
wPiece, hPiece = create_board(board_canvas, canvas_width, canvas_height)

menuFrame = tk.Frame(window)
menuFrame.grid(column=1, row=1)

playerLabel = tk.Label(menuFrame, text='Player: white')
playerLabel.grid(column=0, row=0)

def change_player(player):
    playerLabel['text']=('Player: '+player)

inputBoardText = tk.Text(menuFrame, width=20, height=4)
inputBoardText.grid(column=0, row=1)
inputBoardButton = tk.Button(menuFrame, text='Import Fen', command=import_board_fen_GUI)
inputBoardButton.grid(column=0, row=2)

whitePlayerMethod = 'Player'
methods = ['Player', 'Random']
def change_method_white():
    global whitePlayerMethod, methods
    whitePlayerMethod = methods[wPlayervar.get()]
    print(whitePlayerMethod)
whitePlayerFrame = tk.Frame(window)
whitePlayerFrame.grid(column=0, row=0)
wPlayervar = tk.IntVar()
wPlayer = tk.Radiobutton(whitePlayerFrame, text='Player', value=0, variable=wPlayervar, command=change_method_white)
wRandom = tk.Radiobutton(whitePlayerFrame, text='Random', value=1, variable=wPlayervar, command=change_method_white)
wPlayer.pack(anchor=tk.W)
wRandom.pack(anchor=tk.W)

blackPlayerMethod = 'Player'
methods = ['Player', 'Random']
def change_method_black():
    global blackPlayerMethod, methods
    blackPlayerMethod = methods[bPlayervar.get()]
    print(blackPlayerMethod)
blackPlayerFrame = tk.Frame(window)
blackPlayerFrame.grid(column=2, row=0)
bPlayervar = tk.IntVar()
bPlayer = tk.Radiobutton(blackPlayerFrame, text='Player', value=0, variable=bPlayervar, command=change_method_black)
bRandom = tk.Radiobutton(blackPlayerFrame, text='Random', value=1, variable=bPlayervar, command=change_method_black)
bPlayer.pack(anchor=tk.W)
bRandom.pack(anchor=tk.W)

def draw_pices():
    r = 0
    for row in board:
        t=0
        for tile in row:
            if tile!=0:
                board_canvas.create_image(t*wPiece, r*hPiece, image=tile.img, anchor='nw')
            t+=1
        r+=1

def draw_board():
    board_canvas.delete("all")
    create_board(board_canvas, canvas_width, canvas_height)
    draw_pices()

import_board_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

current_player = 'white'
board_method = "choose piece"
possible_moves = []
choosen_piece_place = []

def all_possible_moves(board, color):
    all_possible_moves = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!=0 and board[i][j].color==color:
                possible_moves = board[i][j].possible_moves(i, j)
                if possible_moves != []:
                    all_possible_moves[i,j] = possible_moves
    return all_possible_moves

def is_check(board):
    moves_white = all_possible_moves(board, 'white')
    moves_black = all_possible_moves(board, 'black')
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!=0 and board[i][j].name == 'King':
                for m in moves_white.values():
                    if [i, j] in m:
                        return True
                for m in moves_black.values():
                    if [i, j] in m:
                        return True
    return False

def playerMethod(event):
    global board_method, possible_moves, choosen_piece_place, current_player
    tile = [int(event.x//wPiece), int(event.y//hPiece)]
    draw_board()
    if board_method == "choose piece":
        if board[tile[1]][tile[0]]!=0 and board[tile[1]][tile[0]].color == current_player:
            board_canvas.create_rectangle(tile[0]*wPiece, tile[1]*hPiece,tile[0]*wPiece+wPiece, tile[1]*hPiece+hPiece, width=2)
            choosen_piece_place = [tile[1], tile[0]]
            possible_moves = board[tile[1]][tile[0]].possible_moves(tile[1], tile[0])
            for i in possible_moves:
                board_canvas.create_rectangle(i[1]*wPiece, i[0]*hPiece, i[1]*wPiece+wPiece, i[0]*hPiece+hPiece, width=0, fill='#136c9c')
            board_method = "choose move"
    elif board_method == "choose move":
        if [tile[1], tile[0]] in possible_moves:
            board[tile[1]][tile[0]] = board[choosen_piece_place[0]][choosen_piece_place[1]]
            board[choosen_piece_place[0]][choosen_piece_place[1]] = 0
            if current_player=='white':
                change_player('black')
                current_player='black'
            else:
                change_player('white')
                current_player='white'
            draw_board()
        board_method="choose piece"
    draw_pices()

def randomMethod(event):
    global possible_moves, choosen_piece_place, current_player, board
    tile = [int(event.x//wPiece), int(event.y//hPiece)]
    d = all_possible_moves(board, current_player)
    choices = []
    for i in d:
        for j in d[i]:
            choices.append([i, j])
    choice = choices[np.random.choice(range(len(choices)))]
    choosen_piece_place = choice[0]
    tile = [choice[1][1], choice[1][0]]
    board[tile[1]][tile[0]] = board[choosen_piece_place[0]][choosen_piece_place[1]]
    board[choosen_piece_place[0]][choosen_piece_place[1]] = 0
    if current_player=='white':
        change_player('black')
        current_player='black'
    else:
        change_player('white')
        current_player='white'
    draw_board()

def callback(event):
    global current_player
    print(is_check(board))
    if current_player=='white':
        if whitePlayerMethod=='Player':
            playerMethod(event)
        elif whitePlayerMethod=='Random':
            randomMethod(event)
        if blackPlayerMethod!="Player" and current_player!='white':
            callback(event)

    elif current_player=='black':
        if blackPlayerMethod=='Player':
            playerMethod(event)
        elif blackPlayerMethod=='Random':
            randomMethod(event)
        if whitePlayerMethod!="Player":
            callback(event)

draw_board()

board_canvas.bind("<ButtonRelease-1>", callback)

window.mainloop()