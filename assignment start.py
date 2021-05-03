import tkinter as tk
HEIGHT = 700
WIDTH = 800
root = tk.Tk()

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

frame= tk.Frame(root,bg='cyan')
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

button = tk.Button(frame,text='test button',bg='red',fg='orange')
button.pack(side='left',fill='both')

label= tk.Label(frame, text="this is alabel",bg="green")
label.place(relx=0,rely=0,relwidth=0.25,relheight=0.35)

entry=tk.Entry(frame,bg='white')
entry.pack()
root.mainloop()