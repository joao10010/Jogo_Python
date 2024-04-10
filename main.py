import random

# Função para imprimir a mensagem de abertura do jogo
def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

# Função para carregar a palavra secreta de uma lista predefinida
def carrega_palavra_secreta():
    palavras = ['banana', 'abacate', 'limao']  # Lista de palavras possíveis
    numero = random.randrange(0, len(palavras))  # Escolhe um índice aleatório
    palavra_secreta = palavras[numero].upper()  # Converte a palavra escolhida para maiúsculas
    return palavra_secreta

# Função para inicializar a lista de letras acertadas com "_"
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]  # Cria uma lista de "_" com o tamanho da palavra secreta

# Função para pedir o chute do jogador
def pede_chute():
    chute = input("Qual letra? ")  # Solicita uma letra do usuário
    chute = chute.strip().upper()  # Remove espaços e converte para maiúsculas
    return chute

# Função para marcar o chute correto nas letras acertadas
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0  # Inicializa o índice para percorrer as letras da palavra secreta
    for letra in palavra_secreta:
        if (chute == letra):  # Se o chute estiver na palavra secreta
            letras_acertadas[index] = letra  # Substitui o "_" pela letra correta
        index += 1  # Incrementa o índice

# Função para imprimir a mensagem de vitória
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")  # Mensagem de vitória

# Função para imprimir a mensagem de derrota e revelar a palavra secreta
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")  # Mensagem de derrota
    print(f"A palavra era {palavra_secreta}")  # Revela a palavra secreta

# Função para desenhar a forca conforme o número de erros
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    # Complete o desenho da forca conforme o número de erros

# Função principal que executa o jogo da forca
def jogo_da_forca():
    imprime_mensagem_abertura()  # Chama a função de abertura
    palavra_secreta = carrega_palavra_secreta()  # Carrega a palavra secreta
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)  # Inicializa as letras acertadas
    print(letras_acertadas)

    enforcou = False  # Variável para verificar se o jogador foi enforcado
    acertou = False  # Variável para verificar se o jogador acertou a palavra
    erros = 0  # Contador de erros

    # Loop do jogo
    while(not enforcou and not acertou):
        chute = pede_chute()  # Pede um chute ao jogador

        if(chute in palavra_secreta):  # Se o chute estiver na palavra secreta
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)  # Marca o chute correto
        else:
            erros += 1  # Incrementa o contador de erros
            desenha_forca(erros)  # Desenha a forca

        enforcou = erros == 6  # Verifica se o jogador foi enforcado
        acertou = "_" not in letras_acertadas  # Verifica se o jogador acertou todas as letras
        print(letras_acertadas)

    # Verifica o resultado do jogo
    if(acertou):
        imprime_mensagem_vencedor()  # Imprime a mensagem de vitória
    else:
        imprime_mensagem_perdedor(palavra_secreta)  # Imprime a mensagem de derrota

# Verifica se o script é o principal e executa o jogo
if __name__ == "__main__":
    jogo_da_forca()
