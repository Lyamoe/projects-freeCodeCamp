num = int(input("Digite um número inteiro:"))
if num < 10:
    print("O dígito das dezenas é", 0)
else:
    dezena = str(num)[-2]
    print(f"O dígito das dezenas é {int(dezena)}")
