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
    
        if self.cabeca is None or grau > self.cabeca.grau:
            novo.proximo = self.cabeca
            self.cabeca = novo
            self.tamanho += 1
            return
        
        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.grau >= grau:
            atual = atual.proximo
        
        novo.proximo = atual.proximo
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
                
            coef = abs(atual.coeficiente)
            
            if atual.grau == 0:
                print(f'{sinal}{coef}', end='')
            elif atual.grau == 1:
                print(f'{sinal}{coef}X ', end='')
            else:
                print(f'{sinal}{coef}X^{atual.grau} ', end='')
            atual = atual.proximo

    def exibir_grau(self):
        atual = self.cabeca
        if atual is None:
                print('A lista esta vazia!')
                return
            
        maior = atual.grau
                
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
        
    def buscar_por_grau(self, grau): 
        atual = self.cabeca
        while atual is not None:
            if atual.grau == grau:
                return atual
            atual = atual.proximo
        return None
    
    def somar(self,outro):
        resultado = Lista()
        
        atual = self.cabeca
        while atual is not None:
            resultado.inserir(atual.coeficiente, atual.grau)
            atual = atual.proximo
        
        atual = outro.cabeca
        while atual is not None:
            existente = resultado.buscar_por_grau(atual.grau)
            if existente is not None:
                existente.coeficiente += atual.coeficiente
            else:
                resultado.inserir(atual.coeficiente, atual.grau)
            atual = atual.proximo
        
        return resultado
    
    def subtrair(self,outro):
            resultado = Lista()
            
            atual = self.cabeca
            while atual is not None:
                resultado.inserir(atual.coeficiente, atual.grau)
                atual = atual.proximo
            
            atual = outro.cabeca
            while atual is not None:
                existente = resultado.buscar_por_grau(atual.grau)
                if existente is not None:
                    existente.coeficiente -= atual.coeficiente
                else:
                    resultado.inserir(-atual.coeficiente, atual.grau)
                atual = atual.proximo
            
            return resultado
        
    def multiplicar(self, outro):
        resultado = Lista()
        
        atual1 = self.cabeca
        while atual1 is not None:
            atual2 = outro.cabeca
            while atual2 is not None:
                # multiplica coef. e soma graus
                novo_coeficiente = atual1.coeficiente * atual2.coeficiente
                novo_grau = atual1.grau + atual2.grau
                
                # agrupa se mesmo grau
                existente = resultado.buscar_por_grau(novo_grau)
                if existente is not None:
                    existente.coeficiente += novo_coeficiente
                else:
                    resultado.inserir(novo_coeficiente, novo_grau)
                
                atual2 = atual2.proximo
            atual1 = atual1.proximo
        
        return resultado
    
    def avaliar(self, x):
        atual = self.cabeca
        resultado = 0
        
        while atual is not None:
            resultado += atual.coeficiente * (x ** atual.grau)
            atual = atual.proximo
        
        print(f'O valor do polinomio para X = {x} eh: {resultado}')
            
            
            
     
        

a = ''     
listas = {'1': Lista(), '2': Lista(), 'resultado': Lista()}

atual = '1'

listas['1'].inserir(-3, 5)
listas['1'].inserir(6, 3)
listas['1'].inserir(-7, 1)
listas['1'].inserir(8, 0)
listas['2'].inserir(8, 1)
listas['2'].inserir(6, 4)
listas['2'].inserir(-2, 0)


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
    elif a == 'r':
        atual = 'resultado'
        print('Voce mudou para o polinomio de resultados!')
    elif a == 'g' or a == 'G':
        listas[atual].exibir_grau()
    elif a == 't' or a == 'T':
        listas[atual].exibir_tamanho()
    elif a == 'e' or a == 'E':
        listas[atual].exibir_all()
    elif a == '+':
        if atual == '1':
            outra = '2'
        elif atual == '2':
            outra = '1'
        listas['resultado'] = listas[atual].somar(listas[outra])
        atual = 'resultado'
        print('Soma calculada! Digite "a" para ver o resultado.')
    elif a == '-':
        if atual == '1':
            outra = '2'
        elif atual == '2':
            outra = '1'
        listas['resultado'] = listas[atual].subtrair(listas[outra])
        atual = 'resultado'
        print('Subtração calculada! Digite "a" para ver o resultado.')
    elif a == '*':
        if atual == '1':
            outra = '2'
        elif atual == '2':
            outra = '1'
        listas['resultado'] = listas[atual].multiplicar(listas[outra])
        atual = 'resultado'
        print('Multiplicação calculada! Digite "a" para ver o resultado.')
    elif a == 'a' or a == 'A':
        x = float(input('Digite o valor de X: '))
        resultado = listas[atual].avaliar(x)
            

    
    