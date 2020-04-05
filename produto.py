#coding:utf-8
class Produto(object):
    def __init__(self):
        print("Inicilizando...\n")
        
    def criar(self, size):
        print("Criando Lista...\n")
        self.size = size
        self.list = [None]*size
        print(("Criado\n"))

    def inserir(self, position, produto):
        print("Inserindo Produto...\n")
        self.list[position] = produto
        print("Inserido\n")
    
    def remover(self, position):
        print("Removendo Produto...\n")
        self.list[position] = None
        print("Removido\n")
    
    def retornar(self, produto):
        print("Retornar Nome do Produto...\n")
        cont = 0
        for i in self.list:
            if(i == produto):
                print(cont, i)
            cont += 1
    
    def buscar(self, produto):
        print("Buscar posição do Produto")
        cont = 0
        for i in self.list:
            if(i == produto):
                print("Posição:"+str(cont))
            cont += 1
    
    def imprimir(self):
        print("Imprimindo valor...\n")
        cont = 0
        for i in self.list:
            if (i != None):
                print(cont, i)
            else:
                print(cont, " ")
            cont += 1
        print("Impresso")
        