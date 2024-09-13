num = int(input("Insira um número e descubra se é impar ou par: "))
if num % 5 == 0 and num %3 == 0:
    print("FizzBuzz")
else:
    print(num)