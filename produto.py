#coding:utf-8
class Produto(object):
    def __init__(self, size):
        print("Criando Lista...")
        self.size = size
        self.list = [None]*size
    
    def inserir(self, position, produto):
        print("Inserindo Produto...")
        self.list[position] = produto
    
    def remover(self, position):
        print("Removendo Produto...")
        self.list[position] = None
    
    def retornar(self, produto):
        print("Retornar Nome do Produto...")
        cont = 0
        for i in self.list:
            if(i == produto):
                print(cont, i)
            cont += 1
    
    def buscar(self):
        print("Buscar posição do Produto")
    
    def imprimir_lista(self):
        print("Imprimindo valor...")
        cont = 0
        for i in self.list:
            if (i != None):
                print(cont, i)
            else:
                print(cont, "Vazio")
            cont += 1
        