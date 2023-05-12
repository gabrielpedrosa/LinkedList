#coding: utf-8
from LinkedList import LinkedList
if __name__ == "__main__":
    linkedList = LinkedList()
    
    keepGoing = True
    
    while keepGoing:
        menu = int(input("Escolha uma opção!\n 1 - Criar uma lista\n 2 - Inserir um elemento\n 3 - Remover um elemento por posição\n 4 - Retornar um elemento\n 5 - Buscar por nome do elemento\n 6 - Exibir lista encadeada\n 7 - Sair\n"))
        if(menu == 1):
            size = int(input("Informe o tamanho da lista:\n"))
            linkedList.create(size)
        elif(menu == 2):
            position = int(input("Informe a posição do produto que deseja inserir na lista :\n"))
            productName = input("Informe o nome do produto:\n")
            linkedList.insert(position, productName)
        elif(menu == 3):
            position = int(input("Informe a posição do produto que deseja remover da lista :\n"))
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