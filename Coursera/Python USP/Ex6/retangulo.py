def retangulo (l, a):
    for i in range (a):
        for j in range (l):
            print ("#", end='')
        print(end='\n')

larg = int(input("digite a largura: "))
alt = int(input("digite a altura: "))
retangulo (larg, alt)