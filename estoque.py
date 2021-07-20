OPCOES_VALIDAS = 'CLABRS'
LINHA = '----------------------------'


# ok
def menu():
    print('\n---------- MENU ------------')
    print('[C] Cadastrar')
    print('[L] Listar')
    print('[B] Buscar')
    print('[A] Atualizar')
    print('[R] Remover')
    print('[S] Sair')
    print(LINHA)
    opcao = input('Informe a operação desejada: ').upper()
    if opcao in OPCOES_VALIDAS:
        return opcao
    elif opcao == '':
        print(LINHA)
        print('  Opção Digitada Incorreta')
        print(LINHA)
        return menu()
    else:
        print(LINHA)
        print('  Opção Digitada Incorreta')
        print(LINHA)
        return menu()


# ok
def verificar_produto(produto: str, lista_produto: list, lista_qtd: list):
    if produto in lista_produto:
        print(LINHA)
        print('   Produto já cadastrado!')
        print(LINHA)
    else:
        qtd = int(input('Informe a quantidade do produto: '))
        if qtd != '':
            lista_produto.append(produto)
            lista_qtd.append(qtd)
            print(LINHA)
            print('\tProduto Cadastrado!')
            print(LINHA)
        else:
            print(LINHA)
            print('Opção incorreta, tente novamente!')
            verificar_produto(produto, lista_produto, lista_qtd)
    aux = input('Cadastrar novamente - [S][N]: ').upper()
    if aux == 'S':
        cadastrar(lista_produto, lista_qtd)
    else:
        return lista_produto, lista_qtd


# ok
def cadastrar(lista_produto: list, lista_qtd: list):
    print(LINHA)
    print(LINHA)
    nome = input('Informe o nome do produto: ').title()
    if nome != '':
        verificar_produto(nome, lista_produto, lista_qtd)
    else:
        print(LINHA)
        print('Opção incorreta, tente novamente!')
        cadastrar(lista_produto, lista_qtd)


# ok
def listar(lista_produto: list, lista_qtd: list):
    if lista_produto != [] and lista_qtd != []:
        lista_aux = lista_qtd.copy()
        lista_aux1 = lista_produto.copy()
        print(LINHA)
        tipo = input('Por nome ou quantidade: ').title()
        if tipo == 'Nome':
            lista_aux1.sort()
            for i in range(len(lista_produto)):
                aux = lista_aux1[i]
                if aux in lista_produto:
                    x = lista_produto.index(aux)
                    print(LINHA)
                    print(f'Produto: {aux}')
                    print(f'Quantidade: {lista_qtd[x]}')
            return lista_produto, lista_qtd
        elif tipo == 'Quantidade':
            for i in range(len(lista_qtd)):
                aux = lista_aux.index(max(lista_aux))
                print(LINHA)
                print(f'Produto: {lista_aux1[aux]}')
                print(f'Quantidade: {lista_aux[aux]}')
                lista_aux.pop(aux)
                lista_aux1.pop(aux)
            return lista_produto, lista_qtd
        else:
            print(LINHA)
            print('Opção incorreta, tente novamente!')
            listar(lista_produto, lista_qtd)
    else:
        print(LINHA)
        print('Nenhum produto cadastrado!')


# ok
def buscar(lista_produto: list, lista_qtd: list):
    if lista_produto != [] and lista_qtd != []:
        print(LINHA)
        tipo = input('Busca por nome ou quantidade: ').title()
        if tipo == 'Nome':
            print(LINHA)
            nome = input('Qual o nome do produto? ').title()
            if nome in lista_produto:
                aux = lista_produto.index(nome)
                print(LINHA)
                print(f'Produto: {lista_produto[aux]}')
                print(f'Quantidade: {lista_qtd[aux]}')
            else:
                print(LINHA)
                print('O produto está indisponível')
        elif tipo == 'Quantidade':
            print(LINHA)
            qtd = int(input('Informe a quantidade desejada para a busca: '))
            if qtd in lista_qtd:
                for i in range(len(lista_qtd)):
                    if qtd == lista_qtd[i]:
                        print(LINHA)
                        print(f'Produto: {lista_produto[i]}')
                        print(f'Quantidade: {lista_qtd[i]}')
            else:
                print(LINHA)
                print('Não existe produto cadastrado com esta quantidade!')
        else:
            print(LINHA)
            print('Opção incorreta, tente novamente!')
            buscar(lista_produto, lista_qtd)

        print(LINHA)
        aux = input('Buscar novamente - [S][N]: ').upper()
        if aux == 'S':
            buscar(lista_produto, lista_qtd)
    else:
        print(LINHA)
        print('Nenhum produto cadastrado!')


# ok
def atualizar(lista_produto: list, lista_qtd: list):
    if lista_produto != [] and lista_qtd != []:
        print(LINHA)
        nome = input('Qual o produto? ').title()
        qtd = int(input('Qual a nova quantidade? '))
        if nome in lista_produto:
            index = lista_produto.index(nome)
            lista_qtd[index] = qtd
            print(LINHA)
            print('Quantidade atualizada!')
            return lista_produto, lista_qtd
        elif nome == '':
            print(LINHA)
            print(f'Digite novamente as informações!')
            atualizar(lista_produto, lista_qtd)
        else:
            print(LINHA)
            print(f'Não foi possível encontrar o produto!')

    else:
        print(LINHA)
        print('Nenhum produto cadastrado!')


# ok
def remover(lista_produto: list, lista_qtd: list):
    if lista_produto != [] and lista_qtd != []:
        print(LINHA)
        nome = input('Qual o nome do produto a ser removido? ').title()
        if nome in lista_produto:
            index = lista_produto.index(nome)
            lista_produto.pop(index)
            lista_qtd.pop(index)
            print(LINHA)
            print('\t Produto removido!')
            return lista_produto, lista_qtd
        elif nome == '':
            print(f'Digite o nome do produto!')
            remover(lista_produto, lista_qtd)
        else:
            print(LINHA)
            print(f'Produto não está disponível!')
    else:
        print(LINHA)
        print('Nenhum produto cadastrado!')


if __name__ == '__main__':
    list_products = []
    list_qtd = []
    op = menu().upper()
    while op in OPCOES_VALIDAS:
        if op == 'C':
            cadastrar(list_products, list_qtd)
            op = menu().upper()
        elif op == 'L':
            listar(list_products, list_qtd)
            op = menu().upper()
        elif op == 'B':
            buscar(list_products, list_qtd)
            op = menu().upper()
        elif op == 'A':
            atualizar(list_products, list_qtd)
            op = menu().upper()
        elif op == 'R':
            remover(list_products, list_qtd)
            op = menu().upper()
        elif op == 'S':
            break
        else:
            print('\nNenhuma opção selecionada.\nTente novamente!')
            op = menu().upper()
