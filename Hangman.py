import random 

def Hangman():

    print("Bem-vindo(a) ao Jogo da Forca! \n")

    # Escolher o conteúdo do jogo:
    escolher = input("O Jogo da Forca poderá abordar os conteúdos abaixo: \n 1. Frutas.\n 2. Cores. \n 3. Profissões. \n 4.Objetos. \n 5. Animais. \n Digite o conteúdo que será abordado no Jogo da Forca: ")
    if escolher == "1":
        palavras = ["uva", "banana","abacaxi", "pera", "maca"]
    if escolher == "2":
        palavras = ["rosa", "azul","laranja","verde", "amarelo"]
    if escolher == "3":
        palavras = ["advogado", "engenheiro", "arquiteto", "veterinario", "medico"]
    if escolher == "4":
        palavras = ["copo", "faca","prato", "computador", "televisao"]
    if escolher == "5":
        palavras ["cachorro", "gato", "vaca","pato", "minhoca"]
    
    # Escolha aleatória da palavra e imprimir o seu tamanho 
    palavra_escolhida = random.choice(palavras)
    tamanho = len(palavra_escolhida)
    print(f"A palavra escolhida tem {tamanho} letras.")

    # Printar caracter para palavr1a oculta
    caracter = "_"
    palavra_oculta = [caracter for letra in palavra_escolhida]
    print(" ".join(palavra_oculta))

    # Cria lista de letras inseridas e define as chances do usuário
    letras_inseridas = []
    chances = tamanho + 3

    # Loop verdadeiro
    while chances > 0:

        # Orienta o usuário a digitar uma letra e verifica a sua aceitação. Caso aceita, adiciona à lista de letras inbseridas. 
        letra_digitada = input("Digite uma letra: ").lower()
        numerico = letra_digitada.isnumeric()
        especial = letra_digitada.isalpha()
        if numerico == True or especial == False:
            print("Não são aceitos valores numéricos ou caracteres especiais.")
        if letra_digitada in letras_inseridas:
            print(f"Você já adicionou essa letra. Tente novamente. As letras inseridas são: {letras_inseridas}")
            continue
        letras_inseridas.append(letra_digitada)

        # Verifica se a letra digitada está ou não na palavra escolhida
        if letra_digitada in palavra_escolhida:
            for indice, caracter in enumerate(palavra_escolhida):
                if caracter == letra_digitada:
                    palavra_oculta[indice] = letra_digitada
            print(''.join(palavra_oculta))

            if palavra_escolhida == "".join(palavra_oculta):
                print("Parabéns, você ganhou!")
                break
        else:
            chances = chances - 1
            print(f"A letra '{letra_digitada}' não está na palavra escolhida. Restam {chances} chances.")

    if chances == 0:
        print("Você infelizmente perdeu. Continue tentando") 
    
Hangman()







