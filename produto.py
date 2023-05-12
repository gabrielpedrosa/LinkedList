#coding:utf-8
class Produto(object):
    def __init__(self):
        print("Inicilizando...")
        
    #def criar(self, size):
        print("Criando Lista...")
        self.size = size
        self.list = [None]*size
        self.increase = 0
        print(("Criado"))

    def inserir(self, position, produto):
        if(self.size > self.increase):
            print("Inserindo Produto...")
            allow = True
            other = False
            if(self.list[position] != None ):
                sure = int(input("Já existe um produto nessa posição.\nDeseja Sobreescrever: 1 - Sim, 2 - Não\n"))
                if(sure == 1):
                    allow = True
                else:
                    sure2 = int(input("Deseja inserir na proxima posição: 1 - Sim, 2 - Não\n"))
                    if(sure2 == 1):
                        cont = position
                        for i in self.list:
                            if(cont >= self.size):
                                cont = 0
                            if(i == None):
                                next = cont
                                break
                            cont += 1
                        self.inserir(next, produto)
                        allow = True
                        other = True
                    else:
                        allow = False
            if allow and not(other):
                self.list[position] = produto
                print("Inserido")
                self.increase += 1
            elif not(allow) and not(other):
                print("Não inserido")
        else:
            print("Lista Cheia!")

    #def remover(self, position):
        print("Removendo Produto...")
        self.list[position] = None
        print("Removido")
    
    # def retornar(self, produto):
        print("Retornar Nome do Produto...")
        cont = 0
        for i in self.list:
            if(i == produto):
                print("Posição: "+str(cont)+" Produto: "+str(i))
            cont += 1
    
    # def buscar(self, produto):
        print("Buscar posição do Produto")
        cont = 0
        for i in self.list:
            if(i == produto):
                print("Posição: "+str(cont))
            cont += 1
    
    # def imprimir(self):
        print("Imprimindo valor...")
        cont = 0
        for i in self.list:
            if (i != None):
                print(cont, i)
            else:
                print(cont, " ")
            cont += 1
        print("Impresso")
        