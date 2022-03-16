import tkinter
from turtle import bgcolor
from Cargar_arch import cargar
from Lexico_Contenido import Analizador_Lexico
from Sintactico_form import *
#import ventana_analizar
#from  ventana_reportes import *
class Todo():
    
    def __init__(self):
        self.contenido = ""
        self.lexico_conte = None
        ventana_principal = tkinter.Tk()
        ventana_principal.geometry("700x500")
        ventana_principal.configure(bg="cyan")
        etiqueta = tkinter.Label(ventana_principal, text = "MENU PRINCIPAL", background="cyan",font=("Comic Sans MS", 25,"bold"))
        etiqueta.place(x = 200, y = 5)
        
        boton_arch_form = tkinter.Button(ventana_principal, text = "Cargar archivo", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white" , command= lambda: self.opcion_elegida(1) )
        boton_generar_form = tkinter.Button(ventana_principal, text = "Generar Formulario", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: self.opcion_elegida(2))
        boton_cargar_analizar = tkinter.Button(ventana_principal, text = "Cargar Analisis", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: self.opcion_elegida(3))
        boton_reportes = tkinter.Button(ventana_principal, text = "Reportes", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: self.opcion_elegida(4))
        boton_arch_form.place(x = 90, y = 60)
        boton_generar_form.place(x = 390, y = 60)
        boton_cargar_analizar.place(x = 90, y = 300)
        boton_reportes.place(x = 390, y = 300)

        boton_salir = tkinter.Button(ventana_principal, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white")
        boton_salir.place(x = 635, y = 0)
        ventana_principal.mainloop()

    def opcion_elegida(self,opcion):
        if(opcion == 1):
            print("AQUI SE SELECCIONA EL ARCHIVO .FORM ")
            self.contenido = cargar()
            print(self.contenido)

        if(opcion == 2):
            print("AQUI SE GENERA EL FORMULARIO ")
        #lexico_conte = Analizador_Lexico(contenido)
            print(self.contenido)
            self.lexico_conte = Analizador_Lexico(self.contenido)
            self.lexico_conte.Imprimir()
            self.lexico_conte.ImprimirErrores()
            sintactico_form = self.lexico_conte.tokens
            Sintactico_form(sintactico_form)
            
        
        if(opcion == 3):
            print("AQUI SE SELECCIONA EL ARCHIVO .FORM ")
            contenido_data = cargar()
            print(contenido_data)

        if(opcion == 4):
            print("AQUI REPORTES")
            ventana_reportes = tkinter.Toplevel()
            ventana_reportes.geometry("500x400")
            ventana_reportes.configure(bg="light blue")
            etiqueta = tkinter.Label(ventana_reportes, text = "REPORTES", background="light blue",font=("Comic Sans MS", 20,"bold"))
            etiqueta.place(x = 175, y = 5)


            #boton_tokens = tkinter.Button(ventana_reportes, text = "Reporte de Tokens", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
            #boton_errores = tkinter.Button(ventana_reportes, text = "Reporte Errores", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
            #boton_usuario = tkinter.Button(ventana_reportes, text = "Manual de Usuario", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
            #boton_tecnico = tkinter.Button(ventana_reportes, text = "Manual Tecnico", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
            #boton_tokens.place(x = 30, y = 60)
            #boton_errores.place(x = 275, y = 60)
            #boton_usuario.place(x = 30, y = 250)
            #boton_tecnico.place(x = 275, y = 250)



            boton_salir = tkinter.Button(ventana_reportes, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white")
            boton_salir.place(x = 435, y = 0)
'''
def interfaz ():
    ventana_principal = tkinter.Tk()
    ventana_principal.geometry("700x500")
    ventana_principal.configure(bg="cyan")
    etiqueta = tkinter.Label(ventana_principal, text = "MENU PRINCIPAL", background="cyan",font=("Comic Sans MS", 25,"bold"))
    etiqueta.place(x = 200, y = 5)
    op=0
    print(op)
    boton_arch_form = tkinter.Button(ventana_principal, text = "Cargar archivo", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white" , command= lambda: opcion_elegida(1) )
    boton_generar_form = tkinter.Button(ventana_principal, text = "Generar Formulario", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: opcion_elegida(2))
    boton_cargar_analizar = tkinter.Button(ventana_principal, text = "Cargar Analisis", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: opcion_elegida(3))
    boton_reportes = tkinter.Button(ventana_principal, text = "Reportes", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: opcion_elegida(4))
    boton_arch_form.place(x = 90, y = 60)
    boton_generar_form.place(x = 390, y = 60)
    boton_cargar_analizar.place(x = 90, y = 300)
    boton_reportes.place(x = 390, y = 300)

    boton_salir = tkinter.Button(ventana_principal, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white")
    boton_salir.place(x = 635, y = 0)
    ventana_principal.mainloop()
    print(str(op)+"ddd")
    '''
#---------------------------------------------------------------------------------------------------------


#FUNCIONES


        
def almacena(conte):
    return conte

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2 
   app = Todo()

if __name__ == "__main__":
    main()

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


