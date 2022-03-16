import tkinter
from turtle import bgcolor
from Cargar_arch import cargar
ventana_principal = tkinter.Tk()
ventana_principal.geometry("700x500")
ventana_principal.configure(bg="cyan")
etiqueta = tkinter.Label(ventana_principal, text = "MENU PRINCIPAL", background="cyan",font=("Comic Sans MS", 25,"bold"))
etiqueta.place(x = 200, y = 5)

boton_arch_form = tkinter.Button(ventana_principal, text = "Cargar archivo", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white" , command= lambda: opcion_elegida(1))
boton_generar_form = tkinter.Button(ventana_principal, text = "Generar Formulario", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: opcion_elegida(2))
boton_cargar_analizar = tkinter.Button(ventana_principal, text = "Cargar Analisis", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: opcion_elegida(3))
boton_reportes = tkinter.Button(ventana_principal, text = "Reportes", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
boton_arch_form.place(x = 90, y = 60)
boton_generar_form.place(x = 390, y = 60)
boton_cargar_analizar.place(x = 90, y = 300)
boton_reportes.place(x = 390, y = 300)

boton_salir = tkinter.Button(ventana_principal, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white")
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
ventana_principal.mainloop()

