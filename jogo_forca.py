import random as rd


def main():

    dificuldade = int(input("insira o nivel de dificuldade (1, 2 ou 3): "))
    
    palavra_secreta = cria_palavra(dificuldade)
    visual = cria_visual(palavra_secreta)

    score = jogo_forca(palavra_secreta, visual)
    final_score = score*dificuldade

    print(f"Pontuação final: {final_score}")


def cria_palavra(dificuldade):

    if dificuldade == 1:
        palavras_secretas = ("gato", "cachorro", "casa", "passaro", "sol")

    elif dificuldade == 2:
        palavras_secretas = ("computador", "telefone", "bicicleta", "livro", "cadeira")

    elif dificuldade == 3:
        palavras_secretas = ("contemporaneo", "Indectavel", "Superficie", "sublime")

    palavras_secreta = palavras_secretas[rd.randint(0, len(palavras_secretas)-1)] 

    return palavras_secreta

def cria_visual(palavra):
    return ["_"for i in palavra]


def jogo_forca(palavra_secreta, visual):
    acertos = 0
    erros = 0
    quantidade_letras = len(palavra_secreta)

    while(erros < 7 and acertos < quantidade_letras):
        print(visual)
        letra_advinhada = input("insira uma letra: ")
        acerto = False

        for i in range(quantidade_letras):
            letra = palavra_secreta[i]

            if letra_advinhada == letra:
                acertos += 1
                acerto = True
                visual[i] = letra
        

        if acerto == False:
            erros += 1
            visual_erros(erros)

    if acerto == False:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        
        pontos = 0
    
    else: 
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

        pontos = calculo_pontos(erros)

    return pontos


def calculo_pontos(erros):
    return (7-erros)*100

def visual_erros(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



if __name__ == "__main__":
    main()