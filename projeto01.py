def leitura(nome_arquivo: str):
    try:
        lista = []
        with open(nome_arquivo, 'r') as arquivo:
            arquivo.seek(0)  # positioning cursor at the beginning
            for linha in arquivo:
                linha = linha.strip()
                if linha.isdigit():
                    valor = float(linha)
                    lista.append(valor)
            return lista
    except Exception as e:
        print("Houve uma falha na abertura do arquivo")
        print(e)
        return None

def soma_valores_arquivo():
    valores = leitura("entrada.txt")
    print(valores)
    return sum(valores)

def maior_valor_arquivo():
    valores = leitura("entrada.txt")
    if valores:
        return max(valores)
    else:
        return None

def multiplica_valores_arquivo():
    valores = leitura("entrada.txt")
    if valores:
        result = 1
        for valor in valores:
            result *= valor
        return result
    else:
        return None

if __name__ == '__main__':
    resultado_soma = soma_valores_arquivo()
    print(f"Soma dos valores: {resultado_soma}")

    resultado_maior = maior_valor_arquivo()
    print(f"Maior valor: {resultado_maior}")

    resultado_multiplica = multiplica_valores_arquivo()
    print(f"Multiplicação dos valores: {resultado_multiplica}")
