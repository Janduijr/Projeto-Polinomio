class No():
    def __init__(self, valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.proximo = None

class Lista():
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def inserir(self,valor1,valor2):
        novo = No(valor1,valor2)
        if self.cabeca is None:
            self.cabeca = novo
            self.tamanho +=1
            return
        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
    
        atual.proximo = novo
        self.tamanho += 1
    
    def exibir_all(self):
        atual = self.cabeca
        
        if atual is None:
            print('A lista esta vazia!')
            return
        
        print('Exibindo todos os valores:')
        while atual is not None:
            print(f'Valor 1: {atual.valor1}\nValor 2: {atual.valor2}')
            atual = atual.proximo
    
    def obter_Proximo(self, no):
        if no is None:
            print('No informado é invalido!')
            return
        if no.proximo is None:
            print('Nao ha proximo!')
            return
        print('Proximos valores:')
        print(f'Valor 1: {no.proximo.valor1}\nValor 2: {no.proximo.valor2}')
    
    def obter_Valor(self, no):
        if no is None:
            print('O No nao existe!')
            return
        print('Valores do No:')
        print(f'Valor 1: {no.valor1}\nValor 2: {no.valor2}')
    
    def alterar_no(self,no,valor1,valor2):
        if no is None:
            print('Nao existe esse No!')
            return
        no.valor1 = valor1
        no.valor2 = valor2
        print('VALORES ALTERADOS: ')
        print(f'Valor 1: {no.valor1}\nValor 2: {no.valor2}')
    
    def exibir_tamanho(self):
        print(f'A lista possui tamanho {self.tamanho}')
        
    def existe(self,no):
        tem = False
        atual = self.cabeca
        while atual is not None:
            if atual is no:
                tem = True
            atual = atual.proximo
        if tem == True:
            print('Existe!')
        else:
            print('Nao existe!')
    
    def buscar(self, valor):
        busca = False
        atual = self.cabeca
        while atual is not None:
            if valor == atual.valor1 or valor == atual.valor2:
                busca = True
            atual = atual.proximo
        if busca == True:
            print('Existe valor!')
        else:
            print('Nao existe valor!')

        
         
    
        
        


lista1 = Lista()
lista1.inserir(3,4)
lista1.inserir(1,2)
lista1.inserir(8,9)


#NOS:
primeiro = lista1.cabeca
segundo = lista1.cabeca.proximo
terceiro = segundo.proximo
quarto = terceiro.proximo

lista1.existe(quarto)
lista1.obter_Valor(segundo)
lista1.obter_Proximo(terceiro)
lista1.alterar_no(segundo,6,7)
lista1.exibir_all()
lista1.exibir_tamanho()
lista1.buscar(8)












