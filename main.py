Produtos_cadastrados = []


def adicionar_produtos():
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    preco = input("Preço: ")
    produto = {'Nome': nome, 'Categoria': categoria, 'Preço': preco}
    Produtos_cadastrados.append(produto)
    retorno()


def retorno():
    resposta_user = input("Deseja continuar adicionando ?\n")
    if resposta_user == "s":
        adicionar_produtos()
    else:
        listar_produtos()

def listar_produtos():
        for produto in Produtos_cadastrados:
            nome = produto['Nome'] 
            categoria = produto['Categoria']
            preco = produto['Preço']
            print(f"Nome: {nome},\nCategoria: {categoria}, \nPreço: R${preco}")


def inicio ():
    escolha_user = int(input( 
    "[1] Adicionar Produto \n"           #Pendente
    "[2] Listar Produtos \n"             #Pendente
    "[3] Filtrar por categoria \n"       #Pendente
    "[4] Ordenar produtos por preço \n"  #Pendente
    "[5] Exibir Categorias \n"           #Pendente
    "[6] Salvar Produtos \n"             #Pendente
    "[7] Importar Produtos \n"           #Pendente
    "[0] Sair \n"                        #Pendente
    "Escolha uma opção: "
    ))

    if escolha_user == 1 :
        adicionar_produtos()




inicio()





