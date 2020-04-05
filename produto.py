#coding:utf-8
class Produto(object):
    def __init__(self):
        print("Incializando......")

    def criar(self):
        print("Criando Produto...")
        self.list = []
    
    def inserir(self):
        print("Inserindo Produto...")
    
    def remover(self):
        print("Removendo Produto...")
    
    def retornar(self):
        print("Retornar Nome do Produto")
    
    def buscar(self):
        print("Buscar posição do Produto")
    
    def imprimir(self):
        print("Imprimir todos os Valores")