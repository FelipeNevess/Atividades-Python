'''
    Cada novo termo na sequência de Fibonacci é gerado
    pela adição dos dois termos anteriores. Começando
    com 1 e 2, os 10 primeiros termos serão:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    Considerando os termos da sequência de Fibonacci cujos
    valores não excedem quatro milhões, encontre a soma dos
    termos de valor par.
'''

LIMIT = 4000000


def taking_fibonacci_values(lim=LIMIT):
    fibonacci_sequence = []
    num1, num2 = 1, 1

    if (type(lim) is str):
        raise TypeError(f"O tipo {type(lim)} não é um tipo inteiro")

    while num2 < lim:
        fibonacci_sequence.append(num2)

        sum = num1 + num2
        num1, num2 = num2, sum

    return fibonacci_sequence


def taking_even_values(list_values):
    pairs = [
        v for v in list_values if v % 2 == 0
    ]

    return pairs


def sum_values(pairs):
    sum = 0

    for v in pairs:
        sum += v

    return sum


if (__name__ == '__main__'):
    fibonacci_list = taking_fibonacci_values(10)
    even_values = taking_even_values(fibonacci_list)
    result_sum = sum_values(even_values)

    print(fibonacci_list)
