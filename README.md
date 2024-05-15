# Python

## Motivação

A primeira linguagem de programação que tive contato foi python, normalmente é a primeira linguagem que a maioria dos estudantes de programação tem contato pela sua facilidade de compreensão e por outros tantos motivos. Com o passar do tempo deixei de programar em python e me dediquei a linguagens de baixo nivel como C e C++.
Programar é como andar de bicicleta, você nunca esquece, mas perde a pratica. Então para retornar de forma mais eficiente, além de apenas fazer vários programas por dia resolvi escrever tudo que considero importante. 

## Introdução

Python é uma linguagem de :
- Alto nivel: Usa expressões em inglês e uma sintaxe fácil que se aproxima do usual;
- “Batteries included” (pilhas inclusas): Já vem com o necessário para seu funcionamento pronto para uso. O interpretador já possui pré-carregado todos recursos necessários para identificar uma função e seus métodos, assim como os tipos de dados básicos que usaremos e todos seus operadores;
- dinamicamente tipada: Quando trabalhamos com variáveis/objetos (itens aos quais iremos atribuir dados ou valores), podemos trabalhar livremente com qualquer tipo de dado e se necessário, também alterar o tipo de uma variável a qualquer momento.

Para programadores acostumados com linguagens de baixo nivel significa que não precisa incluir bibliotecas, inicializar o ambiente ou declarar variaveis.

### Tipos de dados

Primitivos:
- inteiros(int)
- reais ou ponto flutuante(float)
- strings(str)
- booleano(bool)

Estruturados:
- lista(list)
- tupla
- dicionario(dict)

### Variáveis

Como foi dito python é dinamicamente tipado, atribuímos qualquer dado ou valor a uma variável o tipo de dado é implícito. Além disso Python também é uma linguagem case sensitive, ou seja,
ela diferencia caracteres maiúsculos de minúsculos, logo, existem certas maneiras de declarar variáveis que são permitidas enquanto outras não, gerando conflito com o interpretador.
Assim como as outras linguagens, python tambem exige uma boa conduta no nome das variaveis.

```
x = 7
y = 2.6
```
Como python não é fortemente tipado ela não exige que se declare o tipo de variavel para depois receber um valor. 


```
Numero = 4
numero = 4
```
Numero e numero são duas variaveis do mesmo tipo e com mesmo valor, mas não são a mesma variavel. Isso porque existe um espaço de memoria da variavel Numero e outra para a variavel numero.

```
num_inteiro = 7
numInteiro = 7
```
Assim como no exemplo anterior num_inteiro e numInteiro são variaveis diferentes. 

É muito importante que você crie seu padrão de escrever codigos, seguindo sempre a mesma ideia das outras linguagens. Primeiro que o nome das variaveis façam sentido, variavel com nome composto usar " _ " , se possivel sempre fazer comentarios no código pode usar o # para comentarios de uma linha e ''' '''(três aspas) para comentarios de bloco. Atenção tambem as palavras reservadas, no python são 31 palavras.

Outro ponto interessante é que outras linguagens de programação usam " ; " (ponto e virgula) para marca o fim do comando, Python é uma linguagem de forte indentação, ou seja, para
fácil sintaxe e leitura, suas linhas de código não precisam necessariamente de uma pontuação, mas de uma tabulação correta. Quando linhas/blocos de código são filhos de uma determinada
função ou parâmetro, devemos organizá-los de forma a que sua tabulação siga um determinado padrão. Diferente de outras linguagens de programação que o interpretador percorre cada sentença e busca uma pontuação para demarcar seu fim, em Python o interpretador usa uma indentação para conseguir ver a hierarquia das sentenças.

## Operadores

Os operadores em python funcina como em todos os outros lugares, inclussive como nas demais linguagens.

 - Atribuição (=)

- Aritmeticos:                        

  (+)  soma                                 
  
  (-)  subtração                            
  
  (*)  multiplacação                         
  
  (/)  divisão   

