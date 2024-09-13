def retangulo (l, a):
    for i in range (a):
        if i == 0 or i == a-1:
            for j in range (l):
                print ("#", end='')
            print(end='\n')
        else:
            print ("#", end='')
            for k in range (l-2):
                print(" ", end='')
            print ("#", end='\n')

larg = int(input("digite a largura: "))
alt = int(input("digite a altura: "))
retangulo (larg, alt)