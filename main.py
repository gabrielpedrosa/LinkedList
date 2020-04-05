#coding:utf-8
import produto as prod 
class main(object):
    def __init__(self):
        p = prod.Produto()
        continuar = True
        while(continuar):
            menu = int(input("Escolha uma opção!\n 1 - Criar a lista\n 2 - Inserir um produto\n 3 - Remover um produto\n 4 - Retornar um produto\n 5 - Buscar um produto\n 6 - Imprimir a Lista\n 7 - Sair\n"))
            if(menu == 1):
                size = int(input("Informe o tamanho da lista:\n"))
                p.criar(size)
            elif(menu == 2):
                position = int(input("Informe a posição do produto que deseja inserir na lista :\n"))
                produto = input("Informe o nome do produto:\n")
                p.inserir(position, produto)
            elif(menu == 3):
                position = int(input("Informe a posição do produto que deseja remover da lista :\n"))
                p.remover(position) 
            elif(menu == 4):
                produto = input("Informe o nome do produto que deseja encontrar:\n")
                p.retornar(produto) 
            elif(menu == 5):
                produto = input("Informe o nome do produto que deseja buscar:\n")
                p.buscar(produto) 
            elif(menu == 6):
                p.imprimir()
            elif(menu == 7):
                continuar = False 

main()