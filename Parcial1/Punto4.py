def main():
    print("Punto 4 del parcial I\n")
    num = int(input("Ingrese un numero de 4 cifras: "))

    firstDigit = num // 1000
    secondDigit = (num % 1000) // 100
    thirdDigit = (num % 100) // 10
    fourthDigit = num % 10

    if firstDigit % fourthDigit == 0:
        print(f"{firstDigit} SI es multiplo de {fourthDigit}")
    else:
        print(f"{firstDigit} NO es multiplo de {fourthDigit}")

    sumSecondThird = secondDigit + thirdDigit
    print (f"La suma del secondDigit y el tercer numero es: {sumSecondThird}")

main()