- Especiais de atribuição:

  +=
  
  -=
  
  *=
  
  /=

- Especiais:

  (//) divisão exata
  
  (**) potencia
  
  (%)  resto da divisão

- Operadores Relacionais:

  (>)  maior que

  (<)  menor que

  (=>)  maior ou igual que

  (=<)  menor ou igual que

  (==) comparação

  (!=)  diferente de

- Operadores Logicos:

  and  (e)

  or  (ou)

- Operadores de membro: usando em listas, o resultado é um valor booleano true ou false

  in (pertence)
  
  not in (não pertence)

- Operador de identidade: confirmar se diferentes objetos tem o mesmo dado ou valor atribuído, a sainda é um valor booleano tambem

  is (é)

##  Funções de entrada e saida

- print() : para que um programa possa imprimir um texto.
- input() : para que o seu programa receba um valor digitado pelo usuário.

Impressão de texto:
```
print("Bem Vindo!")
```

Impressao de variavel:
```
x = 2
print(x)
```

Impressão de texto e variavel usando mascaras:
```
dia = 11
mes = 'Agosto'
print(" Dia %d, mes de %s" %(dia, mes))
```

%s para strings, %d para inteiros e %f para float.

Float ainda pode limitar o numero de casa decimais usando o %.f, exemplo:
```
pi = 3.1415
print(" Numero Pi = %.2f" %(pi))
```
Nesse caso sera impresso apenas duas casas decimais apos oponto.

Ainda na função de impressão podemos usar outra mascara .format():
```
dia = 11
mes = 'Agosto'
print(" Dia {0}, mes de {1}".format(dia, mes))
```

Podemos usar tambem uma abreviação do format que é:
```
dia = 11
mes = 'Agosto'
print(f"Dia {dia}, mes de {mes}")
```

Solicitar que o usuario digite o valor a ser atribuido a uma variavel:
```
x = input()
```

Solicitar que o usuario digite o valor de um tipo especifico a uma variavel, no exemplo abaixo 'x' só pode receber valores inteiros:
```
x = int(input())
```
Alem disso pode adicionar uma mensagem para essa solicitação:
```
x = int(input("Digite um numero inteiro: "))
```

## Funções personalizadas

Quando estamos fazendo nossos programas as vezes se faz necessario criar funções, funções personalizadas para uma determinada situação e que não estão disponibilizadas em bibliotecas. 
Basicamente quando necessitamos criar uma função personalizada, ela começará com a declaração de um def, é o meio para que o interpretador assuma que a partir dessa palavra reservada está sendo criada uma função. Assim como as outras linguagens as função personalizada pode ou não receber parâmetros, pode retornar ou não algum dado ou valor ao usuário e por fim, terá um bloco de código indentado para receber suas instruções.

Exemplo:
```
def boas_vindas():
  print("Seja Bem-Vindo!)
```
A função boas_vindas não recebe parametros e não tem retorno.
Para programadores de outras linguagens é estranho notar que apenas a indentação demarca as linhas de codigo da função, que não precisa declarar o tipo de retorno da função, mesmo que ela seja vazia.
```
def soma(x, y):
  return (x+y)
```

uma função de soma simples entre dois numeros. Observamos mais uma vez que no parametro não precisamos declarar os tipos de variaveis que entraram na função.

## Importando bibliotecas

Assim como nas outras linguagens, em python tambem podemos importar bibliotecas. Existem duas formas básicas de trabalharmos com as importações, de forma bastante simples, podemos importar uma biblioteca inteira a referenciando pelo nome após o comando import, ou podemos importar apenas algo de dentro de uma biblioteca externa para incormporarmos em nosso código, através do comando from (nome da biblioteca) import (nome da função).
Por exemplo, podemos importar a biblioteca inteira que contem funções matematicas ou importa apenas uma função dessa biblioteca:

```
import math 
```

ou 

```
from math import pi
```

## Modularização
