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
    print(itens)
    return(itens)

remove_repetidos(list(input("Insira a lista: ")))