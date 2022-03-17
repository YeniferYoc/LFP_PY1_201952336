class Elemento():
    def __init__(self,tipo, valor, fondo, nombre, valores, evento):
        self.nombre = nombre
        self.valores = valores
        self.tipo = tipo
        self.valor = valor
        self.fondo = fondo
        self.evento = evento

    def dar_todo(self):
        print("TIPO --> "+self.tipo+", VALOR: "+str(self.valor)+", FONDO: "+str(self.fondo)+", NOMBRE: "+str(self.nombre)+", EVENTO "+str(self.evento))
        
        if self.valores == None: 
            pass
        else:
            print("VALORES")
            for valor in self.valores:
                print(str(valor))