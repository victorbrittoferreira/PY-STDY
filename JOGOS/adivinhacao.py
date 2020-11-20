print('**************************************************')
print('*                                                *')
print('*                 ADIVINHAÇÃO                    *')
print('*                                                *')
print('**************************************************')

#nome = input("Digite seu nome: \n")
#print("Seu nome é " +  nome )

#DECLARACOES

numero_secreto = 69
total_tentivas = 3
#rodada= 1

#while( rodada <= total_tentivas):
for rodada in range(1, total_tentivas +1):

    print('Tentativa {} de {}.'.format(rodada, total_tentivas))
    chute = int(input("Digte seu número: "))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if acertou:
        print ("Você acertou!")
        break
    #else:
    #    print (Você errou!")
    elif ( maior ):
        print("Você errou! Chutou alto demais")
    elif ( menor ):
        print("Você errou! Chutou baixo demais")

#   total_tentivas=total_tentivas -1
#   rodada = rodada +1

print('___________ G A M E   O V E R! ___________')