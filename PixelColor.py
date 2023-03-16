from tkinter import *

def damier(): #fonction dessinant le tableau
    ligne_vert()
    ligne_hor()
        
def ligne_vert():
    c_x = 0
    while c_x != width:
        can1.create_line(c_x,0,c_x,height,width=1,fill='grey')
        c_x+=c
        
def ligne_hor():
    c_y = 0
    while c_y != height:
        can1.create_line(0,c_y,width,c_y,width=1,fill='grey')
        c_y+=c

def click_gauche(event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill=liste.get(ACTIVE),outline='white')
    dico_case[x,y]=1

    pixel.append(str(x) + ' ' + str(y))
    pixel.append(liste.get(ACTIVE))

    print(str(pixel))
    # print(str(pixel_color))

def click_droit(event): #fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='white',outline='white')
    dico_case[x,y]=0
    if pixel.count(str(x)+ ' ' +str(y)) == 1:
        pixel.remove(str(x)+ ' ' +str(y))
    print(str(pixel))
    # print(str(pixel_color))
    # pixel.pop
    print(pixel.index('Black'))


def create():
    pass

def clear():
    print(type(can1.size + 1))
    # can1.create_rectangle(x, y, x+c, y+c, fill='white',outline='white')


height = 600
width = 650

#taille des cellules
c = 10

# flag=0
# dico_etat = {} 
dico_case = {} 
i=0
while i!= width/c: 
    j=0
    while j!= height/c:
        x=i*c
        y=j*c
        dico_case[x,y]=0
        j+=1
    i+=1

#programme "principal" 
fen1 = Tk()

title='PixelColor'
fen1.title(title)

fen1.minsize(256,256)
fen1.maxsize(640, 640)

# print(fen1.sizefrom())

can1 = Canvas(fen1, width =width, height =height, bg ='white')
can1.bind("<Button-1>", click_gauche)
can1.bind("<Button-3>", click_droit)
can1.pack(side =TOP, padx =5, pady =5)

fen1.grid_rowconfigure(0, weight=1)
fen1.grid_columnconfigure(0, weight=1)

## Le canvas
# cnv = Canvas(fen1)
can1.grid(row=0, column=0, sticky='nswe')

## Les scrollbars
hScroll = Scrollbar(fen1, orient=HORIZONTAL, command=can1.xview)
hScroll.grid(row=1, column=0, sticky='we')

vScroll = Scrollbar(fen1, orient=VERTICAL, command=can1.yview)
vScroll.grid(row=0, column=1, sticky='ns')

can1.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)


menu = Menu(fen1)
file = Menu(menu,tearoff=0)

file.add_command(label='New', command=clear)



menu.add_cascade(label='file',menu= file)

menu.add_command(label='Create', command=None)
fen1.config(menu=menu)


frm = Frame(can1)
## Les labels et entrys dans le frame
# for i in range(50):
#     Label(frm, text='Label%s: ' % i).grid(row=i, column=0)
#     Entry(frm).grid(row=i, column=1)
## Pour etre sur que les dimensions sont calculées
frm.update()

## Création de la window dans le Canvas
can1.create_window(0, 0, window=frm, anchor=NW)

## La scrollregion est la boite englobante pour tout ce qu'il y a dans le Canvas
can1.configure(scrollregion=can1.bbox(ALL))


# damier()

pixel = []
pixel_color = []


color = ["Black","White",'Grey',"Red","Blue","Green","Yellow","Pink","Brown","Purple","Cyan"]
# color.remove("Black")
# liste
liste = Listbox(frm,justify='center',width=7,height=4)
# liste.insert(1, "Black")
# liste.insert(2, "White")
# liste.insert(3, "Red")
# liste.insert(4, "Blue")
# liste.insert(5, "Green")
# liste.insert(6, "Yellow")
# liste.insert(7, "Pink")
# liste.insert(8, "Brown")
# liste.insert(9, "Purple")
# liste.insert(10, "Cyan")

for i in color:
    liste.insert(END, i)

liste.pack()

print()
# liste.

# # print(liste.get(1.0,END))
# print(liste.focus())


fen1.mainloop()

