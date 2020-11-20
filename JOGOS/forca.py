
print('**************************')
print('*              _______   *')
print('*              |     |   *') 
print('*  F O R C A   |    _O_  *')
print('*              |     |   *')
print('*              |     /\  *')
print('**************************')

import random

dictionary = ['exumacao','inumacao','obito','pericia','necropsia','baragumbaga','caixao','caixaobaleia','putrefacao','chorume','necropole','velorio','sepultamento','jazigo','cremacao']

#alphabetic order
#sorted_dictionary = sorted(dictionary)
#print(sorted_dictionary".format(''))


randomed_word=random.choice(dictionary) #palavra sorteada do dicionario #choices mostra todo o range

letras_acertadas0 = len(randomed_word)*"_"
letras_acertadas = list(letras_acertadas0)
#print(letras_acertadas)

#letras_acertadas = randomed_word.split(' ')
#print( randomed_word.split(' '))
#letras_acertadas = list(randomed_word) 
#print(list(randomed_word))
#letras_acertadas = ['_','_','_','_','_','_','_','_','_','_','_',]

#for letras_acertadas in enumerate (letras_acertadas, start=1):
print('A palavra secreta é: {}'.format(letras_acertadas)) 

acertou = False
enforcou = False
erros = 0

while( not acertou and not enforcou):
    chute = input('Qual letra? ')
    
    if(chute in randomed_word):
        posicao = 0
        print('Você acertou!')
        
        for letra in randomed_word:
                        
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra '{}' na posição {}.".format(letra, posicao))
                letras_acertadas[posicao] = letra                
            posicao += 1
            
    else:
        print('Você errou! Tente novamente...')
        erros += 1
    acertou = '_' not in  letras_acertadas
    enforcou = erros == 6  

    print(letras_acertadas)   
#    print("Encontrei a letra '{}' na posição {}.".format(letra, posicao))    

if(acertou):
    hc_randomed_word = randomed_word.upper()
    print( 'A palavra secreta é: {}.' .format(hc_randomed_word))
    print(' ***************** ')
    print(' *               * ')
    print(' *  Você GANHOU! * ')
    print(' *               * ')
    print(' ***************** ')
else:
    print(' ________________ ')
    print(' |              | ')
    print(' | Você PERDEU! | ')
    print(' |______________| ')
