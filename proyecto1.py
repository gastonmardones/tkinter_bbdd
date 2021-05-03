import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter.constants import END

root = Tk()

# <-------------------------- FUNCIONES -------------------------------------->


def conexionBBDD():

    sql = '''
        CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR (20),
            APELLIDO VARCHAR (20),
            PASSWORD VARCHAR (20),
            DIRECCION VARCHAR (20),
            COMENTARIOS VARCHAR (100))
        '''

    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='gaston22',
        database='usuarios'
    )

    cursor = cnx.cursor()

    try:
        cursor.execute('''
            CREATE TABLE datos_usuarios(
                ID INT PRIMARY KEY AUTO_INCREMENT,
                NOMBRE VARCHAR (30),
                APELLIDO VARCHAR (30),
                PASSWORD VARCHAR (16),
                DIRECCION VARCHAR (50),
                COMENTARIOS VARCHAR (100))''')

        messagebox.showinfo('BBDD', 'Base de Datos creada con éxito')

    except:
        messagebox.showwarning('Atención', 'La Base de Datos ya existe')




def salir():
    value = messagebox.askquestion('salir', '¿Desea salir de la aplicación?')
    if value == 'yes':
        root.destroy()




def crear():
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='gaston22',
        database='usuarios'
    )
    cursor = cnx.cursor()
    sql = 'INSERT INTO datos_usuarios VALUES (NULL, %s, %s, %s, %s, %s)'
    datos = (nombre.get(), apellido.get(), password.get(),
             direccion.get(), comentarios_text.get("1.0", END))
    cursor.execute(sql, datos)
    cnx.commit()
    messagebox.showinfo('BBDD', 'Registro insertado con éxito')




def leer():

    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='gaston22',
        database='usuarios'
    )

    cursor = cnx.cursor()

    sql = 'SELECT * FROM datos_usuarios WHERE ID=' + mi_id.get()

    cursor.execute(sql)

    datos = cursor.fetchall()

    for i in datos:
        nombre.set(i[1])
        apellido.set(i[2])
        password.set(i[3])
        direccion.set(i[4])
        comentarios_text.insert('1.0', i[5])




def actualizar():

    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='gaston22',
        database='usuarios'
    )

    cursor = cnx.cursor()

    sql = '''UPDATE datos_usuarios SET nombre = %s, apellido = %s, password = %s, direccion = %s, comentarios = %s WHERE ID =''' + mi_id.get()

    datos = (nombre.get(), apellido.get(), password.get(),
             direccion.get(), comentarios_text.get("1.0", END))

    cursor.execute(sql, datos)
    cnx.commit()

    messagebox.showinfo('BBDD','Registro actualizado con éxito')




def borrar():
    
    cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='gaston22',
    database='usuarios'
    )

    cursor = cnx.cursor()

    sql = 'DELETE FROM datos_usuarios WHERE ID='+ mi_id.get()
    
    cursor.execute(sql)
    
    cnx.commit()

    messagebox.showinfo('BBDD', 'Registro borrado con éxito')




def limpiar_campos():

    mi_id.set('')
    nombre.set('')
    apellido.set('')
    password.set('')
    direccion.set('')
    comentarios_text.delete('1.0', END)




# <---------------------------------- INTERFAZ GRAFICA ----------------------------------------->

# <---------------------------------- BARRA MENU ----------------------------------------------->

barra_menu = Menu(root)
root.config(menu=barra_menu, width=300, height=300)

BBDD_menu = Menu(barra_menu, tearoff=0)
BBDD_menu.add_command(label="Crear", command=conexionBBDD)
BBDD_menu.add_separator()
BBDD_menu.add_command(label="Salir", command=salir)

limpiar_menu = Menu(barra_menu, tearoff=0)
limpiar_menu.add_command(label="Limpiar Campos", command=limpiar_campos)


CRUD_menu = Menu(barra_menu, tearoff=0)
CRUD_menu.add_command(label="Crear", command=crear)
CRUD_menu.add_command(label="Leer", command=leer)
CRUD_menu.add_command(label="Actualizar", command=actualizar)
CRUD_menu.add_command(label="Borrar", command=borrar)

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de...")


barra_menu.add_cascade(label="BBDD", menu=BBDD_menu)
barra_menu.add_cascade(label="Campos", menu=limpiar_menu)
barra_menu.add_cascade(label="CRUD", menu=CRUD_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)



# <--------------------------------------------- ENTRYS ------------------------------------------------->

mi_frame = Frame(root)
mi_frame.pack()

mi_id = StringVar()
nombre = StringVar()
apellido = StringVar()
password = StringVar()
direccion = StringVar()


id_entry = Entry(mi_frame, textvariable=mi_id)
id_entry.grid(padx=5, pady=5, row=0, column=1)

nombre_entry = Entry(mi_frame, textvariable=nombre)
nombre_entry.grid(padx=5, pady=5, row=1, column=1)

apellido_entry = Entry(mi_frame, textvariable=apellido)
apellido_entry.grid(padx=5, pady=5, row=2, column=1)

password_entry = Entry(mi_frame, textvariable=password, show='*')
password_entry.grid(padx=5, pady=5, row=3, column=1)

direccion_entry = Entry(mi_frame, textvariable=direccion)
direccion_entry.grid(padx=5, pady=5, row=4, column=1)

comentarios_text = Text(mi_frame, width=16, height=5)
comentarios_text.grid(padx=5, pady=5, row=5, column=1)


scrollVert = Scrollbar(mi_frame, command=comentarios_text.yview)
scrollVert.grid(row=5, column=2, sticky='nsew')
comentarios_text.config(yscrollcommand=scrollVert.set)



# <-------------------------------------------------- LABELS ---------------------------------------------------->

id_label = Label(mi_frame, text='ID:')
id_label.grid(padx=5, pady=5, row=0, column=0, sticky='e')

nombre_label = Label(mi_frame, text='Nombre:')
nombre_label.grid(padx=5, pady=5, row=1, column=0, sticky='e')

apellido_label = Label(mi_frame, text='Apellido:')
apellido_label.grid(padx=5, pady=5, row=2, column=0, sticky='e')

password_label = Label(mi_frame, text='Contraseña:')
password_label.grid(padx=5, pady=5, row=3, column=0, sticky='e')

direccion_label = Label(mi_frame, text='Direccion:')
direccion_label.grid(padx=5, pady=5, row=4, column=0, sticky='e')

comentarios_label = Label(mi_frame, text='Comentarios:')
comentarios_label.grid(padx=5, pady=5, row=5, column=0, sticky='e')



# <----------------------------------------------------- CRUD BUTTONS ------------------------------------------------------------>

mi_frame2 = Frame(root)
mi_frame2.pack()


create_button = Button(mi_frame2, text='Create', command=crear)
create_button.grid(padx=5, pady=5, row=0, column=0)

read_button = Button(mi_frame2, text='Read', command=leer)
read_button.grid(padx=5, pady=5, row=0, column=1)

update_button = Button(mi_frame2, text='Update', command=actualizar)
update_button.grid(padx=5, pady=5, row=0, column=2)

delete_button = Button(mi_frame2, text='Delete', command=borrar)
delete_button.grid(padx=5, pady=5, row=0, column=3)


root.mainloop()
