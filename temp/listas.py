lista1 = [2,3,4,5,6]
print(lista1)

lista1.append(7)
print(lista1)
num = 8 
lista1.extend([num])
print(lista1)
lista1.pop(3)
print(lista1)
lista1.reverse()
print(lista1)
lista1.insert(3,13)
print(lista1)
lista1.remove(13)
print(lista1)
lista1.sort()
print(lista1)

lista2D = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(lista2D)

lista2_2D = [[1,2,3,"a"],[5,6,7],[9,10,"e",12,"cat"],["beta",14,15,16]]
print(lista2_2D)

subLista = [["p","q"],["r","s"]]
lista2D_subLista = [[1,2,3,"a"],[5,6,7,"cat"],[9,10,"e",12],["beta",14,15,subLista]]
print(lista2D_subLista)

subLista2 = [["p","q"],["r","s"]]
lista3 = [[1,2,3,"a"],[5,6,7,"cat"],[9,10,"e",12],["beta",14,15,subLista2]]
print(lista3)
subLista2[0][1] = "z"
print(lista3)

tupla1 = ("0","a","hola", 4.5, 3)
print(tupla1)
print(tupla1[1])
print(tupla1[1:3])
print(tupla1.count(3)) 
print(tupla1.index(4.5))

diccionario1 = {"Nombre":"Richard", "Apellido":"Velasquez", "Edad":18}
print(diccionario1)
print(diccionario1["Nombre"])
diccionario1["Año"] = 2006
print(diccionario1)
diccionario1["Nombre"] = "Alejandro"
print(diccionario1)

diccionario2 = {"Richard":"Nombre", "Velasquez":"Apellido", 18:"Edad"}

print(diccionario1.keys())
print(diccionario1.values())
diccionario1.clear()
print(diccionario1)
diccionario1.update(diccionario2)
print(diccionario1)
diccionario1.pop("Richard")
print(diccionario1)