numero = int(input())
div = numero % 2

if(div == 0):
    print(numero -1, numero + 2)
else:
    if(div == 1):
        print(numero -2, numero +1)
