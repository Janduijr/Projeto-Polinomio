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
    
    def excluir(self,no):
        if no is None or self.cabeca is None:
            print('Nao e possivel excluir!')
            return

        if self.cabeca is no:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return

        atual = self.cabeca
        while atual.proximo is not None:
            if atual.proximo is no:
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return
            atual = atual.proximo
        
        print('No nao encontrado!')
    
    def main(self):
        self = Lista()
        self.inserir(3,4)
        self.inserir(1,2)
        self.inserir(8,9)
        self.inserir(10,3)


        #NOS:
        primeiro = self.cabeca
        segundo = self.cabeca.proximo
        terceiro = segundo.proximo
        quarto = terceiro.proximo

        self.existe(quarto)
        self.obter_Valor(segundo)
        self.obter_Proximo(terceiro)
        self.alterar_no(segundo,6,7)
        self.exibir_all()
        self.exibir_tamanho()
        self.buscar(8)
        
lista1 = Lista()
lista1.main()
    
        
        















