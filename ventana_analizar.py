import tkinter
from turtle import bgcolor
from Cargar_arch import cargar
ventana_analizar = tkinter.Tk()
ventana_analizar.geometry("700x560")
ventana_analizar.configure(bg="light blue")
etiqueta = tkinter.Label(ventana_analizar, text = "ANALISIS DE CODIGO DE ENTRADA", background="light blue",font=("Comic Sans MS", 20,"bold"))
etiqueta.place(x = 75, y = 5)

text_area = tkinter.Text(ventana_analizar)
text_area.place(x = 50, y =65, width=600, height= 400)

boton_analizar = tkinter.Button(ventana_analizar, text = "Reportes", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
boton_analizar.place(x = 260, y = 470)

boton_salir = tkinter.Button(ventana_analizar, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white")
boton_salir.place(x = 635, y = 0)


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
'''
ventana_analizar.mainloop()