class FiguraGeometrica:
    def __init__(self):
        print("---------------------------------------------")
        print("|    Calculador de Áreas                     |")
        print("| Las figuras disponibles son                |")
        print("|  círculo  -  cuadrado  - triángulo         |")
        print("|--------------------------------------------")
        print("|  Ingrese el área a resolver  ⸜(｡˃ ᵕ ˂ )⸝♡  |")
        print("---------------------------------------------")
    
    def solicitar_figura(self):
        while True:
            figura = input("| Figura: ").lower()
            if figura == "triangulo":
                self.Triangulo()
                break
            elif figura == "cuadrado":
                self.Cuadrado()
                break
            elif figura == "circulo":
                self.Circulo()
                break
            else:
                print("Figura no reconocida, por favor intente de nuevo.")

class Triangulo:
    def __init__(self):
        base = float(input("Dame una base: "))
        altura = float(input("Dame la altura: "))
        area = base * altura / 2
        print("Tu área es igual a:", area)

class Cuadrado:
    def __init__(self):
        lado = float(input("Dame el lado del cuadrado: "))
        area = lado * lado
        print("Tu área es igual a:", area)

class Circulo:
    def __init__(self):
        radio = float(input("Dame el radio del círculo: "))
        pi = 3.1416
        area = pi * (radio ** 2)
        print("Tu área es igual a:", area)

figura_geometrica = FiguraGeometrica()
figura_geometrica.solicitar_figura()
