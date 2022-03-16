"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
import math


def front_back(a, b):

    """ Implementação 1: Sucesso | Utilização de operadores divididos em variáveis"""
    # index_a = math.ceil(len(a) / 2)
    # index_b = math.ceil(len(b) / 2)
    #
    # return a[:index_a] + b[:index_b] + a[index_a:] + b[index_b:]

    """ Implementação 2: Sucesso | Utilização de list comprehension"""
    resultado = [math.ceil(len(string) / 2) for string in (a, b)]
    return a[:resultado[0]] + b[:resultado[1]] + a[resultado[0]:] + b[resultado[1]:]


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
