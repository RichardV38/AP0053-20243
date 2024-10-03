class Square:
    def __init__(self):
        self.lectura("cuadrado")
    def getVal(self):        
        resultado = self.a * self.a
        self.imprimir("Cuadrado", resultado)
    def imprimir(self, operacion, resultado):
        print(f"De la clase Square: {operacion} {resultado}\n")
    def lectura(self, operacion):
        self.a = int(input(f"Ingrese número 'a' para {operacion}: "))

class Add_Sub:
    def add(self):
        self.operacion = "sumar"
        self.lectura(self.operacion)
        self.resultado = self.a + self.b
        return self.resultado
    def sub(self):
        self.operacion = "restar"
        self.lectura(self.operacion)
        self.resultado = self.a - self.b
        return self.resultado
    def mult(self):
        self.operacion = "multiplar"
        self.lectura(self.operacion)
        self.resultado = self.a * self.b
        return self.resultado
    def div(self):
        self.operacion = "dividir"
        self.lectura(self.operacion)
        self.resultado = self.a / self.b
        return self.resultado
    def divEntera(self):
        self.operacion = "división entera"
        self.lectura(self.operacion)
        self.resultado = self.a // self.b
        return self.resultado
    def lectura(self, operacion):
        self.a = int(input(f"Ingrese número 'a' para {operacion}: "))
        self.b = int(input(f"Ingrese número 'b' para {operacion}: "))
    def imprimir(self):
        print(f"De la clase Add_Sub: '{self.operacion}' {self.resultado}\n")
        