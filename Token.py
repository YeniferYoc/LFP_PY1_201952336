class Token():
    lexema_valido = ''
    tipo = 0
    fila = 0
    columna = 0

    #ENUM
    PALABRA_RESERVADA = 1
    CADENA = 2
    NUMERO = 3
    CURVA = 4
    MAYOR_QUE = 5
    MENOR_QUE = 6
    CORCHETE_ABRE = 7
    CORCHETE_CIERRA = 8
    COMA = 9
    DOS_PUNTOS = 25
    DESCONOCIDO = 10
    TIPO = 11
    VALOR = 12
    FONDO = 13
    VALORES = 14
    EVENTO = 15
    ENTRADA = 16
    INFO = 17
    LETRAS = 18
   

    #Constructor de la clase
    def __init__(self,lexema,tipo,fila,columna):
        self.lexema_valido = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexema_valido

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna

    def getTipo(self):
        if self.tipo == self.PALABRA_RESERVADA:
            return 'PALABRA_RESERVADA'
        elif self.tipo == self.CADENA:
            return 'CADENA'
        elif self.tipo == self.NUMERO:
            return 'NUMERO'
        elif self.tipo == self.CURVA:
            return 'CURVA'
        elif self.tipo == self.MAYOR_QUE:
            return 'MAYOR QUE'
        elif self.tipo == self.MENOR_QUE:
            return 'MENOR QUE'
        elif self.tipo == self.CORCHETE_ABRE:
            return "CORCHETE ABRE"
        elif self.tipo == self.CORCHETE_CIERRA:
            return "CORCHETE CIERRA"
        elif self.tipo == self.COMA:
            return "COMA"
        elif self.tipo == self.DOS_PUNTOS:
            return "DOS PUNTOS"
        elif self.tipo == self.DESCONOCIDO:
            return "DESCONOCIDO"
        elif self.tipo == self.TIPO:
            return 'TIPO'
        elif self.tipo == self.VALOR:
            return 'VALOR'
        elif self.tipo == self.FONDO:
            return "FONDO"
        elif self.tipo == self.VALORES:
            return "VALORES"
        elif self.tipo == self.EVENTO:
            return "EVENTO"
        elif self.tipo == self.ENTRADA:
            return "ENTRADA"
        elif self.tipo == self.INFO:
            return "INFO"