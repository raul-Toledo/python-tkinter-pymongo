from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import pymongo

# Configuración de la GUI
root = Tk()
root.geometry('400x200+500+50')
root.resizable(0, 0)
root.title("Sensor de Movimiento")
num1 = IntVar()
num1.set(10)

#Para configurar el acceso a mi DB
user = StringVar(value="ulsa")
passw = StringVar(value="1234567890")
database = StringVar(value="Sensores")
cluster = StringVar(value="cluster0-e9jsl.mongodb.net")
coleccion = StringVar(value="movimiento")
SERVER = "mongodb+srv://"
OPCIONES = "?retryWrites=true&w=majority"
conexion = StringVar()
client = ""

# Donde voy a guardar los datos del sensor
snsrValue = IntVar(value=0)
snsrDate = StringVar(value=datetime.now())
snsrLoc = StringVar(value="Patio")


menubar = Menu(root)
root.config(menu=menubar)

configmenu = Menu(menubar, tearoff=0)
configmenu.add_command(label="Configurar base de datos", command=lambda: frame_configura())
configmenu.add_command(label="Guardar Dato", command=lambda: frame_guardar())
configmenu.add_command(label="Leer Dato", command=lambda: frame_leer())
configmenu.add_separator()
configmenu.add_command(label="Salir", command=root.quit)

menubar.add_cascade(label="Configurar", menu=configmenu)


def frame_leer():
    clear()
    mi_Frame = Frame()  # Creacion del Frame
    mi_Frame.pack()  # Empaquetamiento del Frame
    mi_Frame.config(width="400", height="200")  # cambiar tamaño
    mi_Frame.config(bd=5)  # cambiar el grosor del borde
    mi_Frame.config(relief="sunken")  # cambiar el tipo de borde
    mi_Frame.config(cursor="heart")  # cambiar el tipo de cursor
    mi_Frame.pack(fill='both', expand=1)
    mi_Frame.columnconfigure(1, weight=1)

    lblnum1 = Label(mi_Frame, text="Conección").grid(row=0, column=0, padx=5, pady=5)
    txtnum1 = Entry(mi_Frame, text="Numero 1", textvariable=conexion).grid(row=0, column=1, sticky="nsew", padx=5,
                                                                           pady=5)

    client = pymongo.MongoClient(conexion.get())
    client.list_database_names()

    lblnum1 = Label(mi_Frame, text=client.list_database_names()).grid(row=1, column=0, padx=5, pady=5, columnspan=2)


def frame_configura():
    clear()
    mi_Frame = Frame()  # Creacion del Frame
    mi_Frame.pack()  # Empaquetamiento del Frameo
    mi_Frame.config(width="400", height="200")  # cambiar tamaño
    mi_Frame.config(bd=5)  # cambiar el grosor del borde
    # flat, groove, raised, ridge, solid, or sunken
    mi_Frame.config(relief="flat")  # cambiar el tipo de borde
    mi_Frame.config(cursor="pirate")  # cambiar el tipo de cursor
    mi_Frame.pack(fill='both', expand=1)
    mi_Frame.columnconfigure(1, weight=1)

    lbluser = Label(mi_Frame, text="Usuario: ").grid(row=0, column=0, padx=5, pady=5)
    entuser = Entry(mi_Frame, text="Usuario", textvariable=user).grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    lblpass = Label(mi_Frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
    entpassw = Entry(mi_Frame, text="Password", textvariable=passw).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    lblcol = Label(mi_Frame, text="Base de datos:").grid(row=2, column=0, padx=5, pady=5)
    entcol = Entry(mi_Frame, text="Base de datos", textvariable=database).grid(row=2, column=1, sticky="nsew", padx=5,
                                                                               pady=5)

    lblcol = Label(mi_Frame, text="Colección:").grid(row=3, column=0, padx=5, pady=5)
    entcol = Entry(mi_Frame, text="Colección", textvariable=coleccion).grid(row=3, column=1, sticky="NSEW", padx=5,
                                                                            pady=5)

    lblclu = Label(mi_Frame, text="Cluster:").grid(row=4, column=0, padx=5, pady=5)
    entclu = Entry(mi_Frame, text="Cluster", textvariable=cluster).grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

    btnGuardar = Button(mi_Frame, text="Guadar Conexión", command=lambda: setconexion()).grid(row=5, column=0,
                                                                                              columnspan=2,
                                                                                              sticky="nsew", padx=5,
                                                                                              pady=5)


def frame_guardar():
    clear()
    mi_Frame = Frame()  # Creacion del Frame
    mi_Frame.pack()  # Empaquetamiento del Frameo
    mi_Frame.config(width="400", height="200")  # cambiar tamaño
    mi_Frame.config(bd=5)  # cambiar el grosor del borde
    # flat, groove, raised, ridge, solid, or sunken
    mi_Frame.config(relief="flat")  # cambiar el tipo de borde
    mi_Frame.pack(fill='both', expand=1)
    mi_Frame.columnconfigure(1, weight=1)

    lbluser = Label(mi_Frame, text="Fecha: ").grid(row=0, column=0, padx=5, pady=5)
    entuser = Entry(mi_Frame , textvariable=snsrDate).grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    lblpass = Label(mi_Frame, text="Ubicación:").grid(row=1, column=0, padx=5, pady=5)
    entpassw = Entry(mi_Frame, textvariable=snsrLoc).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    lblcol = Label(mi_Frame, text="Detecto:").grid(row=2, column=0, padx=5, pady=5)
    rbtnhigh = Radiobutton(mi_Frame, text="HIGH", value=1, variable=snsrValue).grid(row=2, column=1, sticky="nsew", padx=5,
                                                                               pady=5)
    rbtnlow = Radiobutton(mi_Frame, text="LOW", value=0,  variable=snsrValue).grid(row=3, column=1, sticky="nsew", padx=5,
                                                                               pady=5)

    btnGuardar = Button(mi_Frame, text="Guadar Conexión", command=lambda: save()).grid(row=5, column=0,
                                                                                              columnspan=2,
                                                                                              sticky="nsew", padx=5,
                                                                                              pady=5)


def clear():
    list = root.pack_slaves()
    for l in list:
        l.pack_forget()


def setconexion():
    strtemp = ""

    strtemp = SERVER + user.get() + ":" + passw.get() + "@" + cluster.get() + "/" + database.get() + OPCIONES
    conexion.set(strtemp)

    messagebox.showinfo("Conexión", "Conexión guardada")


def save():
    #el valor que guardo en la DB
    document = {"place": snsrLoc.get(),
                "datetime": snsrDate.get(),
                "value": snsrValue.get()}
    #Nos conectamos al servidor
    client = pymongo.MongoClient(conexion.get())
    #Que DB voy a utilizar
    db = client[database.get()]
    #Que colección voy a utilizar
    colection = db[coleccion.get()]
    #Voy a guardar los datos
    data = colection.insert_one(document)
    print(data.inserted_id)
    messagebox.showinfo("Guardar", "Documento guardado con id:" + str(data.inserted_id))

# Finalmente bucle de la aplicación
root.mainloop()