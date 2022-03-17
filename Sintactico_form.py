from Token import *
from Elemento import *

class Sintactico_form():
    """
   CADENA = 2
    NUMERO = 3
    LLAVE_ABRE = 4
    LLAVE_CIERRA =5
    CORCHETE_ABRE = 6
    CORCHETE_CIERRE = 7
    PUNTO_COMA = 8
    COMA = 9
    DOS_PUNTOS =10
    DESCONOCIDO = 11
    NOMBRE = 12
    GRAFICA = 13
    LETRAS = 14
    PARENTESIS_ABRE = 15
    PARENTESIS_CIERRA = 16
    INTERROGACION_ABRE = 17
    INTERROGACION_CIERRA = 18
    MAYOR_QUE = 19
    MENOR_QUE = 20
    """

    nombre_mes = ''
    año_gra = 0
    arreglo_elementos = []

    lista_tokens = []
    arreglo_lleno = []
    datos_generales = []



    def analizar(self,tokens):

        self.tokens= tokens
        longitud_arr = len(tokens)
        self.tipos = Token("lexema", -1, -1, -1)
        encabezado_encontrado = False

        #prueba = []
        #prueba = self.Buscar_elemento(TypeToken.TITULO.name)
        #print(prueba[1]) no se encotnro, argumento devuelve none si no se encontro

        #arreglo_dos_puntos = self.Buscar_elemento(TypeToken.DOS_PUNTOS.name)
        for i in range(longitud_arr):# SE RECORRE LA LONGITUD DEL ARREGLO
                if self.tokens[i].tipo == self.tipos.PALABRA_RESERVADA:
                    if self.tokens[i].lexema_valido.upper() == "FORMULARIO":
                        if self.tokens[i+1].tipo == self.tipos.CURVA:#SE VERIFICA QUE CUMPLA DETEMINDAMENTE CON CAMPO Y CON CONTENIDO
                            if self.tokens[i+2].tipo == self.tipos.MAYOR_QUE:
                                if self.tokens[i+3].tipo == self.tipos.MAYOR_QUE:
                                    encabezado_encontrado = True
                                else:
                                    print("SE ESPERABA UN >")
                            else:
                                print("SE ESPERABA UN >")
                                
                                break
                        else:#SINO SE CUMPLE ENTONCES QUE SE ROMPA EL CICLO 
                            print("SE ESPERABA ~")
                            break
                    
                    continue
        
        if encabezado_encontrado == True:
            print("CONTINUA")
            self.arreglo_elementos = self.Buscar_elemento(self.tipos.MENOR_QUE)
        
            for elemento in self.arreglo_elementos:
               #print(elemento.tipo + " -> : " + str(producto.precio_u)+" ganancia: "+str(producto.ganancia))### aqui mi quede
                elemento.dar_todo()
                print("---------------------------------------------------------------")
        else:
            print("ERROR SINTACTICO")
        #self.arreglo_productos = self.Buscar_elemento(TypeToken.CORCHETE_ABRE.name)
        
        #for producto in self.arreglo_productos:
         #   print(producto.producto + " -> precio: " + str(producto.precio_u)+" ganancia: "+str(producto.ganancia))### aqui mi quede
        

        


    def Buscar_elemento(self, tipo):
        longitud_arr = len(self.tokens)
        print(longitud_arr)
        for i in range(longitud_arr):# SE RECORRE LA LONGITUD DEL ARREGLO
                if self.tokens[i].tipo == tipo:
                    print("ENCONTRE MENOR QUE")
                    
                    arreglo_menorque = self.Buscar_pos_menorque(i,longitud_arr, self.tipos.MAYOR_QUE)
                    if arreglo_menorque[0] == True:
                        print("CONTINUA PORQUE SE ENCONTRO EL CIERRE >")
                        print(arreglo_menorque[1])
                        arreglo_tipo = self.Buscar_atributo(i,arreglo_menorque[1], "TIPO")
                        if arreglo_tipo[0] == True:
                            print("EL TIPO ES: ")
                            print(arreglo_tipo[1])
                            if arreglo_tipo[1].upper() == "ETIQUETA":
                                arreglo_at_etiqueta = self.Buscar_atributo(i,arreglo_menorque[1], "VALOR")
                                valor = arreglo_at_etiqueta[1]
                                etiqueta_nueva = Elemento("etiqueta", valor, None, None, None, None)
                                self.arreglo_elementos.append(etiqueta_nueva)

                            elif arreglo_tipo[1].upper() == "TEXTO":
                                arreglo_valor_texto = self.Buscar_atributo(i,arreglo_menorque[1], "VALOR")
                                arreglo_fondo_texto = self.Buscar_atributo(i,arreglo_menorque[1], "FONDO")
                                valor = arreglo_valor_texto[1]
                                fondo = arreglo_fondo_texto[1]
                                texto_nuevo = Elemento("texto", valor, fondo, None, None, None)
                                self.arreglo_elementos.append(texto_nuevo)

                            elif arreglo_tipo[1].upper() == "GRUPO-RADIO":

                                arreglo_nombre_radio = self.Buscar_atributo(i,arreglo_menorque[1], "NOMBRE")
                                arreglo_val = self.Buscar_valores(i,arreglo_menorque[1],"VALORES")
                                nombre = arreglo_nombre_radio[1]
                                radio_nuevo = Elemento("grupo-radio",None, None, nombre, arreglo_val, None)
                                self.arreglo_elementos.append(radio_nuevo)

                            elif arreglo_tipo[1].upper() == "GRUPO-OPTION":
                                arreglo_nombre_option = self.Buscar_atributo(i,arreglo_menorque[1], "NOMBRE")
                                arreglo_val = self.Buscar_valores(i,arreglo_menorque[1],"VALORES")
                                nombre = arreglo_nombre_option[1]
                                option_nuevo = Elemento("grupo-option",None, None, nombre, arreglo_val, None)
                                self.arreglo_elementos.append(option_nuevo)

                            elif arreglo_tipo[1].upper() == "BOTON":
                                arreglo_valor_boton = self.Buscar_atributo(i,arreglo_menorque[1], "VALOR")
                                arreglo_bton_evento = self.Buscar_atributo(i,arreglo_menorque[1], "EVENTO")
                                valor = arreglo_valor_boton[1]
                                evento = arreglo_bton_evento[1]
                                evento = evento.upper()
                                boton_nuevo = Elemento("boton", valor, None, None, None, evento)
                                self.arreglo_elementos.append(boton_nuevo)
                            
                            else:
                                print("ERROR, NO PERTENECE A NINGUN TIPO")
                        else:
                            print("NOS SE ENCONTRO TIPO")
                            break
                    else:
                        print("ERROR SINTACTICO, NO PUEDE CONTINUAR, FALTO CIERRE DE ELEMENTO")
                        break

                    
                    continue
        if len(self.arreglo_elementos) >0:
            return self.arreglo_elementos
        else: 
            return self.arreglo_elementos

    def Buscar_pos_menorque(self, inicio, fin, tipo):
            print(fin)
            salida = [False, 0]
            encontre = False
            poscion_encontre = 0

            for i in range(inicio,fin):# SE RECORRE LA LONGITUD DEL ARREGLO
                    if self.tokens[i].tipo == tipo:
                        poscion_encontre = i
                        encontre = True
                        salida[0] = True
                        salida[1] = poscion_encontre
                        break
            if encontre == True:
                return salida
            else: 
                salida[0] = False
                salida[1] = 0
                return salida

    def Buscar_atributo(self, inicio, fin,lexema):
            salida = [False, None]
            encontre = False
            for i in range(inicio,fin):# SE RECORRE LA LONGITUD DEL ARREGLO
                    if self.tokens[i].tipo == self.tipos.PALABRA_RESERVADA:
                        print("ENCONTRE RESERVADA")
                        if self.tokens[i].lexema_valido.upper() == lexema:
                            print("ENCONTRE LEXEMA")
                            if self.tokens[i+1].tipo == self.tipos.DOS_PUNTOS:
                                print("ENCONTRE DOS PUNTOS")
                                if lexema == "EVENTO":
                                    if self.tokens[i+2].tipo == self.tipos.PALABRA_RESERVADA:
                                        print("ENCONTRE PALABRA RESERVADA")
                                        encontre = True
                                        salida[0] = True
                                        salida[1] = self.tokens[i+2].lexema_valido
                                    else:
                                        print("SE ESPERABA UNA CADENA")
                                        break
                                else: 
                                    if self.tokens[i+2].tipo == self.tipos.CADENA:
                                        print("ENCONTRE CADENA")
                                        encontre = True
                                        salida[0] = True
                                        salida[1] = self.tokens[i+2].lexema_valido
                                    else:
                                        print("SE ESPERABA UNA CADENA")
                                        break

                                
                            else:
                                print("SE ESPERABAN DOS PUNTOS")
                        
                        continue
            if encontre == True:
                return salida
            else: 
                salida[0] = False
                salida[1] = None
                return salida

    def Buscar_valores(self, inicio, fin, lexema):
        arreglo_valores = []
        for i in range(inicio, fin):# SE RECORRE LA LONGITUD DEL ARREGLO
            if self.tokens[i].tipo == self.tipos.PALABRA_RESERVADA:
                print("ENCONTRE RESERVADA")
                if self.tokens[i].lexema_valido.upper() == lexema:
                    print("ENCONTRE LEXEMA")
                    if self.tokens[i+1].tipo == self.tipos.DOS_PUNTOS:
                        print("SE ENCONTRO DOS PUNTOS")
                        if self.tokens[i+2].tipo == self.tipos.CORCHETE_ABRE:
                            arreglo_valores = []
                            print("ENCONTRE CORCHETE ABRE")
                            arreglo_del_cierre = self.Buscar_pos_menorque(i,fin, self.tipos.CORCHETE_CIERRA)
                            for j in range(i+2, arreglo_del_cierre[1]): 
                                if self.tokens[j].tipo == self.tipos.CADENA:
                                    valor_nuevo = self.tokens[j].lexema_valido
                                    arreglo_valores.append(valor_nuevo)
                        else: 
                            print("SE ESPERABA CORCHETE ABRE")
                            break
                    else: 
                        print("SE ESPERABAN DOS PUNTOS")
                        break

                    
                    
                continue
        if len(arreglo_valores) >0:
            return arreglo_valores
        else: 
            return arreglo_valores

    def printTokens(self):
        
        print("ESTE ES EL ARREGLO DEL ANALIZADOR SINTACTICO")
        for token in self.arreglo_tok:
            print(token.lexema + " -> Tipo: " + str(token.type))

