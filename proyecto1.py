from tkinter import *
from tkinter import messagebox

root = Tk()

# <----- FUNCIONES ------------>

def salir():
    value = messagebox.askquestion('salir', '¿Desea salir de la aplicación?')
    if value == 'yes':
        root.destroy()














# <---- INTERFAZ GRAFICA ------->

barra_menu = Menu(root)
root.config(menu=barra_menu, width=300, height=300)

BBDD_menu = Menu(barra_menu, tearoff=0)
BBDD_menu.add_command(label="Crear")
BBDD_menu.add_separator()
BBDD_menu.add_command(label="Salir", command=salir)

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campos")


CRUD_menu = Menu(barra_menu, tearoff=0)
CRUD_menu.add_command(label="Crear")
CRUD_menu.add_command(label="Leer")
CRUD_menu.add_command(label="Actualizar")
CRUD_menu.add_command(label="Borrar")

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de...")


barra_menu.add_cascade(label="BBDD", menu=BBDD_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=CRUD_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)


mi_frame = Frame(root)
mi_frame.pack()


id_entry = Entry(mi_frame)
id_entry.grid(padx=5, pady=5, row=0, column=1)
nombre_entry = Entry(mi_frame).grid(padx=5, pady=5, row=1, column=1)
apellido_entry = Entry(mi_frame).grid(padx=5, pady=5, row=2, column=1)
password_entry = Entry(mi_frame).grid(padx=5, pady=5, row=3, column=1)
direccion_entry = Entry(mi_frame).grid(padx=5, pady=5, row=4, column=1)
comentarios_text = Text(mi_frame, width=16, height=5).grid(padx=5, pady=5, row=5, column=1)



id_label = Label(mi_frame,text='ID:')
id_label.grid(padx=5, pady=5, row=0,column=0, sticky='e')

nombre_label = Label(mi_frame,text='Nombre:')
nombre_label.grid(padx=5, pady=5, row=1,column=0, sticky='e')

apellido_label = Label(mi_frame,text='Apellido:')
apellido_label.grid(padx=5, pady=5, row=2,column=0, sticky='e')

password_label = Label(mi_frame,text='Contraseña:')
password_label.grid(padx=5, pady=5, row=3,column=0, sticky='e')

direccion_label = Label(mi_frame,text='Direccion:')
direccion_label.grid(padx=5, pady=5, row=4,column=0, sticky='e')

comentarios_label = Label(mi_frame,text='Comentarios:')
comentarios_label.grid(padx=5, pady=5, row=5,column=0, sticky='e')



mi_frame2 = Frame(root)
mi_frame2.pack()


create_button = Button(mi_frame2, text='Create')
create_button.grid(padx=5, pady=5, row=0, column=0)

read_button = Button(mi_frame2, text='Read')
read_button.grid(padx=5, pady=5, row=0, column=1)

update_button = Button(mi_frame2, text='Update')
update_button.grid(padx=5, pady=5, row=0, column=2)

delete_button = Button(mi_frame2, text='Delete')
delete_button.grid(padx=5, pady=5, row=0, column=3)


root.mainloop()
