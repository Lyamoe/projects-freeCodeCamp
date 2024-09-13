def maximo(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return "Mesmo número"

num1 = int(input("Insira o 1° número:"))
num2 = int(input("Insira o 2° número:"))
print(maximo(num1, num2))