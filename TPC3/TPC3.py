import re
import sys


def tokenize(texto):
    # Define os padrões dos tokens que o analisador reconhece
    padrao = (r'(?P<COMENTARIO>\#[^\n]*)|'
              r'(?P<VAR>\?[a-zA-Z0-9]+)|'
              r'(?P<LINGUA>@[a-zA-Z]{2})|'
              r'(?P<STRING>"[^"]*")|'
              r'(?P<LIMIT>\bLIMIT\b)|'
              r'(?P<NUM>\d+)|'
              r'(?P<ID>[a-zA-Z][a-zA-Z0-9_:]*)|'
              r'(?P<DELIM>[{}\.])|'
              r'(?P<SKIP>\s+)|'
              r'(?P<ERRO>.)')

    # Procura os tokens no texto com expressões regulares
    for m in re.finditer(padrao, texto):
        # Obtém o tipo do token encontrado
        tipo = m.lastgroup

        # Ignora os comentários e os espaços
        if tipo not in ('COMENTARIO', 'SKIP'):
            # Mostra o tipo e o valor do token
            print((tipo, m.group()))


# Lê a entrada linha a linha e analisa cada linha
for linha in sys.stdin:
    tokenize(linha)
