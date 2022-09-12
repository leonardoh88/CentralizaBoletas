from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END

import psycopg2

root = Tk()
root.title("Python & PosgreSQL")

##GUARDAR BOLETA EN BD
def save_new_boleta(rut,  CONSUMO, precio):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="leo", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''INSERT INTO boleta(rut, CONSUMO, precio) VALUES (%s, %s, %s)'''
    cursor.execute(query, (rut,  CONSUMO, precio))
    print("succesfully data inserted")
    conn.commit()
    conn.close()
    # refresh with new boleta
    display_boleta()


##BUSCAR BOLETA POR ID
def search(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="leo", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM boleta where id=%s'''
    cursor.execute(query, (id))

    row = cursor.fetchone()
    print(row)
    display_search_result(row)

    conn.commit()
    conn.close()

##MOSTRAR BOLETA BUSCADA
def display_search_result(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W+E)
    listbox.insert(END, row)

##MOSTRAR BOLETAS EN EL GRID
def display_boleta():
    conn = psycopg2.connect(dbname="postgres", user="postgres",
                            password="leo", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM boleta'''
    cursor.execute(query)

    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, columnspan=4, sticky=W+E)
    for x in row:
      listbox.insert(END, x)

    conn.commit()
    conn.close()


#CANVAS (INTERFAZ DE PYTHON)

canvas = Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="BOLETA")
label.grid(row=0, column=1)

#_rut Input
label = Label(frame, text="RUT")
label.grid(row=1, column=0)

entry_rut = Entry(frame)
entry_rut.grid(row=1, column=1)
entry_rut.focus()

# CONSUMO
label = Label(frame, text="TIPO CONSUMO")
label.grid(row=2, column=0)

entry_CONSUMO = Entry(frame)
entry_CONSUMO.grid(row=2, column=1)

# PRECIO
label = Label(frame, text="PRECIO")
label.grid(row=3, column=0)

entry_precio = Entry(frame)
entry_precio.grid(row=3, column=1)


#BOTON AGREGAR
button = Button(frame, text="AGREGAR", command=lambda: save_new_boleta(
    entry_rut.get(), entry_CONSUMO.get(), entry_precio.get()))
button.grid(row=4, column=1, sticky=W+E)


#BOTON BUSCAR
label = Label(frame, text="LISTA")
label.grid(row=6, column=1)

label = Label(frame, text="INGRESA ID:")
label.grid(row=7, column=0)

id_search = Entry(frame)
id_search.grid(row=7, column=1)

button = Button(frame, text="BUSCAR", command=lambda: search(id_search.get()))
button.grid(row=7, column=2)


display_boleta()
root.mainloop()
