import tkinter
from turtle import bgcolor
from Cargar_arch import cargar


ventana_reportes = tkinter.Toplevel()
ventana_reportes.geometry("500x400")
ventana_reportes.configure(bg="light blue")
etiqueta = tkinter.Label(ventana_reportes, text = "REPORTES", background="light blue",font=("Comic Sans MS", 20,"bold"))
etiqueta.place(x = 175, y = 5)


boton_tokens = tkinter.Button(ventana_reportes, text = "Reporte de Tokens", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
boton_errores = tkinter.Button(ventana_reportes, text = "Reporte Errores", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
boton_usuario = tkinter.Button(ventana_reportes, text = "Manual de Usuario", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
boton_tecnico = tkinter.Button(ventana_reportes, text = "Manual Tecnico", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
boton_tokens.place(x = 30, y = 60)
boton_errores.place(x = 275, y = 60)
boton_usuario.place(x = 30, y = 250)
boton_tecnico.place(x = 275, y = 250)



boton_salir = tkinter.Button(ventana_reportes, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white")
boton_salir.place(x = 435, y = 0)


#FUNCIONES
def opcion_elegida(opcion):

    if(opcion == 1):
        print("AQUI SE SELECCIONA EL ARCHIVO .FORM ")
        contenido_data = cargar()
        print(contenido_data)

    if(opcion == 2):
        print("AQUI SE SELECCIONA INSTRUCCIONES.LFP ")
    
    if(opcion == 3):
        print("AQUI SE SELECCIONA EL ARCHIVO .FORM ")
        contenido_data = cargar()
        print(contenido_data)

    if(opcion == 4):
        print("AQUI SE SELECCIONA INSTRUCCIONES.LFP ")


'''
caja_texto = tkinter.Entry(ventana_nueva, font = "Helvetica 30")
caja_texto.pack()

def saludo (nombre):
    print("holaa"+nombre)

def extraer_texto():
    entrada = caja_texto.get()
    print(entrada)

def extraer_texto_etiqueta():
    entrada = caja_texto.get()
    etiqueta["text"] = entrada 

boton1 = tkinter.Button(ventana_nueva, text= "presiona",width=10, height=5, command = extraer_texto_etiqueta)
boton1.pack()
#boton1 = tkinter.Button(ventana_nueva, text= "presiona", command = lambda:  saludo(" yenifer"))
#boton1.pack()




class Ventana_reportes:
    def __init__(self):
        ventana_reportes = tkinter.Tk()
        ventana_reportes.geometry("500x400")
        ventana_reportes.configure(bg="light blue")
        etiqueta = tkinter.Label(ventana_reportes, text = "REPORTES", background="light blue",font=("Comic Sans MS", 20,"bold"))
        etiqueta.place(x = 175, y = 5)

        boton_tokens = tkinter.Button(ventana_reportes, text = "Reporte de Tokens", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
        boton_errores = tkinter.Button(ventana_reportes, text = "Reporte Errores", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
        boton_usuario = tkinter.Button(ventana_reportes, text = "Manual de Usuario", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
        boton_tecnico = tkinter.Button(ventana_reportes, text = "Manual Tecnico", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
        boton_tokens.place(x = 30, y = 60)
        boton_errores.place(x = 275, y = 60)
        boton_usuario.place(x = 30, y = 250)
        boton_tecnico.place(x = 275, y = 250)



        boton_salir = tkinter.Button(self.ventana_reportes, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white")
        boton_salir.place(x = 435, y = 0)

        ventana_reportes.mainloop()


#FUNCIONES
def opcion_elegida(opcion):

    if(opcion == 1):
        print("AQUI SE SELECCIONA EL ARCHIVO .FORM ")
        contenido_data = cargar()
        print(contenido_data)

    if(opcion == 2):
        print("AQUI SE SELECCIONA INSTRUCCIONES.LFP ")
    
    if(opcion == 3):
        print("AQUI SE SELECCIONA EL ARCHIVO .FORM ")
        contenido_data = cargar()
        print(contenido_data)

    if(opcion == 4):
        print("AQUI SE SELECCIONA INSTRUCCIONES.LFP ")


    
'''
ventana_reportes.mainloop()