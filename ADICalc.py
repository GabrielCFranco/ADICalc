def calculadora(valor1, valor2, operacao):
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
    except ValueError:
        return None

    if operacao == '+':
        return valor1 + valor2
    elif operacao == '-':
        return valor1 - valor2
    elif operacao == '*':
        return valor1 * valor2
    elif operacao == '/':
        return valor1 / valor2 if valor2 != 0 else None
    elif operacao == '^':
        return valor1 ** valor2
    else:
        return None

if __name__ == "__main__":
    valor1 = input("Digite o primeiro valor: ")
    valor2 = input("Digite o segundo valor: ")
    operacao = input("Digite a operação (+, -, *, /, ^): ")
    resultado = calculadora(valor1, valor2, operacao)
    if resultado is None:
        print("ERRO")
    else:
        print(f"Resultado: {resultado}")
