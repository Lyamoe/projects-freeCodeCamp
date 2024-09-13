soma = 0

for i in range (4):
    num = float(input(f"Insira o {i+1}° número"))
    soma = soma + num

print("A média aritmética é:", soma/4)