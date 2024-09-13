num = int(input("Digite um número inteiro:"))
div = 100000000000
sum = 0


while num > 0 and div > 0:
    if num >= div:
        sum += num // div
        num = num % div
    div = div / 10
print (int(sum))