# IMPORTS
import tkinter as tk
root = tk.Tk() 
root.geometry("600x600")
frame = tk.Frame() 
frame.master.title("Hello PNC")
canvas=tk.Canvas(frame)


# #CONSTANTS
color={"blue","red","green","purple","yello"}

# Verrible
# Game-Over= False
oval1=canvas.create_rectangle(0,0,600,600, fill="yellow")
oval2=canvas.create_rectangle(0,0,600,20, fill="black")
oval3=canvas.create_rectangle(0,0,20,600, fill="black")
oval4=canvas.create_rectangle(580,600,600,0, fill="black")
oval4=canvas.create_rectangle(0,580,600,600, fill="black")
snake=canvas.create_oval(50,50,80,80, fill="cyan")
snake=canvas.create_oval(60,50,70,60, fill="black")



# display
frame.pack(expand=True, fill="both")
canvas.pack(expand=True, fill='both')
root.mainloop()





