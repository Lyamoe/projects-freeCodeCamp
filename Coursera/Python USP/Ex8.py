import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
  return re.findall(r"\w+", frase)

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    #? IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade
    #? nas assinaturas.
    total = 0
    for i in range(6):
            total += (as_a[i] - as_b[i])
    total /= 6
    return total

def soma_elementos(geral):
    soma = 0
    i = 0

    for i in geral:
        soma += i
    
    return(soma)

def calcula_assinatura(texto):
    #* DECLARAÇÕES variáveis
    seppal = []
    contFrase = 0
    tamanhoPalavra = 0
    totalPalavra = 0
    todasPalavras = []

    sepsen = separa_sentencas(texto)
    for i in range (len(sepsen)):
        sepfra = separa_frases(str(sepsen[i]))
        for j in range (len(sepfra)):
            contFrase += 1
            #? Tamanho médio de palavra
            separacao = separa_palavras(str(sepfra))
            if separacao != seppal:
                seppal = separacao
                charac = [len(elem) for elem in seppal]
                tamanhoPalavra += soma_elementos(charac)
                totalPalavra += len(seppal)

                #? Type Token
                for palavras in seppal:
                    todasPalavras.append(palavras)

    #* Tamanho médio de palavra
    mediaPalavra = tamanhoPalavra / totalPalavra

    #* Type Token
    palavraDif = n_palavras_diferentes(todasPalavras) / totalPalavra

    #* Hapax Legomana
    palavraUnica = n_palavras_unicas(todasPalavras) / totalPalavra

    #* Tamanho médio da sentença
    mediaSent = tamanhoPalavra / len(sepsen)

    #* Complexidade da senteça
    compSent = contFrase / len(sepsen)

    #* Tamanho médio da frase
    mediaFrase = tamanhoPalavra / (contFrase)

    return [mediaPalavra, palavraDif, palavraUnica, mediaSent, compSent, mediaFrase]

def avalia_textos(textos, ass_cp):
    #? IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero
    #? (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    avaliacao = []
    comp = 0
    autor = 0

    for i in textos:
        avaliacao.append(compara_assinatura(i, ass_cp))
    
    for i in range(len(avaliacao)):
        if avaliacao[i] > comp:
            comp = avaliacao[i]
            autor = i+1
    
    print(f"O autor do texto {autor} está infectado com COH-PIAH")
    return comp

ass = []
ass_cp = le_assinatura()
totalTexto = le_textos()

for i in range (len(totalTexto)):
    ass.append(calcula_assinatura(totalTexto[i]))

avalia_textos(ass, ass_cp)