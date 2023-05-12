#coding: utf-8

class Product:
    '''
    Abstração de um produto.
    
    :param name: (str) nome do produto.
    :param value: (double) valor do produto.
    '''
    def __init__(self, name = "chair", value = 100.0) -> None:
        self.name = name
        self.value = value
        
    def __repr__(self) -> str:
        return f"Product(Name: '{self.name}', Value: '{self.value}')"

if __name__ == "__main__":
    p = Product("chair")
    print(p)