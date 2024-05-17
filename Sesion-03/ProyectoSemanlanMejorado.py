class FiguraGeometricas():

    ubicacion_x = 0
    ubicacion_y = 0

    def __init__(self):
        None
    def get_area(self):
        return 999999999.9
    def modificar_x(self,x):
        self.ubicacion_x = x
    def modificar_y(self,y):
        self.ubicacion_y = y

class Rectangulo(FiguraGeometricas):
    alto = 0.0
    base = 0.0
    #esta funciones estan divididas dentro de la propia clase para que furule se tiene que llamar 
    #para buena practica es mejor usar la llamada self
    def __init__(self,alto,base): #variables de clase
        self.alto = float(alto) #llama a contenido dentro de la clase
        self.base = float(base)

#    def Dibujafigura():

    def __str__(self):
        return "Es un rectangulo, con area: " + str(self.get_area())
    
    def get_area(self):  #variables de clase
        return self.alto * self.base
    
class Circulo(FiguraGeometricas):
    None #tarea

class Triangulo(FiguraGeometricas):
    None #tarea

#tarea implementar Circulo & trinagulo
#Refactor Proyecto Semanal 01
#dinujar figura a travez del metodo dibujarFigura
#aqui empieza nuestro codigo
import turtle 
t = turtle.turtle
t.foward(100)
t.mainloop()

prueba = Rectangulo(2,2)
print(str(prueba.get_area()))

#el termino self es un metodo para que me llame a si mismo 
#metodo get y self son necesarios para evitar modificaciones a distincion entre