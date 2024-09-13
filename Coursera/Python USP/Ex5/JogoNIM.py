# Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que
# seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

# O programa deve implementar:

# Uma função computador_escolhe_jogada que recebe n e m descritos acima e devolve um inteiro correspondente à
# próxima jogada do computador.

# Uma função usuario_escolhe_jogada que verifica se o valor informado é válido.
# Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente.

# Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m.
# A cada jogada, deve ser impresso na tela o estado atual do jogo. Quando a última peça é removida, essa função
# imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!".

# Campeonatos
# Você deverá criar uma outra função chamada campeonato. Essa nova função deve realizar três partidas seguidas.
# Placar: Você ??? X ??? Computador

def computador_escolhe_jogada(n, m):
    goal = m+1

    if n > m:
        while m > 0:
            check = n - m
            if check % goal == 0:
                print(f"O computador tirou {m} peça(s).")
                return m
            else:
                m -= 1
    if m > n:
        print(f"O computador tirou {n} peça(s).")
        return n
    else:
        print(f"O computador tirou {m} peça(s).")
        return m

def usuario_escolhe_jogada(n, m):
    atual = int(input("Quantas peças você vai tirar?"))
    while atual > m or atual < 1 or atual > n:
        atual = int(input("Quantas peças você vai tirar? Lembre do limite."))

    print(f"Voce tirou {atual} peça(s).")
    return atual


def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))

    if n % (m+1) == 0:
        print("Você começa!")
        vitoria = "O computador"
        while n > 0:
            print()
            n -= usuario_escolhe_jogada(n, m)
            print(f"Agora resta apenas {n} peça(s) no tabuleiro.")

            print()
            if n > 0:
                n -= computador_escolhe_jogada(n, m)
                print(f"Agora resta apenas {n} peça(s) no tabuleiro.")
            else:
                vitoria = "Você"
        print(f"Fim do jogo! {vitoria} ganhou!")
    else:
        print("Computador começa!")
        vitoria = "Você"
        while n > 0:
            print()
            n -= computador_escolhe_jogada(n, m)
            print(f"Agora resta apenas {n} peça(s) no tabuleiro.")

            print()
            if n > 0:
                n -= usuario_escolhe_jogada(n, m)
                print(f"Agora resta apenas {n} peça(s) no tabuleiro.")
            else:
                vitoria = "O computador"
        print(f"Fim do jogo! {vitoria} ganhou!")

    if vitoria == "O computador":
        return 1
    else:
        return 2

def campeonato():
    rodada = 1
    computador = 0
    jogador = 0
    
    while rodada < 4:
        print()
        print(f"**** Rodada {rodada} ****")
        print()
        vencedor = partida()
        
        if vencedor == 1:
            computador += 1
        else:
            jogador +=1
        
        rodada += 1
    print()
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {jogador} X {computador} Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

choise = int(input("Seleção: "))
while choise > 2 or choise <1:
    choise = int(input("Selecione 1 ou 2"))
    
if choise == 1:
    partida()
else:
    campeonato()