def suma_recursiva(lista, pi, pf):

    if pi > pf:
        return 0

    return lista[pi] + suma_recursiva(lista, pi + 1, pf)


n = int(input("Tamaño de la lista: "))
lista = []

for i in range(n):
    lista.append(int(input("Numero: ")))

pi = int(input("Ingrese PI: "))
pf = int(input("Ingrese PF: "))

resultado = suma_recursiva(lista, pi, pf)

print("Resultado:", resultado)