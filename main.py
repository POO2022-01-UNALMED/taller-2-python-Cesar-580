class Asiento:
    
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio 
        self.registro = registro

    def cambiarColor(self,color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color 
    
class Auto:
    cantidadCreados = int
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = list(asientos)
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cont = 0
        if self.asientos != None:
            for asientos_list in self.asientos:
                if asientos_list != None:
                    cont += 1
        return cont

    def verificarIntegridad(self):

        if self.registro == self.motor.registro:
            if self.registro == self.asientos[0].registro:
                return "Auto original"
            else:
                return "Las piezas no son originales"
        return "Las piezas no son originales"


class Motor:
    
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self,registro):
        self.registro = registro
    
    def asignarTipo(self,tipo):
        if tipo == "gasolina" or tipo == "electrico":
            self.tipo = tipo












