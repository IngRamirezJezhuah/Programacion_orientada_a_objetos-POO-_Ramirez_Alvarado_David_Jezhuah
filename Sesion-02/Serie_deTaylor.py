import math
acumulador = 0.0
contador = 0
division_actual =1.0
suma= True

while division_actual > 0.0099:
    contador += 1
    division_actual = 1/contador

    if contador % 2 != 0:
        acumulador+=1/contador
        if suma:
            acumulador += division_actual
        else:
            acumulador -= division_actual
        suma = not suma

print("pi es igual a:", acumulador)