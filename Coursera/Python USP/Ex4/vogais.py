def vogal (k):
    if k == "a" or k == "e" or k == "i" or k == "o" or k == "u" or k == "A" or k == "E" or k == "I" or k == "O" or k == "U":
        return True
    else:
        return False

letra = str(input("Insira a letra:"))
print(vogal(letra))