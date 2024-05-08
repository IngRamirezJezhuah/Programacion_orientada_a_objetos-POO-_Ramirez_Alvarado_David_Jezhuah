import math
divisiones = 10000
base = 1 / divisiones

cuarto_de_area = 0.0

acumulador = 0

for i in range(divisiones):
    acumulador += 1
    base_triangulo = float(acumulador)/float(divisiones)
    altura = math.sqrt(1-base_triangulo*base_triangulo)
    base = 1/float(divisiones)
    cuarto_de_area += base*altura

print("El cuarto de area es igual:",cuarto_de_area)
pi = cuarto_de_area * 4
print("pi es igual a ", pi)