def suma_recursiva(lista, pi, pf):

    if pi > pf:
        return 0
    
        return lista[pi] + suma_recursiva(lista, pi + 1, pf)
lista = [2, 4, 6, 3]

pi = int(input("Ingrese PI: "))
pf = int(input("Ingrese PF: "))