class No():
    def __init__(self, coeficiente, grau):
        self.coeficiente = coeficiente
        self.grau = grau
        self.proximo = None

class Lista():
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def inserir(self, coeficiente, grau):
        novo = No(coeficiente, grau)
        if self.cabeca is None:
            self.cabeca = novo
            self.tamanho += 1
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
            if atual.coeficiente >= 0:
                sinal = '+'
            else:
                sinal = '-'
                
            atual.coeficiente = abs(atual.coeficiente)
            
            if atual.grau == 0:
                print(f'{sinal}{atual.coeficiente}', end='')
            elif atual.grau == 1:
                print(f'{sinal}{atual.coeficiente}X ', end='')
            else:
                print(f'{sinal}{atual.coeficiente}X^{atual.grau} ', end='')
            atual = atual.proximo
    
    
    def obter_Valor(self, no):
        if no is None:
            print('O No nao existe!')
            return
        print('Valores do No:')
        print(f'Coeficiente: {no.coeficiente}\nGrau: {no.grau}')
 
    
    def main(self,a):
        self = Lista()
        self.inserir(5, 3)
        self.inserir(2, 2)
        self.inserir(-4, 1)
        self.inserir(7, 0)

        #NOS:
        primeiro = self.cabeca
        segundo = self.cabeca.proximo
        terceiro = segundo.proximo
        quarto = terceiro.proximo
        
        if a == 'G' or a == 'g':
            self.exibir_all()

a = ''     
lista1 = Lista()
while True:
    a = input('\nDigite algo: ')
    if a == 'x' or a == 'X':
        break
    lista1.main(a)
    