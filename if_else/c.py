# c. Cálculo de aumento de precio según la categoría del producto
# Pide al usuario ingresar el precio de un producto y la categoría a la que pertenece:

# "A": aplica un aumento del 20%
# "B": aplica un aumento del 10%
# "C": aplica un aumento del 5%
# Si la categoría ingresada no es válida, muestra un mensaje de error. Calcula el precio final con el aumento y muestra el resultado.

precio = float(input('Ingresa el precio del producto: '))
categoria = input('Ingresa si la categoria es "A", "B" o "C":').upper()

if categoria == 'A':
  resultado = precio * 1.20
elif categoria == 'B':
   resultado = precio * 1.10
elif categoria == 'C':
    resultado =  precio * 1.05
else:
    print('La categoria indicada no es valida')
    resultado = None 

if resultado is not None:
    print(f'El precio final con aumento es: {resultado}')