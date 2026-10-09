import re


def converter(texto):
    # Converte os títulos Markdown em títulos HTML
    texto = re.sub(r'^### (.*)$', r'<h3>\1</h3>', texto, flags=re.M)
    texto = re.sub(r'^## (.*)$', r'<h2>\1</h2>', texto, flags=re.M)
    texto = re.sub(r'^# (.*)$', r'<h1>\1</h1>', texto, flags=re.M)

    # Converte negrito e itálico
    texto = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', texto)
    texto = re.sub(r'\*(.*?)\*', r'<i>\1</i>', texto)

    # Converte imagens e links
    texto = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', texto)
    texto = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', texto)

    # Converte listas numeradas em elementos HTML
    texto = re.sub(r'^\d+\. (.*)$', r'<li>\1</li>', texto, flags=re.M)
    texto = re.sub(r'((?:<li>.*</li>\n?)+)', r'<ol>\n\1</ol>\n', texto)

    # Devolve o texto convertido
    return texto


# Texto de exemplo para testar o conversor
texto = """# Exemplo
Este é um **texto a negrito**.
Este é um *texto em itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

[Google](https://www.google.com)
![Imagem](imagem.png)
"""

# Mostra o resultado da conversão
print(converter(texto))
