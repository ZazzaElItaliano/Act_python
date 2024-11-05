"""
5. Palíndromo con while
Escribe un programa que verifique si una palabra es un palíndromo utilizando un bucle
while.
"""
palabra=input("Dime una palabrita")
palabra = palabra.lower().replace(" ", "")
izquierda=0
derecha=len(palabra)-1
palabra_comprobada=True

while(izquierda<derecha):
        if(palabra[izquierda]!= palabra[derecha]):
            palabra_comprobada=False
            break
        izquierda+=1
        derecha-=1
        
if(palabra_comprobada):
    print("Es palíndromo")
else:
    print("No es palíndroma")

