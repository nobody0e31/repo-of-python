import tkinter as tk

def start_timer(count):
    minutes, seconds = divmod(count, 60)
    label.config(text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        root.after(1000, start_timer, count - 1)
    else:
        label.config(text="Done!")

root = tk.Tk()
# Keeps the window floating on top of all other apps
root.attributes('-topmost', True) 
# Removes window borders for a clean, minimalist look
root.overrideredirect(True) 
# Sets window size and starting position
root.geometry("100x40+100+100") 
root.configure(bg='black')

label = tk.Label(root, text="25:00", font=("Helvetica", 24), fg="white", bg="black")
label.pack(expand=True)

# Click the timer to start the countdown
label.bind("<Button-1>", lambda e: start_timer(25 * 60))
# Two-finger tap (right-click) to close the timer
label.bind("<Button-2>", lambda e: root.destroy()) 
label.bind("<Button-3>", lambda e: root.destroy())

root.mainloop()