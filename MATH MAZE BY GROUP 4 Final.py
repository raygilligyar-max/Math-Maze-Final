import tkinter as tk
from tkinter import messagebox
import random

BG = "#02170F"

THEMES = [
    ("Green", "#064E3B"),
    ("Blue", "#1E3A8A"),
    ("Purple", "#4C1D95"),
    ("Dark", "#111827")
]


class MathMaze:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Maze Adventure")
        self.root.geometry("1500x950")
        self.root.configure(bg=BG)

        self.active = False
        self.running = False
        self.paused = False

        self.player_skins = ["🙂", "🧑‍🚀", "🧙", "🥷", "🤖"]
        self.player_skin = 0

        self.theme = 0
        self.cell_color = THEMES[self.theme][1]

        self.root.bind_all("<KeyPress>", self.move)

        self.login()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        self.clear()

        tk.Label(self.root, text="PLEASE ENTER YOUR NAME",
                 font=("Arial", 60, "bold"),
                 fg="#FACC15", bg=BG).pack(pady=30)

        self.entry = tk.Entry(self.root, font=("Arial", 24), justify="center")
        self.entry.pack(pady=10)

        def enter_game():
            name = self.entry.get().strip().title()

            if name == "":
                messagebox.showwarning("Missing Name", "Please enter your name first!")
                return

            self.player_name = name
            self.home()

        self.menu_btn("ENTER GAME", "#10B981", enter_game)

    def menu_btn(self, text, color, cmd):
        btn = tk.Button(self.root, text=text,
                        font=("Arial", 18, "bold"),
                        width=22, height=2,
                        bg=color, fg="white",
                        command=cmd)
        btn.pack(pady=6)

        btn.bind("<Enter>", lambda e: btn.config(bg="#FACC15", fg="black"))
        btn.bind("<Leave>", lambda e: btn.config(bg=color, fg="white"))

    def home(self):
        self.active = False
        self.running = False
        self.clear()

        welcome = f"WELCOME, {getattr(self, 'player_name', 'PLAYER')}"
        tk.Label(self.root, text=welcome,
                 font=("Arial", 48, "bold"),
                 fg="#FACC15", bg=BG).pack(pady=20)

        self.menu_btn("START GAME", "#10B981", self.start)
        self.menu_btn("📘 TUTORIAL", "#8B5CF6", self.tutorial)
        self.menu_btn("🎭 SKINS", "#6366F1", self.skins)
        self.menu_btn("🎨 MAP COLORS", "#0EA5E9", self.map_colors)
        self.menu_btn("📜 CREDITS", "#F59E0B", self.credits)
        self.menu_btn("❌ EXIT", "#EF4444", self.root.destroy)

    def tutorial(self):
        self.clear()

        container = tk.Frame(self.root, bg=BG)
        container.pack(expand=True)

    # Title
        tk.Label(container, text="📘 HOW TO PLAY",
             font=("Arial", 42, "bold"),
             fg="#FACC15", bg=BG).pack(pady=20)

    # Movement Section
        tk.Label(container, text="🎮 Movement",
             font=("Arial", 24, "bold"),
             fg="#34D399", bg=BG).pack(pady=5)

        tk.Label(container,
             text="Use W A S D keys to move through the maze",
             font=("Arial", 16),
             fg="white", bg=BG).pack(pady=5)

    # Objective
        tk.Label(container, text="🏁 Objective",
             font=("Arial", 24, "bold"),
             fg="#F87171", bg=BG).pack(pady=10)

        tk.Label(container,
             text="Reach the finish line at the bottom-right of the maze",
             font=("Arial", 16),
             fg="white", bg=BG).pack(pady=5)

    # Questions
        tk.Label(container, text="❓ Math Tiles",
             font=("Arial", 24, "bold"),
             fg="#60A5FA", bg=BG).pack(pady=10)

        tk.Label(container,
             text="Solve math questions to gain time and score",
             font=("Arial", 16),
             fg="white", bg=BG).pack(pady=5)

    # Power Tiles
        tk.Label(container, text="⚡ Power Tiles",
             font=("Arial", 24, "bold"),
             fg="#A78BFA", bg=BG).pack(pady=10)

        tk.Label(container,
             text="⏱ Time Tile → +20 seconds\n"
                  "💎 Score Tile → +50 points\n"
                  "❄ Freeze Tile → Stops timer briefly",
             font=("Arial", 16),
             fg="white", bg=BG,
             justify="center").pack(pady=5)

    # Streak System
        tk.Label(container, text="🔥 Streak System",
             font=("Arial", 24, "bold"),
             fg="#FBBF24", bg=BG).pack(pady=10)

        tk.Label(container,
             text="Answer correctly in a row to gain bonus score and time",
             font=("Arial", 16),
             fg="white", bg=BG).pack(pady=5)

    # Controls
        tk.Label(container, text="⏸ Controls",
             font=("Arial", 24, "bold"),
             fg="#F59E0B", bg=BG).pack(pady=10)

        tk.Label(container,
             text="Use the Pause button to stop the game anytime",
             font=("Arial", 16),
             fg="white", bg=BG).pack(pady=5)

    # Back button
        tk.Button(container, text="⬅ BACK",
              font=("Arial", 18, "bold"),
              bg="#EF4444", fg="white",
              command=self.home).pack(pady=25)
    
    def skins(self):
        self.clear()
        tk.Label(self.root, text="SKINS",
                 font=("Arial", 40, "bold"),
                 fg="#FACC15", bg=BG).pack(pady=20)

        tk.Label(self.root,
                 text=self.player_skins[self.player_skin],
                 font=("Arial", 40),
                 fg="white", bg=BG).pack()

        self.menu_btn("NEXT", "#6366F1", self.next_player)
        self.menu_btn("BACK", "#EF4444", self.home)

    def next_player(self):
        self.player_skin = (self.player_skin + 1) % len(self.player_skins)
        self.skins()

    def map_colors(self):
        self.clear()

        tk.Label(self.root, text="MAP COLORS",
                 font=("Arial", 40, "bold"),
                 fg="#FACC15", bg=BG).pack(pady=20)

        for i, (name, color) in enumerate(THEMES):
            tk.Button(self.root, text=name, bg=color,
                      width=20, height=2,
                      command=lambda i=i: self.set_theme(i)).pack(pady=5)

        self.menu_btn("BACK", "#EF4444", self.home)

    def set_theme(self, i):
        self.theme = i
        self.cell_color = THEMES[i][1]

    def credits(self):
        self.clear()
        tk.Label(self.root, text="GROUP 4",
                 font=("Arial", 60, "bold"),
                 fg="#FACC15", bg=BG).pack(expand=True)
        self.menu_btn("BACK", "#EF4444", self.home)

    def start(self):
        self.clear()
        tk.Label(self.root, text="SELECT DIFFICULTY",
                 font=("Arial", 40, "bold"),
                 fg="#FACC15", bg=BG).pack(pady=30)

        self.menu_btn("EASY", "#10B981", lambda: self.start_game("easy"))
        self.menu_btn("MEDIUM", "#3B82F6", lambda: self.start_game("medium"))
        self.menu_btn("HARD", "#EF4444", lambda: self.start_game("hard"))
        self.menu_btn("BACK", "#EF4444", self.home)

    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.size = 31
        self.player = [1, 1]
        self.exit = [self.size - 2, self.size - 2]

        self.score = 0
        self.time_left = 180
        self.streak = 0
        self.paused = False

        self.generate_maze()
        self.generate_items()

        self.active = True
        self.running = True

        self.show()
        self.countdown()

    def generate_maze(self):
        self.walls = set((r, c) for r in range(self.size) for c in range(self.size))
        stack = [(1, 1)]
        self.walls.remove((1, 1))

        directions = [(-2,0),(2,0),(0,-2),(0,2)]

        while stack:
            x,y = stack[-1]
            neighbors = []

            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 1<=nx<self.size-1 and 1<=ny<self.size-1:
                    if (nx,ny) in self.walls:
                        neighbors.append((nx,ny,dx,dy))

            if neighbors:
                nx,ny,dx,dy = random.choice(neighbors)
                self.walls.remove((nx,ny))
                self.walls.remove((x+dx//2,y+dy//2))
                stack.append((nx,ny))
            else:
                stack.pop()

    def generate_question(self):
        if self.difficulty == "easy":
            a, b = random.randint(1, 10), random.randint(1, 10)
            return f"{a} + {b}", a + b

        elif self.difficulty == "medium":
            a, b, c = random.randint(2, 10), random.randint(2, 10), random.randint(2, 10)
            return random.choice([
                (f"{a} + {b} × {c}", a + b * c),
                (f"({a} + {b}) × {c}", (a + b) * c),
                (f"{a} × {b} - {c}", a * b - c),
                (f"{a*b} ÷ {a} + {c}", b + c)
            ])

        else:
            a, b, c, d = random.randint(2, 12), random.randint(2, 12), random.randint(2, 12), random.randint(2, 12)
            return random.choice([
                (f"({a} + {b}) × {c} - {d}", (a + b) * c - d),
                (f"{a} × {b} + {c} × {d}", a*b + c*d),
                (f"{a*b*c} ÷ {a} + {d}", b*c + d),
                (f"({a} × {b}) ÷ {a} + {c}", b + c),
                (f"{a} × ({b} + {c})", a * (b + c))
            ])

    def generate_items(self):
        self.items = {}
        while len(self.items) < 25:
            x = random.randrange(1,self.size-1,2)
            y = random.randrange(1,self.size-1,2)

            if (x,y) not in self.walls and [x,y] != self.player:
                chance = random.random()

                if chance < 0.1:
                    self.items[(x,y)] = ("TIME", None)
                elif chance < 0.2:
                    self.items[(x,y)] = ("SCORE", None)
                elif chance < 0.25:
                    self.items[(x,y)] = ("FREEZE", None)
                else:
                    self.items[(x,y)] = self.generate_question()

    def show(self):
        self.clear()

        self.score_label = tk.Label(self.root, text=f"⭐ {self.score} | 🔥 {self.streak}",
                                    font=("Arial",20,"bold"),
                                    fg="#FACC15", bg=BG)
        self.score_label.place(x=1200,y=20)

        self.timer_label = tk.Label(self.root, text=f"⏰ {self.time_left}",
                                    font=("Arial",20,"bold"),
                                    fg="white", bg=BG)
        self.timer_label.place(x=1200,y=70)

        tk.Button(self.root, text="⬅ MENU",
                  bg="#EF4444", fg="white",
                  command=self.home).place(x=20,y=20)

        self.pause_btn = tk.Button(self.root, text="⏸ PAUSE",
                                   bg="#F59E0B", fg="white",
                                   command=self.toggle_pause)
        self.pause_btn.place(x=20,y=70)

        center = tk.Frame(self.root,bg=BG)
        center.pack(expand=True)

        self.canvas = tk.Canvas(center,width=850,height=850,bg=BG)
        self.canvas.pack()

        self.draw()

    def toggle_pause(self):
        if not self.paused:
            self.paused = True
            self.running = False
            self.active = False
            self.pause_btn.config(text="▶ RESUME")
        else:
            self.paused = False
            self.running = True
            self.active = True
            self.pause_btn.config(text="⏸ PAUSE")
            self.countdown()

    def countdown(self):
        if self.running:
            self.time_left -= 1
            self.timer_label.config(text=f"⏰ {self.time_left}")

            if self.time_left <= 0:
                self.running = False
                self.active = False
                messagebox.showerror("TIME UP","You ran out of time!")
                self.home()
                return

            self.root.after(1000,self.countdown)

    def draw(self):
        self.canvas.delete("all")
        cell = 850 // self.size

        for i in range(self.size):
            for j in range(self.size):

                x1, y1 = j * cell, i * cell
                x2, y2 = x1 + cell, y1 + cell

                if (i, j) in self.walls:
                    color = "#022c22"
                else:
                    color = self.cell_color

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

                if [i, j] == self.exit:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FACC15")
                    self.canvas.create_text(x1+cell//2,y1+cell//2,text="🏁")

                elif (i, j) in self.items:
                    item = self.items[(i,j)][0]

                    colors = {"TIME":"#10B981","SCORE":"#3B82F6","FREEZE":"#8B5CF6"}
                    icons = {"TIME":"⏱","SCORE":"💎","FREEZE":"❄"}

                    self.canvas.create_rectangle(x1,y1,x2,y2,fill=colors.get(item,"#F59E0B"))
                    self.canvas.create_text(x1+cell//2,y1+cell//2,text=icons.get(item,"❓"))

                if [i, j] == self.player:
                    self.canvas.create_rectangle(x1,y1,x2,y2,fill="#FDE047")
                    self.canvas.create_text(x1+cell//2,y1+cell//2,
                                            text=self.player_skins[self.player_skin])

    def move(self,event):
        if not self.active or self.paused:
            return

        moves={"w":(-1,0),"s":(1,0),"a":(0,-1),"d":(0,1)}
        key = event.keysym.lower()

        if key in moves:
            dx,dy = moves[key]
            x = self.player[0]+dx
            y = self.player[1]+dy

            if (x,y) not in self.walls:
                self.player=[x,y]

        if tuple(self.player) in self.items:
            self.ask(tuple(self.player))

        if self.player==self.exit:
            self.win()
            return

        self.draw()

    def ask(self,pos):
        item = self.items.pop(pos)

        if item[0] == "TIME":
            self.time_left += 20
            self.draw()
            return

        elif item[0] == "SCORE":
            self.score += 50
            self.score_label.config(text=f"⭐ {self.score} | 🔥 {self.streak}")
            self.draw()
            return

        elif item[0] == "FREEZE":
            self.running = False
            self.root.after(5000, lambda: setattr(self, 'running', True))
            self.draw()
            return

        q,answer = item
        self.active=False

        win = tk.Toplevel(self.root)
        win.geometry("450x300")
        win.configure(bg=BG)
        win.grab_set()

        tk.Label(win,text="Solve This!",
                 font=("Arial",16,"bold"),
                 fg="#FACC15",bg=BG).pack(pady=10)

        tk.Label(win,text=q,
                 font=("Arial",28,"bold"),
                 fg="white",bg=BG).pack(pady=10)

        entry = tk.Entry(win,font=("Arial",20), justify="center")
        entry.pack(pady=10)
        entry.focus()

        def submit():
            if entry.get()==str(answer):
                self.streak += 1
                bonus = 10 + self.streak * 2

                self.score += bonus
                self.time_left += 5 + self.streak

                self.score_label.config(text=f"⭐ {self.score} | 🔥 {self.streak}")

                self.active=True
                win.destroy()
                self.draw()
            else:
                self.streak = 0
                entry.delete(0, tk.END)
                messagebox.showerror("Wrong","Try again!")

        tk.Button(win,text="✔ Submit",bg="#10B981",fg="white",
                  command=submit).pack(pady=5)

        tk.Button(win,text="⏭ Skip (-5 sec)",bg="#EF4444",fg="white",
                  command=lambda: [win.destroy(), self.resume_after_skip()]).pack(pady=5)

    def resume_after_skip(self):
        self.time_left -= 5
        self.streak = 0

        if self.time_left <= 0:
            self.running = False
            self.active = False
            messagebox.showerror("TIME UP", "You ran out of time!")
            self.home()
            return

        self.active = True
        self.draw()

    def win(self):
        self.active=False
        self.running=False

        win = tk.Toplevel(self.root)
        win.geometry("400x250")
        win.configure(bg=BG)

        tk.Label(win, text="🎉 YOU ESCAPED THE MAZE!",
                 font=("Arial",26,"bold"),
                 fg="#FACC15", bg=BG).pack(pady=20)

        tk.Label(win, text=f"Final Score: {self.score}",
                 font=("Arial",18),
                 fg="white", bg=BG).pack(pady=5)

        tk.Label(win, text=f"Time Left: {self.time_left}",
                 font=("Arial",14),
                 fg="#34D399", bg=BG).pack(pady=5)

        tk.Button(win, text="▶ Next Game",
                  bg="#10B981", fg="white",
                  command=lambda: [win.destroy(), self.start()]).pack(pady=5)

        tk.Button(win, text="🏠 Main Menu",
                  bg="#EF4444", fg="white",
                  command=lambda: [win.destroy(), self.home()]).pack(pady=5)


root = tk.Tk()
MathMaze(root)
root.mainloop()