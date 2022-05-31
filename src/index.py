'''
    Para rodar os testes rode o seguinte comando ==> python3 -m pytest

    Site de atividades ===> https://projecteuler.net
'''

from acts.act1.multiplos import soma_multiplos
from acts.act2.fibonacci import taking_fibonacci_values

# A função soma_multiplos pode receber um parametro com valor inteiro
soma_multiplos(10)

# Retorna a soma da lista fibonacci pares de té 4000000
# taking_fibonacci_values(10) ele também recebe um parâmetro inteiro

taking_fibonacci_values()
