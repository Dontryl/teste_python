# Exercício 1
indice = 13

Soma = 0

K = 0

while K < indice:
    K = K + 1 
    Soma = Soma + K
print (Soma)

# Exercício 2 
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def verifica_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

def main():
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    print("Sequência de Fibonacci até o número informado:")
    fibonacci(numero)
    if verifica_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
#Exercício 5 
def inverter_string(string):
    return string[::-1]

def main():
    texto = input("Digite uma string: ")
    string_invertida = inverter_string(texto)
    print("String original:", texto)
    print("String invertida:", string_invertida)

if __name__ == "__main__":
    main()
