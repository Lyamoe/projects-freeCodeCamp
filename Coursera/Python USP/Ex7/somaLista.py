def soma_elementos(itens):
    soma = 0
    i = 0

    for i in itens:
        soma += i
    
    print(soma)
    return(soma)

def remove_repetidos(itens):
    itens.sort()
    teste = 102348
    i = 0

    while i < len(itens):
        if itens[i] == teste:
            del itens[i]
        else:
            teste = itens[i]
            if itens[i] == "," or itens[i] == "[" or itens[i] == "]":
                del itens[i]
            else:
                itens[i] = int(itens[i])
                i += 1

    return(itens)

lista = remove_repetidos(list(input("Insira a lista: ")))

soma_elementos(lista)