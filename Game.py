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



canvas.create_rectangle(0,0,0,0, fill="yellow")
# canvas.create_rectangle(0,20,20,600, fill="teal")
# canvas.create_rectangle(0,600,20,600, fill="teal")
# canvas.create_rectangle(0,600,20,600, fill="teal")
# FUNCTIONS




# convas.creat_oval(12,14,39,30)
# # display
frame.pack(expand=True, fill="both")
canvas.pack(expand=True, fill='both')
root.mainloop()






# for row in range(10):
#     x1=0
#     y1=0
#     x2=x1+50
#     y2=x2+50
#     for column in range(10):
#         canvas.create_rectangle(x1,y1,x2,y2, fill="teal")



