from tkinter import *
from tkinter import messagebox, simpledialog
import random
import threading
import time
try:
    from playsound import playsound
except:
    playsound = None

def play_sound_nonblocking(file):
    if not playsound:
        return
    def _p():
        try:
            playsound(file)
        except:
            pass
    threading.Thread(target=_p, daemon=True).start()

def play_background_music():
    def _bg():
        while True:
            try:
                playsound("Background.mp3")
            except:
                break
    threading.Thread(target=_bg, daemon=True).start()

root_temp = Tk()
root_temp.withdraw()
mode = simpledialog.askstring("Pilih Mode Permainan",
                              "Pilih Mode:\n1. Player vs Player\n2. Player vs CPU",
                              initialvalue="1")
if mode not in ("1", "2"):
    mode = "1"

if mode == "1":
    player1_name = simpledialog.askstring("Nama Pemain", "Masukkan nama Player 1 (O):", initialvalue="Player 1") or "Player 1"
    player2_name = simpledialog.askstring("Nama Pemain", "Masukkan nama Player 2 (X):", initialvalue="Player 2") or "Player 2"
    cpu_level = None
else:
    player1_name = simpledialog.askstring("Nama Pemain", "Masukkan nama Player (O):", initialvalue="Player 1") or "Player 1"
    player2_name = "CPU"
    cpu_level = simpledialog.askstring("Mode CPU", "Pilih Level CPU:\n1. Easy\n2. Medium\n3. Hard", initialvalue="1")
    if cpu_level not in ("1","2","3"):
        cpu_level = "1"

root_temp.destroy()

ROOT_W = 420
ROOT_H = 600
CELL_SIZE = 120
FONT_BASE = ("Comic Sans MS", 28, "bold")

COLOR_O = "#FF69B4"
COLOR_X = "#87CEFA"
BG_COLOR = "#FFE6F2"
TILE_COLOR = "#FFF0F7"

current_turn = "O"
states = [[None]*3 for _ in range(3)]
canvases = []
text_items = []
rect_items = []
game_over = False
winning_coords = []

root = Tk()
root.title("Tic Tac Toe Pastel Pink")
root.geometry(f"{ROOT_W}x{ROOT_H}")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

header = Label(root, text=f"{player1_name} (O)    vs    {player2_name} (X)",
               font=("Comic Sans MS", 20, "bold"),
               bg=BG_COLOR, fg=COLOR_X)
header.pack(pady=(8,6))

board_frame = Frame(root, bg=BG_COLOR)
board_frame.pack()

confetti_canvas = Canvas(root, width=ROOT_W, height=140, bg=BG_COLOR, highlightthickness=0)
confetti_canvas.pack(pady=(6,0))
confetti_pieces = []


bottom_frame = Frame(root, bg=BG_COLOR)
bottom_frame.pack(side=BOTTOM, fill="x", pady=(6,12))

status_label = Label(bottom_frame, text="", font=("Comic Sans MS", 16, "bold"),
                     bg=BG_COLOR, fg=COLOR_O)
status_label.pack(pady=(6,4))

def create_cell(r, c):
    cv = Canvas(board_frame, width=CELL_SIZE, height=CELL_SIZE,
                bg=TILE_COLOR, highlightthickness=2, bd=0)
    rect = cv.create_rectangle(6,6,CELL_SIZE-6,CELL_SIZE-6, outline="#e6cfe0", width=3)
    txt = cv.create_text(CELL_SIZE//2, CELL_SIZE//2, text="", font=FONT_BASE)

    cv.grid(row=r, column=c, padx=6, pady=6)
    cv.bind("<Button-1>", lambda e, rr=r, cc=c: on_cell_click(rr, cc))
    return cv, rect, txt

for i in range(3):
    canvases.append([])
    text_items.append([])
    rect_items.append([])
    for j in range(3):
        cv, rect, txt = create_cell(i,j)
        canvases[i].append(cv)
        rect_items[i].append(rect)
        text_items[i].append(txt)

def on_cell_click(r, c):
    global current_turn, game_over
    if game_over or states[r][c] is not None:
        return

    states[r][c] = current_turn
    canvases[r][c].itemconfigure(text_items[r][c], text=current_turn,
                                 fill=(COLOR_O if current_turn == "O" else COLOR_X))
    play_sound_nonblocking("Klik.mp3")

    if check_for_win_and_animate(): return
    if full(): return draw()

    if mode == "2" and current_turn == "O":
        switch_turn()
        root.after(400, cpu_move)
    else:
        switch_turn()

def switch_turn():
    global current_turn
    current_turn = "X" if current_turn == "O" else "O"
    name = player2_name if current_turn == "X" else player1_name
    status_label.config(text=f"Giliran: {name}",
                        fg=(COLOR_X if current_turn == "X" else COLOR_O))

def cpu_move():
    global current_turn
    if game_over: return
    move = choose_move()
    r,c = move
    states[r][c] = "X"
    canvases[r][c].itemconfigure(text_items[r][c], text="X", fill=COLOR_X)
    play_sound_nonblocking("Klik.mp3")

    if check_for_win_and_animate(): return
    if full(): return draw()

    current_turn = "O"
    status_label.config(text=f"Giliran: {player1_name}", fg=COLOR_O)

def full():
    return all(states[i][j] is not None for i in range(3) for j in range(3))

def check_for_win_and_animate():
    global game_over, winning_coords
    lines = [
        [(i,0),(i,1),(i,2)] for i in range(3)
    ] + [
        [(0,i),(1,i),(2,i)] for i in range(3)
    ] + [
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]
    ]

    for line in lines:
        a,b,c = line
        if states[a[0]][a[1]] == states[b[0]][b[1]] == states[c[0]][c[1]] != None:
            winning_coords = line
            finish(states[a[0]][a[1]])
            return True
    return False

