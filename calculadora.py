def adição(x, y):
    return x + y
def subtração (x, y):
    return x - y
def multiplicação (x, y):
    return x * y
def divisão(x, y):
    if y != 0:
        return x / y
    else:
        return("não é possivél dividir usando o zero")
def exibir_menu():
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
while True:
    exibir_menu()

    escolha = input("Digite a opção (1/2/3/4/5): ")

    if escolha == '5':
        print("Calculadora encerrada.")
        break
    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado: ", adicao(num1, num2))

        elif escolha == '2':
            print("Resultado: ", subtracao(num1, num2))

        elif escolha == '3':
            print("Resultado: ", multiplicacao(num1, num2))

        elif escolha == '4':
            print("Resultado: ", divisao(num1, num2))

    else:
        print("Opção inválida. Por favor, escolha novamente.")