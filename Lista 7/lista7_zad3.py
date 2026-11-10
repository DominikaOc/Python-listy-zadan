def get_words(prefix='', contains='', suffix=''):
    lista = []
    with open("collins2015.txt") as f:
        for line in f:
            x = line.strip() #usuwanie białych znaków
            if x.startswith(prefix) and x.endswith(suffix) and contains in x:
                lista.append(x)


    return sorted(lista)