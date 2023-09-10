from random import choice
from time import sleep
pedra = 1
papel = 2
tesoura = 3
print('VAMOS JOGAR JOKEMPÔ!!!')
print('''Escolha uma das opções:
      [  1  ] - PEDRA
      [  2  ] - PAPEL
      [  3  ] - TESOURA''')
opcao = int(input('Sua opção: '))
print('AGORA DEIXA EU PENSAR NA MINHA OPÇÃO...')
sleep(4)
lista = [pedra, papel, tesoura]
escolha_pc = choice(lista)
if escolha_pc == pedra and opcao == 1:
    print('EMPATOU, OS DOIS ESCOLHERAM PEDRA!!!')
elif escolha_pc == papel and opcao == 2:
    print('EMPATOU, OS DOIS ESCOLHERAM PAPEL!!!')
elif escolha_pc == tesoura and opcao == 3:
    print('EMPATOU, OS DOIS ESCOLHERAM TESOURA!!!')
elif escolha_pc == pedra and opcao == 2:
    print('EU PERDI!!! Você escolheu papel e eu escolhi pedra')
elif escolha_pc == pedra and opcao == 3:
    print('EU GANHEI!!! Você escolheu tesoura e eu escolhi pedra')
elif escolha_pc == papel and opcao == 1:
    print('EU GANHEI!!! Você scolheu pedra e eu escolhi papel')
elif escolha_pc == papel and opcao == 3:
    print('EU PERDI!!!, Você escolheu tesoura e eu escolhi papel')
elif escolha_pc == tesoura and opcao == 1:
    print('EU PERDI!!!, Você escolheu pedra e eu escolhi tesoura')
elif escolha_pc == tesoura and opcao == 2:
    print('EU GANHEI!!!, Você escoheu papel e escolhi tesoura')
else: 
    print('Tem que escolher uma daquelas opções burrão')