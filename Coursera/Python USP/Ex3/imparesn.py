num = int(input("Digite o valor de n:"))
i = 0
impar = 0

if num <= 0:
    print("Insira um número maior que 0")
else:
    while impar < num:
        i += 1
        if i % 2 != 0:
            print(i)
            impar += 1
        