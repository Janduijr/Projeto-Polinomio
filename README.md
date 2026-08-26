# Como usar essa ferramenta

Essa ferramenta faz contas com polinômios (soma, subtração, multiplicação e outras) a partir de um arquivo de texto.

## Passo a passo

1. Abra o arquivo `arquivo.txt` e escreva o que você quer calcular (veja os exemplos abaixo).
2. Salve o arquivo.
3. Rode o programa.
4. O resultado aparece na tela.

## O que escrever no arquivo.txt

Você escreve os polinômios como números separados por espaço, alternando entre **coeficiente** e **grau**.

Por exemplo, para escrever o polinômio **-3X⁵ + 6X³ - 7X + 8**, você escreve:
```
-3 5 6 3 -7 1 8 0
```

Antes do(s) polinômio(s), você coloca uma letra ou símbolo dizendo o que quer fazer:

- `+` → somar dois polinômios
- `-` → subtrair dois polinômios
- `*` → multiplicar dois polinômios
- `g` → ver o grau de um polinômio
- `p` → ver o polinômio formatado
- `a` → calcular o valor do polinômio para um número (X)

## Exemplo pronto

```
+
-3 5 6 3 -7 1 8 0
8 1 6 4 -2 0
```

Isso soma os dois polinômios das linhas 2 e 3.

```
g
4 6 3 9
```

Isso mostra o grau do polinômio da linha seguinte.

```
a
3
-2 2 4 1
```

Isso calcula o valor do polinômio da última linha quando X = 3.

## Dica

Sempre que usar `+`, `-` ou `*`, coloque **dois** polinômios logo depois.
Sempre que usar `g` ou `p`, coloque **um** polinômio logo depois.
Sempre que usar `a`, coloque o número de X e depois o polinômio.
