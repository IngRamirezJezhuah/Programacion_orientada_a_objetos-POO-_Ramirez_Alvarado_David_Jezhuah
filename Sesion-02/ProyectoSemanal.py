print("---------------------------------------------")
print("|    Calculador de Areas                     |")
print("| las figuras disponibles son                |")
print("|  circulo  -  cuadrado  - triangulo         |")
print("|--------------------------------------------")
print("|  Ingrese el area a resolver  ⸜(｡˃ ᵕ ˂ )⸝♡  |")
print("---------------------------------------------")

Figura = input("|figura: ")

def Circulo():
    if Figura == "circulo":
        radio = float(input("ingrese el radio del circulo: "))
        pi = 3.1416
        radioCuadrado = radio * radio
        areaCirculo = pi * radioCuadrado
        return areaCirculo

def Cuadrado():
    if Figura == "cuadrado":
        lado = float(input("Ingrese tamaño del lado: "))
        areaCuadrado = lado * lado
        return areaCuadrado

def Triangulo():
    if Figura == "triangulo":
        base = float(input("Ingrese el tamaño de su base: "))
        altura = float(input("Ingrese el tamaño de su altura: "))
        areaTriangulo = base * altura / 2
        return areaTriangulo

def calcularAreas():
    print("|--------------------------------------------")
    if Figura == "circulo":
        print("/ᐠ - ˕ -マ",f"El área del círculo es:",Circulo())
        print("|--------------------------------------------")
    elif Figura == "cuadrado":
        print("/ᐠ - ˕ -マ",f"El área del cuadrado es:",Cuadrado())
        print("|--------------------------------------------")
    elif Figura == "triangulo":
        print("/ᐠ - ˕ -マ",f"El área del triángulo es:",Triangulo())
        print("|--------------------------------------------")
    else:
        print(" ")
        print("Lo siento, la figura ingresada no es válida. Intenta de nuevo. \(^o^)/")
        print("|--------------------------------------------")
        

calcularAreas()
print(" ")
print("Eso es todo hehehe ദ്ദി（• ˕ •マ.ᐟ")
print(" ")