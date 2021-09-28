from particulas import Particula
import json

class ListaParticulas:
    def __str__(self):
        self.__particulas = []
        
    def agregar_inicio (self, lp:Particula):
        self.__particulas.append (0,lp)
        
    def agregar_final (self, lp:Particula):
        self.__particulas.append (lp)
        
    #def mostrar (self):
     #   for e in self.particula:
      #      e.imprimir()
        
    def __str__(self) -> str:
        return "".join(
            str(particula)+"\n" for particula in self.__particulas)
        
    def __len__(self):
        return len(self.__particulas)
    
    #comienza
    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        if self.count < len(self.__particulas):
            particula = self.__particulas[self.count]
            self.count += 1
            return particula
        else:
            return StopIteration
    #termina
        
    def guardar (self,ubicacion):
        try:
            with open (ubicacion, 'w') as archivo:
                datosParticula = [particula.to_jason() for particula in self.__particulas]
                json.dump (datosParticula,archivo,indent=5)
            return True
        except:
            return False
    
    def abrir (self,ubicacion):
        try:
            with open (ubicacion, 'r') as archivo:
                datosParticula = json.load(archivo)
                self.__particulas = [Particula(**particulaJ) for particulaJ in datosParticula]
                return 1
        except:
            return 0