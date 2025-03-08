def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def calculator():
    print("Bem-vindo à Calculadora!")
    
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        
        choice = input("Digite sua escolha (1/2/3/4): ")
        if choice not in ['1', '2', '3', '4']:
            print("Escolha inválida! Tente novamente.")
            continue
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite números válidos.")
            continue
        
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        
        # Solicita se o usuário deseja realizar outro cálculo.
        while True:
            again = input("Deseja fazer outro cálculo? (sim/não): ").strip().lower()
            if again == "sim":
                break  # Retorna ao loop principal
            elif again == "não":
                print("Obrigado por usar a calculadora!")
                return  # Encerra a função e o programa
            else:
                print('Entrada inválida! Por favor, responda com "sim" ou "não".')

if __name__ == "__main__":
    calculator()
