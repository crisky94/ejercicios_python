# d. Calificación de un estudiante
# Escribe un programa que le pida al usuario una calificación entre 0 y 100 y que determine la letra correspondiente:

# 90 a 100: "A"
# 80 a 89: "B"
# 70 a 79: "C"
# 60 a 69: "D"
# Menor a 60: "F"
# Muestra la letra correspondiente.

numero = float(input('Ingresa un número entre el 0 y 100: '))

if 90 <= numero <= 100:
    calificación = 'A'
elif 80 <= numero <= 89:
    calificación = 'B'
elif 70 <= numero <= 79:
    calificación = 'C'
elif 60 <= numero <= 69:
    calificación = 'D'
elif 60 < numero:
    calificación = 'F'
else :
    print('El numero ingresado no es válido')
    calificación = None

if calificación is not None:
    print(f'Resultado: La calificación es {calificación}')