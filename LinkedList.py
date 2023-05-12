#coding: utf-8
from Product import Product

class LinkedList:
    def __init__(self, size: int = 0.0) -> None:
        self.size = size
        self.list = None
        self.increase = None
        self.create()
        
    def create(self) -> None:
        '''
        Cria uma lista encadeada com o tamanho indicado.
        
        :param size: (int) tamanho da lista encadeada.
        '''
        try:
            if(self.size <= 0):
                raise Exception("size must be greater than 0!")
            
            self.list = [None]*self.size
            self.increase = 0
        except Exception as ex:
            print(f"cannot create linked list with size '{self.size}'! message: {ex}")
    
    def insert(self, position: int, element: any) -> None:
        '''
        Inserir um valor na lista.
        
        :param position: (int) posição da lista onde o elemento vai ser inserido.
        :param element: (any) elemento que sera inserido na lista.
        '''
        try:
            self._raiseFull()
            
            allowed = True
            other = False
            
            if not(self._isPositionValidToAdd(position)):
                print("opa")
                confirm_1 = int(input("Já existe um produto nessa posição.\nDeseja Sobreescrever: 1 - Sim, 2 - Não\n"))
            
                if confirm_1 == 1:
                    allowed = True
                else:
                    confirm_2 = int(input("Deseja inserir na proxima posição: 1 - Sim, 2 - Não\n"))
                    
                    if (confirm_2 == 1):
                        self._insertNextPosition(position, element)
                        
                        allowed = True
                        other = True
                    else:
                        allowed = False
                        
            if allowed and not(other):
                self._insertOverwriting(position, element)
            elif not(allowed) and not(other):
                print("element not inserted!")
            
        except Exception as ex:
            print(f"cannot insert element! message: {ex}")
    
    def _insertOverwriting(self, position: int, element: any) -> None:
        '''
        Inserir sobrescrevendo o valor anterior.
        
        :param position: (int) posição que o elemento será inserido.
        :param element: (any) elemento a ser inserido.
        '''
        try:
            self.list[position] = element
            self.increase += 1
        except:
            raise Exception(f"cannot insert overwriting value!")
    
    def _insertNextPosition(self, position: int, element: any) -> None:
        '''
        Insere na próxima posição vazia da lista.
        
        :param position: (int) posição do elemento.
        :param element: (any) elemento a ser inserido.
        '''
        try:
            cont = position
            
            for el in self.list:
                if(cont >= self.size):
                    cont = 0
                
                if(el == None):
                    nextPosition = cont
                    break
            
                cont += 1
            
            self.insert(nextPosition, element)
        except:
            raise Exception("cannot insert on nextPosition!")
    
    def _isPositionValidToAdd(self, position: int) -> bool:
        '''
        Verifica se existe algo na posição selecionada para adicionar.
        
        :param position: (int) posição na lista.
        :return: (bool) True, não existe e pode adicionar.
        '''
        try:
            self._raiseInvalidList()
            
            return self.list[position] == None
        except Exception as ex:
            print(f"cannot validate position! message: {ex}")
        return False
    
    def remove(self, position) -> bool:
        '''
        Remove um elemento da lista.
        
        :param position: (int) posição do elemento na lista.
        '''
        try:
            self.list[position] = None
            
            return True
        except Exception as ex:
            print(f"cannot remove element! mesage: {ex}")
            return False

    def get(self, position: int) -> Product:
        '''
        Retorna o elemento na posição indicada.
        
        :return: (any) elemento.
        '''
        try:
            self._raiseEmpty()
            
            element = self.list[position]
            if(element == None):
                raise Exception("list position is empty!")
            else:
                return self.list[position]
            
        except Exception as ex:
            return ex
    
    def search(self, elementSearch) -> int:
        '''
        Retorna a posição do elemento na lista.
        
        :param elementSearch: elemento a ser procurado.
        :return: (int) posição do elemento.
        '''
        try:
            cont = 0
            
            for element in self.list:
                if(element != None):
                    if(element == elementSearch):
                        return cont 
                       
                cont += 1
            raise Exception(f"no result found of '{elementSearch}' on list!")
        except Exception as ex:
            return ex
    
    def show(self) -> None:
        '''
        Exibe os elementos da lista.
        '''
        try:
            self._raiseInvalidList()
            self._raiseEmpty()
            
            cont = 0
            
            for element in self.list:
                if(element == None):
                    print(f"{cont}. ")
                else:
                    print(f"{cont}. {element}")
                    
                cont += 1
                
        except Exception as ex:
            print(f"cannot show list! message: {ex}")
    
    def isFull(self) -> bool:
        '''
        Retorna se a lista está cheia.
        
        :return: (bool) True, está cheia.
        '''
        return (self.size <= self.increase)
    
    def _raiseFull(self) -> None:
        '''
        Lança uma exceção de lista cheia.
        '''
        if(self.isFull()):
            raise Exception("list is full!")
    
    def isEmpty(self) -> bool:
        '''
        Retorna se a lista está vazia.
        
        :return: (bool) True, está vazia.
        '''
        return self.size <= 0 
    
    def _raiseEmpty(self) -> None:
        '''
        Lança uma exceção de lista vazia.
        '''
        if(self.isEmpty()):
            raise Exception("list is empty!")
    
    def isValidList(self) -> None:
        '''
        Retorna se a lista é valida.
        
        :return: (bool) True, é válida.
        '''
        return self.list == None
    
    def _raiseInvalidList(self) -> None:
        '''
        Lança uma exceção de lista inválida.
        '''
        if(self.isValidList()):
            raise Exception("list is not created!")
        

if __name__ == "__main__":
    linkedList = None
    
    keepGoing = True
    
    while keepGoing:
        menu = int(input("Escolha uma opção!\n 1 - Criar uma lista\n 2 - Inserir um elemento\n 3 - Remover um elemento por posição\n 4 - Retornar um elemento\n 5 - Buscar por nome do elemento\n 6 - Exibir lista encadeada\n 7 - Sair\n"))
        if(menu == 1):
            size = int(input("Informe o tamanho da lista:\n"))
            linkedList = LinkedList(size)
        elif(menu == 2):
            position = int(input("Informe a posição do elemento que deseja inserir na lista:\n"))
            productName = input("Informe o nome do produto:\n")
            linkedList.insert(position, productName)
        elif(menu == 3):
            position = int(input("Informe a posição do elemento que deseja remover da lista:\n"))
            linkedList.remove(position) 
        elif(menu == 4):
            position = int(input("Informe a posição da lista que deseja buscar:\n"))
            print(linkedList.get(position))
        elif(menu == 5):
            productName = input("Informe o nome do produto que deseja buscar:\n")
            print(linkedList.search(productName))
        elif(menu == 6):
            linkedList.show()
        elif(menu == 7):
            keepGoing = False 