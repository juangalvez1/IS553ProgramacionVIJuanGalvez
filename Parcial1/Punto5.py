from io import *

class Cesar:
    def __init__(self, k = 0):
        self.k = k
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.alphabetDisplaced = self.alphabet[-self.k:] + self.alphabet[:-self.k]

    def __str__(self):
        return f"{self.alphabet}\n k = {self.k}\n{self.alphabetDisplaced}"
    
    def modifyK(self, k):
        self.k = k
        self.alphabetDisplaced = self.alphabet[-self.k:] + self.alphabet[:-self.k]

    def encode(self, text):
        encryptedText = ""
        for i in range(len(text)):
            if text[i] != ' ':
                encryptedText += self.alphabetDisplaced[self.alphabet.index(text[i])]
            else:
                encryptedText += ' '
        return encryptedText
    
    def deEncode(self, encryptedText):
        text = ""
        for i in range(len(encryptedText)):
            if encryptedText[i] != ' ':
                text += self.alphabet[self.alphabetDisplaced.index(encryptedText[i])]
            else:
                text += ' '
        return text
    
def main():
    print("Este es un codigo que con una clase 'Cesar' que recibe un desplazamiento 'k' y usando sus metodos se puede cifrar o decifrar una palabra con la 'k' dada.")
    
    encription = Cesar(0)
    while 1:
        print("\n--- MENÚ ---")
        print("1. Ingresar desplazamiento")
        print("2. Encriptar una frase")
        print("3. Desencriptar una frase")
        print("4. Salir")

        opcion = int(input("\nSeleccione una opción: "))

        if opcion == 1:
            encription.modifyK(int(input("\nIngrese el desplazamiento para el cifrado: ")))
            print(encription)
        elif opcion == 2:
            phrase = input("\nIngrese la frase a encriptar: ").lower()
            encryptedPhrase = encription.encode(phrase)
            print(f"\nFrase = {phrase}\nEncriptado = {encryptedPhrase}")
        elif opcion == 3:
            encryptedPhrase = input("\nIngrese la frase a desencriptar: ").lower()
            phrase = encription.deEncode(encryptedPhrase)
            print(f"\nEncriptado = {encryptedPhrase}\nFrase = {phrase}")
        elif opcion == 4:
            print("\nSaliendo...")
            break
        else:
            print("Opción no valida, intente de nuevo.")

main()