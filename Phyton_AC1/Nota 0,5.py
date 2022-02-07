trabalho = float(input())
prova = float(input())

if(trabalho <=10 and trabalho >=0 and prova <= 10 and prova >= 0):
    media = (prova + trabalho)/ 2

if(media >= 6):
   print("aprovado")
elif(media < 6 and trabalho >= 2):
    print("talvez com a sub")
else:
        print("reprovado")
