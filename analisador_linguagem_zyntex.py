def analisar_lexico(codigo):
    i = 0
    tamanho = len(codigo)

    palavras_chave = {"fx", "vx", "zf", "zl", "fr", "wl", "out", "in", "rx"}
    tipos = {"int", "float", "char", "string", "bool", "arr", "list", "function", "null", "void", "dict"}
    operadores = {
        "+>", "->", "++", "--", "**", "//", "rd", "exp",
        "=?", "!=?", "<<", ">>", "<=", ">=", "&&", "||", "!", ":=", "=>"
    }
    simbolos = {"{", "}", "(", ")", ";", ","}

    while i < tamanho:
        c = codigo[i]

        # Ignorar espaços em branco
        if c.isspace():
            i += 1
            continue

        # Comentários
        if codigo[i:i+2] == "##":
            i += 2
            while i < tamanho and codigo[i] != '\n':
                i += 1
            if i < tamanho and codigo[i] == '\n':
                i += 1  # Consumir a quebra de linha
            continue

        # Strings entre aspas duplas
        if c == '"':
            i += 1
            string = ''
            while i < tamanho and codigo[i] != '"':
                string += codigo[i]
                i += 1
            i += 1  # Consumir aspas finais
            print(f'TOKEN: STRING "{string}"')
            continue

        # Números
        if c.isdigit() or (c == '.' and i + 1 < tamanho and codigo[i + 1].isdigit()):
            numero = ''
            tem_ponto = False
            while i < tamanho and (codigo[i].isdigit() or codigo[i] == '.'):
                if codigo[i] == '.':
                    if tem_ponto or (i + 1 >= tamanho or not codigo[i + 1].isdigit()):
                        break
                    tem_ponto = True
                numero += codigo[i]
                i += 1
            print(f"TOKEN: NUMERO {numero}")
            continue

        # Identificadores, palavras-chave ou tipos
        if c.isalpha() or c == '_':
            ident = ''
            while i < tamanho and (codigo[i].isalnum() or codigo[i] == '_'):
                ident += codigo[i]
                i += 1
            if ident in palavras_chave:
                print(f"TOKEN: PALAVRA_CHAVE {ident}")
            elif ident in tipos:
                print(f"TOKEN: TIPO {ident}")
            else:
                print(f"TOKEN: IDENTIFICADOR {ident}")
            continue

        # Operadores compostos
        encontrado = False
        for op in sorted(operadores, key=len, reverse=True):
            if codigo.startswith(op, i):
                print(f"TOKEN: OPERADOR {op}")
                i += len(op)
                encontrado = True
                break
        if encontrado:
            continue

        # Símbolos
        if c in simbolos:
            print(f"TOKEN: SIMBOLO {c}")
            i += 1
            continue

        # Caractere desconhecido
        print(f"TOKEN: DESCONHECIDO {c}")
        i += 1
