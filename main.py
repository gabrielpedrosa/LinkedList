#coding:utf-8
class main(object):
    def __init__(self):
        continuar = True
        while(continuar):
            menu = int(input("Escolha uma opção!\n 1 - Criar um produto\n 2 - Inserir um produto\n 3 - Remover um produto\n 4 - Retornar um produto\n 5 - Buscar um produto\n 6 - Imprimir a Lista\n 7 - Sair\n"))
            if(menu == 1):
                print("1")
            elif(menu == 2):
                print("2")
            elif(menu == 3):
                print("3") 
            elif(menu == 4):
                print("4") 
            elif(menu == 5):
                print("5") 
            elif(menu == 6):
                print("6") 
            elif(menu == 7):
                continuar = False 

main()