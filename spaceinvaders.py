import tkinter as tk
import random
from tkinter import messagebox

# --- Game variables ---
score = 0
lives = 5
level = 1
speed = 1000
goal = 100

# --- Functions ---
def move_character():
    if lives > 0 and score < goal:
        new_x = random.randint(50, 700)
        new_y = random.randint(80, 500)
        btn_target.place(x=new_x, y=new_y)
        root.after(speed, move_character)

def on_click():
    global score, speed, level

    if lives <= 0:
        return

    score += 1

    # Every 5 points → level up
    if score % 5 == 0:
        level += 1
        speed = max(300, speed - 50)
        root.config(bg=random.choice(["#f0f0f0", "#e1f5fe", "#fff9c4"]))

    update_ui()

    if score >= goal:
        messagebox.showinfo("ПЕРЕМОГА!", f"Ти набрав {goal} очок! Рівень: {level}")
        reset_game()

def miss_click(event):
    global lives
    if event.widget != btn_target and lives > 0:
        lives -= 1
        update_ui()
        if lives <= 0:
            messagebox.showinfo("GAME OVER", "Ти програв!")
            reset_game()

def update_ui():
    label_info.config(text=f"Очки: {score} | Життя: {lives} | Рівень: {level}")

def reset_game():
    global score, lives, speed, level
    score = 0
    lives = 5
    speed = 1000
    level = 1
    root.config(bg="black")
    update_ui()
    move_character()

# --- UI setup ---
root = tk.Tk()
root.title("Cyber Hunter 2026")
root.geometry("800x600")
root.resizable(False, False)
root.config(bg="black")

root.bind("<Button-1>", miss_click)

label_info = tk.Label(
    root,
    text="Очки: 0 | Життя: 5 | Рівень: 1",
    font=("Courier New", 20, "bold"),
    bg="#333",
    fg="white"
)
label_info.pack(fill="x")

btn_target = tk.Button(
    root,
    text="👾",
    font=("Arial", 35),
    command=on_click,
    bg="#4caf50",
    fg="white",
    width=3,
    relief="raised"
)
btn_target.place(x=350, y=250)

move_character()
root.mainloop()