def busqueda_binaria(lista, valor):
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1  # valor no encontrado

# Lista de ejemplo ordenada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 17, 19]
valor_buscado = 8
resultado = busqueda_binaria(lista, valor_buscado)

if resultado != -1:
    print("El valor", valor_buscado, "fue encontrado en la posición", resultado)
else:
    print("El valor buscado", valor_buscado, "no fue encontrado en la lista")