def finish(symbol):
    global game_over
    game_over = True

    if mode == "2" and symbol == "X":
        play_sound_nonblocking("Kalah.mp3")
    else:
        play_sound_nonblocking("Win.mp3")

    confetti()
    popup(symbol)

def popup(symbol):
    name = player1_name if symbol == "O" else player2_name
    messagebox.showinfo("Pemenang!", f"{name} MENANG!")

def draw():
    global game_over
    game_over = True
    play_sound_nonblocking("Seri.mp3")
    messagebox.showinfo("Seri", "Permainan Seri!")

def confetti():
    confetti_pieces.clear()
    confetti_canvas.delete("all")
    for _ in range(40):
        x = random.randint(0, ROOT_W-10)
        y = random.randint(-150, 0)
        color = random.choice(["#FFC0EB","#FF99DA","#FFB6C9","#FFFFFF","#87CEFA","#FFD700"])
        oval = confetti_canvas.create_oval(x,y,x+8,y+8, fill=color, outline="")
        confetti_pieces.append([oval,x,y,random.randint(3,8)])
    move_confetti()


def move_confetti():
    if not game_over: return
    for p in confetti_pieces:
        oval,x,y,vy = p
        y += vy
        x += random.randint(-2,2)
        confetti_canvas.coords(oval,x,y,x+8,y+8)
        p[1],p[2] = x,y
    confetti_canvas.after(60, move_confetti)

def choose_move():

    if cpu_level == "1":
        return random_move()      
    elif cpu_level == "2":
        return block_or_random()  
    else:
        return find_best_move()   

def random_move():
    available = [(r,c) for r in range(3) for c in range(3) if states[r][c] is None]
    return random.choice(available)

def block_or_random():
    for r,c in possible_winning_moves("X"):
        return (r,c)

    for r,c in possible_winning_moves("O"):
        return (r,c)

    return random_move()

def possible_winning_moves(symbol):
    moves = []
    lines = [
        [(i,0),(i,1),(i,2)] for i in range(3)
    ] + [
        [(0,i),(1,i),(2,i)] for i in range(3)
    ] + [
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]
    ]

    for line in lines:
        vals = [states[r][c] for r,c in line]
        if vals.count(symbol) == 2 and vals.count(None) == 1:
            idx = vals.index(None)
            moves.append(line[idx])
    return moves

def find_best_move():
    for r,c in possible_winning_moves("X"):
        return (r,c)

    for r,c in possible_winning_moves("O"):
        return (r,c)

    if states[1][1] is None:
        return (1,1)
    
    corners = [(0,0),(0,2),(2,0),(2,2)]
    random.shuffle(corners)
    for r,c in corners:
        if states[r][c] is None:
            return (r,c)

    return random_move()

def reset_game():
    global states, current_turn, game_over
    play_sound_nonblocking("Mulai.mp3")
    states = [[None]*3 for _ in range(3)]
    game_over = False
    current_turn = "O"
    confetti_pieces.clear()
    confetti_canvas.delete("all")
    for r in range(3):
        for c in range(3):
            canvases[r][c].itemconfigure(text_items[r][c], text="", font=FONT_BASE)
    status_label.config(text=f"Giliran: {player1_name}", fg=COLOR_O)

reset_btn = Button(root, text="RESET", font=("Comic Sans MS", 18, "bold"),
                   bg="#FF99CC", fg="white", command=reset_game,
                   bd=4, padx=20, cursor="hand2")
reset_btn.place(relx=0.5, rely=0.92, anchor="center")


status_label.config(text=f"Giliran: {player1_name}", fg=COLOR_O)

play_background_music() 
reset_game()
root.mainloop()