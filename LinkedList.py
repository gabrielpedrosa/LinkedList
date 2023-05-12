#coding: utf-8
from Product import Product

class LinkedList:
    def __init__(self) -> None:
        self.size = 0.0
        self.list = None
        self.increase = None
        
    def create(self, size = 0) -> None:
        '''
        Cria uma lista encadeada com o tamanho indicado.
        
        :param size: (int) tamanho da lista encadeada.
        '''
        try:
            if(size <= 0):
                raise Exception("size must be greater than 0!")
            
            self.size = size
            self.list = [None]*self.size
            self.increase = 0
        except Exception as ex:
            print(f"cannot create linked list with size '{self.size}'! message: {ex}")
    
    def insert(self, position, element) -> None:
        try:
            self._raiseFull()
            
            allowed = True
            other = False
            
            if(self._isPositionValid(position)):
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
    
    def _insertOverwriting(self, position, element) -> None:
        try:
            self.list[position] = element
            self.increase += 1
        except:
            raise Exception(f"cannot insert overwriting value!")
    
    def _insertNextPosition(self, position, element) -> None:
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
    
    def _isPositionValid(self, position: int) -> bool:
        try:
            return self.list[position] != None
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
            
            return self.list[position]
        except Exception as ex:
            print(f"cannot get element at position '{position}'! message: {ex}")
    
    def search(self, elementName) -> int:
        '''
        Retorna a posição do elemento na lista.
        
        :param elementName: nome do elemento.
        :return: (int) posição do elemento.
        '''
        try:
            print("returning element position...")
            cont = 0
            
            for element in self.list:
                if(element != None):
                    if(element.name == elementName):
                        return cont 
                       
                cont += 1
            print("no result found on list!")
        except Exception as ex:
            print(f"cannot search element '{elementName}'! message: {ex}")
    
    def show(self) -> None:
        '''
        Exibe os elementos da lista.
        '''
        try:
            self._raiseEmpty()
            
            cont = 0
            
            for element in self.list:
                if(element == None):
                    print(f"{cont}. {self.element}")
                else:
                    print(f"{cont}. ")
                    
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
        return self.size <= 0 or self.list == None
    
    def _raiseEmpty(self) -> None:
        '''
        Lança uma exceção de lista vazia.
        '''
        if(self.isEmpty):
            raise Exception("list is empty!")