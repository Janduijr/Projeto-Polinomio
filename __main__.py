class No():
    def __init__(self, valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.proximo = None

class Lista():
    def __init__(self):
        self.cabeca = None
    
    def inserir(self,valor1,valor2):
        novo = No(valor1,valor2)
        if self.cabeca is None:
            self.cabeca = novo
            return
        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
    
        atual.proximo = novo
    
    def exibir_all(self):
        atual = self.cabeca
        
        if atual == None:
            print('A lista esta vazia!')
            return
        
        while atual is not None:
            print(f'Valor 1: {atual.valor1}\nValor 2: {atual.valor2}')
            atual = atual.proximo
    
    def Obter_Proximo(self, no):
        if self.cabeca is None:
            print('A lista esta vazia!')
            return
        print('Proximos valores:')
        print(f'Valor 1: {no.proximo.valor1}\nValor 2: {no.proximo.valor2}')
    
    def Obter_Valor(self, no):
        if self.cabeca is None:
            print('A lista esta vazia!')
            return
        print('Valores do No:')
        print(f'Valor 1: {no.valor1}\nValor 2: {no.valor2}')
    
        
        


lista1 = Lista()
lista1.inserir(3,4)
lista1.inserir(1,2)
lista1.inserir(8,9)
lista1.exibir_all()
segundo = lista1.cabeca.proximo
lista1.Obter_Proximo(segundo)
lista1.Obter_Valor(segundo)









