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
        print(maior,'\n')
        
    
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
    
    def buscar_por_coefiente(self): 
            atual = self.cabeca
            while atual is not None:
                if atual.coeficiente == 0:
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
                novo_coeficiente = atual1.coeficiente * atual2.coeficiente
                novo_grau = atual1.grau + atual2.grau
                
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
        
        print(f'O valor do polinomio para X = {x} eh: {resultado}\n')
        
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
        
    def simplificar(self):
        zero = self.buscar_por_coefiente()
        while zero is not None:
            self.excluir(zero)
            zero = self.buscar_por_coefiente()
        return self


#PEGANDO TXT
def ler_documento():
    with open('arquivo.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    
    conteudo = []
    
    for linha in linhas:
        linha = linha.strip()
        
        if linha == '':
            continue
        
        if linha.lower() in ('+', '-', '*', 'g', 'p', 'a', 's', 't'):
            conteudo.append(linha.lower())
        else:
            partes = linha.split()
            numeros = []
            for p in partes:
                numeros.append(int(p))
            conteudo.append(numeros)
    
    return conteudo


def montar_polinomio(numeros):
    polinomio = Lista()
    
    i = 0
    while i < len(numeros):
        coeficiente = numeros[i]
        grau = numeros[i + 1]
        polinomio.inserir(coeficiente, grau)
        i += 2
    
    return polinomio


conteudo = ler_documento()
vezes = 0
i = 0
while i < len(conteudo):
    comando = conteudo[i]
    
    if comando == '+':
        print(f'Exibindo comando Somar: ({vezes})')
        poli1 = montar_polinomio(conteudo[i + 1])
        poli2 = montar_polinomio(conteudo[i + 2])
        resultado = poli1.somar(poli2)
        resultado.exibir_all()
        print('\n')
        vezes += 1
        i += 3
    
    elif comando == '-':
        print(f'Exibindo comando Subtrair: ({vezes})')
        poli1 = montar_polinomio(conteudo[i + 1])
        poli2 = montar_polinomio(conteudo[i + 2])
        resultado = poli1.subtrair(poli2)
        resultado.exibir_all()
        print('\n')
        vezes += 1
        i += 3
    
    elif comando == '*':
        print(f'Exibindo comando Mutiplicar: ({vezes})')
        poli1 = montar_polinomio(conteudo[i + 1])
        poli2 = montar_polinomio(conteudo[i + 2])
        resultado = poli1.multiplicar(poli2)
        resultado.exibir_all()
        print('\n')
        vezes += 1
        i += 3
    
    elif comando == 's':
        print(f'Exibindo comando Simplificar: ({vezes})')
        poli = montar_polinomio(conteudo[i + 1])
        poli.simplificar()
        poli.exibir_all()
        print('\n')
        vezes += 1
        i += 2
    
    elif comando == 'g':
        print(f'Exibindo comando para exibir grau: ({vezes})')
        poli = montar_polinomio(conteudo[i + 1])
        poli.exibir_grau()
        vezes += 1
        i += 2
    
    elif comando == 'p':
        print(f'Exibindo comando de exibir polinomio: ({vezes})')
        poli = montar_polinomio(conteudo[i + 1])
        poli.exibir_all()
        print('\n')
        vezes += 1
        i += 2
    
    elif comando == 'a':
        print(f'Exibindo comando de Avaliar: ({vezes})')
        poli = montar_polinomio(conteudo[i + 2])
        x = conteudo[i + 1][0]
        poli.avaliar(x)
        vezes += 1
        i += 3
        
    elif comando == 't':
        print(f'Exibindo comando de Tamanho: ({vezes})')
        poli = montar_polinomio(conteudo[i + 1])
        poli.exibir_tamanho()
        vezes += 1
        i += 2
        
    
    else:
        i += 1
        