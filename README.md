
# Karatsuba Algorithm - Multiplicação Binária

Este repositório contém uma implementação em Python do algoritmo de Karatsuba para multiplicação binária. O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de dois números grandes, utilizando a abordagem de dividir para conquistar, que reduz a complexidade em comparação à multiplicação tradicional.

## Como funciona

O script realiza a multiplicação de dois números binários utilizando o algoritmo de Karatsuba. Para isso, ele divide os números binários em partes menores, realiza operações de soma e subtração binária, e combina os resultados intermediários para obter o produto final.

### Funções principais

1. **addBinary(x, y)**: Realiza a soma de dois números binários.
2. **multiplyBinary(x, y)**: Multiplica dois números binários de um único dígito.
3. **substractBinary(x, y)**: Realiza a subtração de dois números binários.
4. **ajustSize(x, y)**: Ajusta o tamanho dos dois números binários para que ambos tenham o mesmo comprimento, preenchendo com zeros à esquerda.
5. **karatsuba(num1, num2)**: Implementação recursiva do algoritmo de Karatsuba para multiplicação binária.

### Estrutura do código

- O código começa verificando se os argumentos fornecidos são válidos.
- Verifica se as entradas são números binários.
- Ajusta os tamanhos das entradas para que tenham o mesmo número de dígitos.
- Aplica o algoritmo de Karatsuba para realizar a multiplicação binária.

## Como executar

Para executar o programa, você deve ter o Python instalado. O script espera dois números binários como entrada e pode ser executado no terminal da seguinte forma:

```bash
python3 karatsuba.py <bin1> <bin2>
```

### Exemplo de execução

```bash
python3 karatsuba.py 1011 1101
```

### Saída esperada

O resultado da multiplicação binária dos números fornecidos será exibido no terminal.