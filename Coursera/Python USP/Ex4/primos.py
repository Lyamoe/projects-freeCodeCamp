def maior_primo(num):
    while num > 1:
        primo = éPrimo(num)
        if primo == False:
            num -= 1
        else:
            return num

def éPrimo(k):
    mult = 2
    while mult < k:
        if k % mult == 0:
            return False
        else:
            mult +=1
    return True
    
num1 = int(input("Insira o número:"))
while num1 < 2:
    num1 = int(input("Insira um número maior ou igual a 2:"))
print(maior_primo(num1))