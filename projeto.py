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

    def exibir_grau(self):
        atual = self.cabeca
        maior = atual.grau
                
        if atual is None:
            print('A lista esta vazia!')
            return
                
        print('O polinomio possui grau:', end= '')
        while atual is not None:
            if atual.grau > maior:
                maior = atual.grau
            atual = atual.proximo
        print(maior)
    
    
    def obter_Valor(self, no):
        if no is None:
            print('O No nao existe!')
            return
        print('Valores do No:')
        print(f'Coeficiente: {no.coeficiente}\nGrau: {no.grau}')
    
    def exibir_tamanho(self):
        print(f'A lista possui {self.tamanho} termos!')
 
        
        

a = ''     
listas = {'1': Lista(), '2': Lista()}

atual = '1'

listas['1'].inserir(5, 3)
listas['1'].inserir(2, 2)
listas['1'].inserir(-4, 1)
listas['1'].inserir(7, 0)
listas['2'].inserir(6, 6)
listas['2'].inserir(8, 2)
listas['2'].inserir(-4, 1)
listas['2'].inserir(8, 0)

while True:
    a = str(input('\nDigite algo: '))
    if a == 'x' or a == 'X':
        break
    elif a == '1':
        print('Voce mudou para o polinomio 1!')
        atual = '1'
    elif a == '2':
        print('Voce mudou para o polinomio 2!')
        atual = '2'
    elif a == 'g' or a == 'G':
        listas[atual].exibir_grau()
    elif a == 't' or a == 'T':
        listas[atual].exibir_tamanho()
    elif a == 'a' or a == 'A':
        listas[atual].exibir_all()

    
    