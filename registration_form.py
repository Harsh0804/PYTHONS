from tkinter import *
top=Tk()
mb=Menubutton(top,text=&quot;GfG&quot;)
mb.grid()
mb.menu=Menu(mb,tearoff=0)
mb[&quot;menu&quot;]=mb.menu
cVar=IntVar()
aVar=IntVar()
mb.menu.add_checkbutton(label="Contact",variable=cVar)
mb.menu.add_checkbutton(label="About",variable=aVar)
mb.pack()
top.mainloop()