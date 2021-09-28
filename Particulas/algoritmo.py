import math

def distancia_euclidiana(x_1,y_1,x_2,y_2):
    
    distancia = math.sqrt(sum([(origen_x - destino_x & origen_y - destino_y)**2
                               for origen_x, destino_x, origen_y, destino_y
                               in zip(x_1, x_2, y_1, y_2)]))

    return distancia;

#x_1 = (2,3,5)
#x_2 = (7,9,11)
#y_1 = (1,4,6)
#y_2 = (8,10,12)

#resultado = distancia_euclidiana(x_1, x_2, y_1, y_2)

#print (resultado)