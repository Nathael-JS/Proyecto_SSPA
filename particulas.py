from algoritmo import distancia_euclidiana
from typing import OrderedDict

class Particula:
    
    def __init__(self, id="", origen_x="", origen_y="", destino_x="", destino_y="",
    velocidad=0.0, red="",green="",blue=""):
    
        self.__id = id
        
        self.__origen_x = origen_x
        self.__destino_x = destino_x
        
        self.__origen_y = origen_y
        self.__destino_y = destino_y
        
        self.__velocidad = velocidad
        
        self.__red=red
        self.__blue=blue
        self.__green=green
        
        self.distancia = distancia_euclidiana (origen_x, origen_y, destino_x, destino_y)


    #def imprimir (self):
     #   print ("El calculo de las particulas es: ",self.distancia)
    
    def __str__(self) -> str:
        return ("La particula: "+self.__id+" tiene su punto x1 en: "+self.__origen_x+" y su x2 en:  "+self.__destino_x
                +" tiene su punto y1 en: "+self.__origen_y+" y su y2 en:  "+self.__destino_y+"y su velocida es: "+ str(self.__velocidad))
        
    def to_jason (self):
        return{
            "ID": self.__id,
            "Punto x1":self.__origen_x,
            "Punto x2":self.__destino_x,
            "Punto x1":self.__origen_y,
            "Punto x2":self.__destino_y,
            "Resultado":self.distancia,
            "Rojo":self.__red,
            "Azul":self.__blue,
            "Verde":self.__green,
            "Velocidad":self.__velocidad
        }
        
        #getters
    @property
    def id(self):
        return self.__id
        
    @property
    def origen_x(self):
        return self.__origen_x
    
    @property
    def destinno_x(self):
        return self.__destino_x
    
    @property
    def origen_y(self):
        return self.__origen_y
    
    @property
    def destino_y(self):
        return self.__destino_y
    
    @property
    def distacia(self):
        return self.distancia
    
    @property
    def red(self):
        return self.__red
    
    @property
    def blue(self):
        return self.__blue
    
    @property
    def green(self):
        return self.__green
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    #setter
    @velocidad.setter
    def velocidad(self, newVelocidad):
        if not (newVelocidad > 0):
            self.__velocidad = 0.1
        else:
            self.__velocidad = newVelocidad