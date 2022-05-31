'''
  Se listarmos todos os números naturais abaixo de 10
  que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A
  soma desses múltiplos é 23. Encontre a soma de todos
  os múltiplos de 3 ou 5 abaixo de 1000.
'''


def soma_multiplos(n=1000):
    result = 0

    for i in range(n):
        if ((i % 3) == 0) or ((i % 5) == 0):
            result += i

    return result


if (__name__ == "__main__"):
    response = soma_multiplos()

    print(f"Resultado: {response}")
