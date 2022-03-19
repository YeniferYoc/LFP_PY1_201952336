import tkinter
from turtle import bgcolor
from Cargar_arch import cargar
from Lexico_Contenido import Analizador_Lexico
from Sintactico_form import *
from tkinter import Tk, messagebox as mb
from tkinter.simpledialog import *
from os import startfile
#import ventana_analizar
#from  ventana_reportes import *
class Todo():
    
    def __init__(self):
        self.contenido = ""
        self.lexico_conte = Analizador_Lexico()
        self.sintactico_cont = Sintactico_form()
        self.elementos = None
        self.nombre_rep = ""
        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.geometry("700x500")
        self.ventana_principal.configure(bg="cyan")
        etiqueta = tkinter.Label(self.ventana_principal, text = "MENU PRINCIPAL", background="cyan",font=("Comic Sans MS", 25,"bold"))
        etiqueta.place(x = 200, y = 5)
        
        boton_arch_form = tkinter.Button(self.ventana_principal, text = "Cargar archivo", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white" , command= lambda: self.opcion_elegida(1) )
        boton_generar_form = tkinter.Button(self.ventana_principal, text = "Generar Formulario", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: self.opcion_elegida(2))
        boton_cargar_analizar = tkinter.Button(self.ventana_principal, text = "Cargar Analisis", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: self.opcion_elegida(3))
        boton_reportes = tkinter.Button(self.ventana_principal, text = "Reportes", font=("Comic Sans MS", 15,"bold"), width=17, height=5, background=  "gray",fg="white",command= lambda: self.opcion_elegida(4))
        boton_arch_form.place(x = 90, y = 60)
        boton_generar_form.place(x = 390, y = 60)
        boton_cargar_analizar.place(x = 90, y = 300)
        boton_reportes.place(x = 390, y = 300)

        boton_salir = tkinter.Button(self.ventana_principal, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white", command=lambda: self.destruir_ventana(self.ventana_principal))
        boton_salir.place(x = 635, y = 0)
        self.ventana_principal.mainloop()

    def opcion_elegida(self,opcion):
        if(opcion == 1):
            #SI SELECCIONAN OTRO ARCHIVO, SE LIMPIAN LOS CAMPOS
            self.contenido = ""
            self.lexico_conte.tokens = []
            self.lexico_conte.tokens_errorres = []
            self.sintactico_cont.arreglo_elementos = []
            print(len(self.contenido))
            print(len(self.lexico_conte.tokens))
            print(len(self.lexico_conte.tokens_errorres))
            print(len(self.sintactico_cont.arreglo_elementos))
            print("AQUI SE SELECCIONA EL ARCHIVO .FORM ")
            self.contenido = cargar()
            print(self.contenido)

        if(opcion == 2):
            print("AQUI SE GENERA EL FORMULARIO ")
        #lexico_conte = Analizador_Lexico(contenido)
            print(self.contenido)
            self.lexico_conte.analisis(self.contenido)
            #self.lexico_conte.Imprimir()
            #self.lexico_conte.ImprimirErrores()
            if len(self.lexico_conte.tokens_errorres)>0:
                mb.showerror("ERROR", "Se encontro uno o mas errores en el archivo de entrada, para mas informacion consulte reportes de errores")
            else:
                print("si se puede seguir")
                sintactico_form = self.lexico_conte.tokens
                self.sintactico_cont.analizar(sintactico_form)
                self.elementos = self.sintactico_cont.arreglo_elementos
                for elemento in self.elementos:
                    elemento.dar_todo()
                    print("---------------------------------------------------------------")
                if len(self.elementos)>0:
                    self.generar()
                                      
        if(opcion == 3):
            print("AQUI SE ANALIZA")
            self.lexico_conte.tokens = []
            self.lexico_conte.tokens_errorres = []
            self.sintactico_cont.arreglo_elementos = []
            print(len(self.lexico_conte.tokens))
            print(len(self.lexico_conte.tokens_errorres))
            print(len(self.sintactico_cont.arreglo_elementos))

            self.ventana_analizar = tkinter.Toplevel(self.ventana_principal)
            self.ventana_analizar.geometry("700x560")
            self.ventana_analizar.configure(bg="light blue")
            etiqueta = tkinter.Label(self.ventana_analizar, text = "ANALISIS DE CODIGO DE ENTRADA", background="light blue",font=("Comic Sans MS", 20,"bold"))
            etiqueta.place(x = 75, y = 5)

            self.text_area = tkinter.Text(self.ventana_analizar)
            self.text_area.place(x = 50, y =65, width=600, height= 400)
            self.text_area.insert(tkinter.END,self.contenido )

            boton_analizar = tkinter.Button(self.ventana_analizar, text = "ANALIZAR", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= self.recuperar_texto)
            boton_analizar.place(x = 260, y = 470)

            boton_salir = tkinter.Button(self.ventana_analizar, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white",command= lambda: self.destruir_ventana(self.ventana_analizar))
            boton_salir.place(x = 635, y = 0)        

        if(opcion == 4):
            print("AQUI REPORTES")
            self.ventana_reportes = tkinter.Toplevel(self.ventana_principal)
            self.ventana_reportes.geometry("500x400")
            self.ventana_reportes.configure(bg="light blue")
            etiqueta = tkinter.Label(self.ventana_reportes, text = "REPORTES", background="light blue",font=("Comic Sans MS", 20,"bold"))
            etiqueta.place(x = 175, y = 5)


            boton_tokens = tkinter.Button(self.ventana_reportes, text = "Reporte de Tokens", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: self.opciones_reporte(1))
            boton_errores = tkinter.Button(self.ventana_reportes, text = "Reporte Errores", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: self.opciones_reporte(2))
            boton_usuario = tkinter.Button(self.ventana_reportes, text = "Manual de Usuario", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: self.opciones_reporte(3))
            boton_tecnico = tkinter.Button(self.ventana_reportes, text = "Manual Tecnico", font=("Comic Sans MS", 15,"bold"), width=15, height=2, background=  "gray",fg="white",command= lambda: self.opciones_reporte(4))
            boton_tokens.place(x = 30, y = 60)
            boton_errores.place(x = 275, y = 60)
            boton_usuario.place(x = 30, y = 250)
            boton_tecnico.place(x = 275, y = 250)



            boton_salir = tkinter.Button(self.ventana_reportes, text = "Salir", font=("Comic Sans MS", 15,"bold"), background=  "red",fg="white", command=lambda: self.destruir_ventana(self.ventana_reportes))
            boton_salir.place(x = 435, y = 0)
            self.ventana_reportes.mainloop()
  
    def generar_form(self, elementos, nombre):
        nombre = nombre+".html"
        file = open(nombre, "w")
        file.write("<!doctype html>")
        file.write("<html lang=\"en\">")
        file.write("<head>")
        file.write("<meta charset=\"utf-8\">")
        file.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
        file.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU\" crossorigin=\"anonymous\">")
        file.write(" <title>YENIFER YOC</title>")
        file.write(" <script>function form_mio(valor) {")
        file.write("if (valor == 1) { document.getElementById(\"formulario\").style.display = \"\"; }")
        file.write("else { document.getElementById(\"formulario\").style.display = \"none\"; }")
        file.write(" }")
        file.write("</script>")
        file.write("")

        file.write(" </head>")
        file.write("<body bgcolor=\"#0E0440\">")
        file.write("<div style=\"height: 100%;\">")
        file.write("<nav class=\"navbar navbar-expand-md navbar-dark bg-dark\" style=\"height: 9vh;\">")
        file.write("<div class=\"container-fluid\">")
        file.write("<div class=\"mx-auto order-0\">")
        file.write("<a class=\"navbar-brand mx-auto\"> OPCIONES</a>")
        file.write("</div>")
        file.write("<div class=\"navbar-collapse collapse w-100 order-3 dual-collapse2\">")
        file.write(" <ul class=\"navbar-nav ms-auto\">")
        file.write("<li class=\"nav-item\">")
        file.write("<button type=\"button\" class=\"btn btn-dark\" style = \"height: 7vh;\" onclick = \"form_mio(1)\">MOSTRAR</button>")
        file.write("</li>")
        file.write("</ul>")
        file.write("</div>")
        file.write("</div>")
        file.write("</nav>")
        file.write("<font color=#0E0440></font><img src=\"imagenes/usac.png\" width=\"200\" height=\"200\" align=center>")
        file.write("<link rel=\"stylesheet\" href=\"css/estilo-carrusel.css\">")
        file.write("<font color=#FDFEFE>SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS</font> ")
        file.write("<font size=\"24\" color=#0E0440>FORMULARIO </font>")
        file.write("<font type=\"Gill Sans Ultra Bold\"size=\"24\" color=#FFFFFF><b>IPC 1 A</b>")
        file.write("</font>")
        file.write("<link rel=\"stylesheet\" href=\"css/estilo-carrusel.css\">")
        file.write("<font color=#FDFEFE>SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS</font> <font size=\"24\" color=#0E0440>LFPA</font><font type=\"Gill Sans Ultra Bold\"size=\"24\" color=#FFFFFF><b>lfp 1 A</b></font>")
        file.write("<div class=\"content-all\">")
        file.write("<div class=\"content-carrousel\">")
        file.write(" <figure><img src=\"imagenes/1.jpg\"></figure>")
        file.write("<figure><img src=\"imagenes/2.png\"></figure>")
        file.write("<figure><img src=\"imagenes/3.jpg\"></figure>")
        file.write("<figure><img src=\"imagenes/4.jpg\"></figure>")
        file.write("<figure><img src=\"imagenes/5.png\"></figure>")
        file.write("<figure><img src=\"imagenes/6.jpg\"></figure>")
        file.write("<figure><img src=\"imagenes/7.jpg\"></figure>")
        file.write("<figure><img src=\"imagenes/8.jpg\"></figure>")
        file.write("<figure><img src=\"imagenes/9.jpg\"></figure>")
        file.write("<figure><img src=\"imagenes/10.jpg\"></figure>")
        file.write("</div>")
        file.write("</div>")
        file.write(" <br>")
        file.write(" <br>")
        file.write(" <br>")
        file.write(" <br>")
        file.write("<img src=\"imagenes/logo.png\" width=\"200\" height=\"200\" align=right>")
        file.write(" <div class = \"d-flex align-items-center justify-content-md-center\" style=\"height: 93vh;\" >")
        file.write("<div id = \"formulario\" class = \"card border\" style = \"display: none; width: 40vw;\">")
        file.write("<div class=\"card-body\">")

        for elemento in elementos:
            file.write("<div class=\"input-group mb-3\">")
            if elemento.tipo == "etiqueta":#ETIQUETAS
                file.write("<p>"+elemento.valor+"</p>")

            elif elemento.tipo == "texto":#TEXTO
                file.write("<input id = \""+elemento.valor+"\" type=\"text\" class=\"form-control\" placeholder=\""+elemento.fondo+"\" aria-label=\"Username\" aria-describedby=\"basic-addon1\">")
            
            elif elemento.tipo == "grupo-radio":#GRUPO RADIO
                file.write("<p>"+elemento.nombre+"</p>&nbsp&nbsp&nbsp")
                file.write("<br>")
                file.write("<br>")
                file.write("<form name = \""+elemento.nombre+"\">")
                for valor in elemento.valores:
                    file.write("<input type = \"radio\" id= \""+valor+"\" name = \"Grupo\">"+valor)
                    file.write("<br>")
                file.write("</form>")

            elif elemento.tipo == "grupo-option":#GRUPO OPTION
                file.write("<p>"+elemento.nombre+"</p>&nbsp&nbsp&nbsp")
                file.write("<br>")
                file.write("<br>")
                file.write("<select id=\""+elemento.nombre+"\">")
                for valor in elemento.valores:
                    file.write("<option value=\""+valor+"\">"+valor+"</option> ")
                file.write("</select>")

            elif elemento.tipo == "boton":#BOTON
                if elemento.evento == "INFO":
                    file.write("<button type=\"button\" class=\"btn btn-secondary\" onclick=\"info()\" >"+elemento.valor+"</button>")
                elif elemento.evento == "ENTRADA":
                    file.write("<button type=\"button\" class=\"btn btn-secondary\" onclick=\"entrada()\" >"+elemento.valor+"</button>")
  
            file.write("</div>")
       
        file.write("</div>")
        file.write("<div id = \"info\" class = \"card border\" style = \"display: none; width: 40vw;\">")
        file.write("<div class=\"card-body\">")
        file.write(" <h4 >"+self.contenido+"</h4>")
        file.write(" </div>")

        file.write(" <script >")
        file.write("async function info(){")
        file.write("document.getElementById(\"info\").style.display = \"\"; }")
        file.write(" async function entrada(){")
        file.write("let cadena = \"LOS DATOS INGRESADOS FUERON LOS SIGUIENTES: <br>\";")
        
        for elemento in elementos:
            
            if elemento.tipo == "texto":#TEXTO
                file.write("cadena += document.getElementById(\""+elemento.valor+"\").value;")
                file.write("cadena+=\"<br>\";")
            
            elif elemento.tipo == "grupo-radio":#GRUPO RADIO
                file.write("var i ;")
                file.write("for (i = 0; i < document."+elemento.nombre+".Grupo.length; i++){ ")
                file.write("if (document."+elemento.nombre+".Grupo[i].checked) {")
                file.write("cadena += document."+elemento.nombre+".Grupo[i].id;")
                file.write(" }")
                file.write("} ")
                file.write("cadena+=\"<br>\";")

                
            elif elemento.tipo == "grupo-option":#GRUPO OPTION
                file.write("var d = document.getElementById(\""+elemento.nombre+"\");")
                file.write("var displaytext = d.options[d.selectedIndex].text;")
                file.write("cadena += displaytext;")
                file.write("cadena+=\"<br>\";")
                file.write("")
                file.write("")
                file.write("")

                
        
        file.write("document.body.innerHTML = \"<h2>\" +cadena+\"</h2>\";")

            


                
        file.write("}")
        file.write("</script>")
        
        
        
        

        #file.write("<script src = \"./index_mio.js\"></script>")
        file.write(" <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ\" crossorigin=\"anonymous\"></script>")
 
        

        file.write("</BODY>\r\n"+ "</HTML>");			
        file.close()
        startfile(nombre)
        print("")
        print("SE HA CREADO EL REPORTE CON EXITO")
        print("")

    def extraer_texto(self):
        entrada = self.caja_texto.get()
        self.caja_texto.delete(0, tkinter.END)
        self.generar_form(self.elementos, entrada)
        self.ventana_dialog.destroy()

    def recuperar_texto(self):
        self.contenido = self.text_area.get("1.0","end")
        self.text_area.delete("1.0","end")
        self.ventana_analizar.destroy()

        print(self.contenido)
        self.lexico_conte.analisis(self.contenido)
        self.lexico_conte.Imprimir()
        self.lexico_conte.ImprimirErrores()
        if len(self.lexico_conte.tokens_errorres)>0:
            mb.showerror("ERROR", "Se encontro uno o mas errores en el archivo de entrada, para mas informacion consulte reportes de errores")
        else:
            print("si se puede seguir")
            sintactico_form = self.lexico_conte.tokens
            self.sintactico_cont.analizar(sintactico_form)
            self.elementos = self.sintactico_cont.arreglo_elementos
            for elemento in self.elementos:
                elemento.dar_todo()
                print("---------------------------------------------------------------")
            if len(self.elementos)>0:
                self.generar()
    
    def destruir_ventana(self, ventana):
        ventana.destroy()
    
    def generar(self):
                    self.ventana_dialog = tkinter.Toplevel(self.ventana_principal)
                    self.ventana_dialog.geometry("300x150")
                    self.ventana_dialog.configure(bg="light blue")
                    etiqueta = tkinter.Label(self.ventana_dialog, text = "NOMBRE DEL ARCHIVO HTML", background="light blue",font=("Comic Sans MS", 10,"bold"))
                    etiqueta.place(x = 40, y = 5)
                    self.caja_texto = tkinter.Entry(self.ventana_dialog, font=("Comic Sans MS", 15,"bold"))
                    self.caja_texto.place(x = 25, y = 40)
                    boton1 = tkinter.Button(self.ventana_dialog, text= "Aceptar",width=10, height=3, command = self.extraer_texto)
                    boton1.place(x = 120, y = 80)

    def opciones_reporte(self, opcion):
        if(opcion == 1):
            print("REPORTE DE TOKENS")
            self.ventana_dialog2 = tkinter.Toplevel(self.ventana_reportes)
            self.ventana_dialog2.geometry("300x150")
            self.ventana_dialog2.configure(bg="light blue")
            etiqueta = tkinter.Label(self.ventana_dialog2, text = "NOMBRE DEL ARCHIVO HTML", background="light blue",font=("Comic Sans MS", 10,"bold"))
            etiqueta.place(x = 40, y = 5)
            self.caja_texto2 = tkinter.Entry(self.ventana_dialog2, font=("Comic Sans MS", 15,"bold"))
            self.caja_texto2.place(x = 25, y = 40)
            boton1 = tkinter.Button(self.ventana_dialog2, text= "Aceptar",width=10, height=3, command = self.extraer_nom_rep)
            boton1.place(x = 120, y = 80) 
            
            
        if(opcion == 2):
            print("REPORTE DE ERRORES")
            self.ventana_dialog23 = tkinter.Toplevel(self.ventana_reportes)
            self.ventana_dialog23.geometry("300x150")
            self.ventana_dialog23.configure(bg="light blue")
            etiqueta = tkinter.Label(self.ventana_dialog23, text = "NOMBRE DEL ARCHIVO HTML", background="light blue",font=("Comic Sans MS", 10,"bold"))
            etiqueta.place(x = 40, y = 5)
            self.caja_texto23 = tkinter.Entry(self.ventana_dialog23, font=("Comic Sans MS", 15,"bold"))
            self.caja_texto23.place(x = 25, y = 40)
            boton1 = tkinter.Button(self.ventana_dialog23, text= "Aceptar",width=10, height=3, command = self.extraer_nom_rep_errores)
            boton1.place(x = 120, y = 80) 
            
        if(opcion == 3):
            print("MANUAL DE USUARIO")
            startfile("[LFPA]_MANUAL_USUARIO_201952336.pdf")

        if(opcion == 4):
            print("MANUAL TECNICO")
            startfile("[LFPA]_MANUAL_TECNICO_201952336.pdf")

    def reporte_tokens(self, nombre, tokens, titulo):
        nombre = nombre + ".html"
        file = open(nombre, "w")
        file.write("<HTML>")
        file.write("<HEAD><TITLE>REPORTE TOKENS</TITLE>")
        file.write("<link rel=\"stylesheet\"  href=\"estilos.css\">")
        file.write("</head>")
        file.write("<body>")
        file.write("<CENTER><H1><b>------------------------------- REPORTE DE &nbsp &nbsp"+titulo+" -------------------------------</b></H1>")
        file.write("</CENTER>")
        file.write("<img src=\"2d.gif\" width=\"300\" height=\"200\" align=right>")
        file.write("<form action=\"\"> ")
        file.write("<p><b>&nbsp &nbsp &nbsp &nbsp &nbsp &nbspYENIFER ESTER YOC LARIOS &nbsp &nbsp -------->&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 201952336 </b></p>")
        file.write("<br>")
        file.write("<div  id = \"main-container\" >")
        file.write("<b>")
        file.write("<table>")
        file.write("<thead>")
        file.write("<tr>")
        file.write("<th> TOKEN   </th><th>LEXEMA</th><th>FILA</th><th>COLUMNA</th>")
        file.write("</tr>")
        file.write("</thead>")
                
        for token in tokens:
                    file.write("<tr><font size = 12 color = \"white\" >")
                    file.write("<td> "+str(token.getTipo())+"</td><td>"+str(token.lexema_valido)+"</td><td>"+str(token.fila)+"</td><td>"+str(token.columna)+"</td>")
                    file.write("<font size = 12></tr>")
                
        file.write("</b>")
        file.write("</table>")
        file.write("</div>")
        file.write("</BODY>\r\n"+ "</HTML>");			
        file.close()
        startfile(nombre)
        print("")
        print("SE HA CREADO EL REPORTE CON EXITO")
        print("")   
           
    def extraer_nom_rep (self):
        nombre_rep = self.caja_texto2.get()
        self.caja_texto2.delete(0, tkinter.END)
        self.ventana_dialog2.destroy()
        tokens_rep = self.lexico_conte.tokens_bien
        self.reporte_tokens(nombre_rep, tokens_rep, "TOKENS")
    
    def extraer_nom_rep_errores (self):
        nombre_rep_e = self.caja_texto23.get()
        self.caja_texto23.delete(0, tkinter.END)
        self.ventana_dialog23.destroy()
        tokens_rep_e = self.lexico_conte.tokens_errorres
        self.reporte_tokens(nombre_rep_e, tokens_rep_e, "ERRORES")
        

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
#ultimo