num = int(input("Digite o valor de n:"))
mult = 1

if num < 0:
    print("Insira um número igual ou maior que 0")
elif num == 0:
    print(1)
else:
    while num !=0:
        mult = mult * num
        num -= 1
    print(mult)