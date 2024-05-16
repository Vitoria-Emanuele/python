# Python

A primeira linguagem de programação que tive contato foi python, normalmente é a primeira linguagem que a maioria dos estudantes de programação tem contato pela sua facilidade de compreensão e por outros tantos motivos. Com o passar do tempo deixei de programar em python e me dediquei a linguagens de baixo nivel como C e C++.
Programar é como andar de bicicleta, você nunca esquece, mas perde a pratica. Então para retornar de forma mais eficiente, além de apenas fazer vários programas por dia resolvi escrever tudo que considero importante. 

##### Referencia: Python do zero à programação orientada a objetos, por Fernando Feltrin. https://www.amazon.com.br/Python-ZERO-Programa%C3%A7%C3%A3o-Orientada-Objetos-ebook/dp/B07P2VJVW5
Não tenho certeza se este livro é uma boa escolha para quem está começando a programar. Talvez seja mais apropriado um livro que introduza primeiro os conceitos de algoritmos e, em seguida, a linguagem de programação. Acredito também que este livro é bastante conciso, indo direto ao conteúdo, o que facilita para quem já programa, mas pode ser complicado para quem não está familiarizado com os conceitos básicos de programação.


## Introdução

Python é uma linguagem de :
- Alto nivel: Usa expressões em inglês e uma sintaxe fácil que se aproxima do usual;
- “Batteries included” (pilhas inclusas): Já vem com o necessário para seu funcionamento pronto para uso. O interpretador já possui pré-carregado todos recursos necessários para identificar uma função e seus métodos, assim como os tipos de dados básicos que usaremos e todos seus operadores;
- dinamicamente tipada: Quando trabalhamos com variáveis/objetos (itens aos quais iremos atribuir dados ou valores), podemos trabalhar livremente com qualquer tipo de dado e se necessário, também alterar o tipo de uma variável a qualquer momento.

Para programadores acostumados com linguagens de baixo nivel significa que não precisa incluir bibliotecas, inicializar o ambiente ou declarar variaveis.

### 1. Tipos de dados

Primitivos:
- inteiros(int)
- reais ou ponto flutuante(float)
- strings(str)
- booleano(bool)

Estruturados:
- lista(list)
- tupla
- dicionario(dict)

### 2. Variáveis

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

## 3. Operadores

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

###  4. Funções de entrada e saida

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

### 5. Estruturas de Controle de Fluxo

#### Condicionais:

- if (se)
- elif (mas se)
- else (se não)

A lógica de execução dos condicionais sempre se dará dessa forma, o interpretador estará executando o código linha por linha até que ele encontrará uma das palavras reservadas(if, elif ou else) que sinaliza que naquele ponto existe uma tomada de decisão, de acordo com a decisão que o usuário indicar, ou de acordo com a validação de algum parâmetro, o código executará uma instrução, ou não executará nada, ignorando esta condição e pulando para o bloco de código seguinte.

O exemplo que eu vou usar é um programa que define se o numero é impar ou par:
```
x = int(input())
if (x%2 == 0):
 print("%d eh par"%(x))
else:
 print("%d eh impar" %(x))
```

na 1° linha você atribui a x um valor inteiro, na 2° linha o programa verifica se o resto da divisão de x por 2 é 0 em caso de ser verdade o codigo indentado na função é executado. Caso seja falso pula da 2° para a 3° linha o seu codigo indentado é executado e o programa é encerrado. Observe que o else só é executado caso o if seja false.

Quando usamos if, elif e else a primeira condição é verificada, se o if for falso é verificado a condição do elif, o else só é executado caso as duas ou mais condições anteriores sejam falsas. 

Você tambem pode usar os condicionais dentro dos condicionais.

#### Repetição:

- while (enquanto)

A logica do condicional while é enquanto uma determinada condição for válida, a ação continuará sendo repetida. Normalemente usamos quando não sabemos quantas vezes o programa vai ser rodado. Por exemplo:

```
x = int(input())

while x > 0 :
    x -= 1
    print(x)
```
Esse programa vai imprimir os numeros entre o numero que voce digitou e 0. Como eu não sei qual numero o usuario vai digitar eu uso o while.

- for

for é um laço de repetição usado onde conhecemos o limite da repetição. Esse laço de repetição é muito usado para interagir com variaveis estruturadas, como listas e dicionarios. Outro uso bastante comum do for é quando sabemos o tamanho de um determinado intervalo, o número de elementos de uma lista, etc... e usamos seu método in range para que seja explorado todo esse intervalo.

Um observação legal que é diferente das outras linguagens de programação em Python o laço for pode nativamente trabalhar como uma espécie de condicional, sendo assim podemos usar o comando else para incluir novas instruções no mesmo.

```
lista = []
qnt = int(input("Digite a quantidade de elementos que deseja adicionar à lista: "))
for i in range(qnt):
    elemento = input("Digite um elemento para adicionar à lista: ")
    lista.append(elemento)
```

Esse codigo utiliza o for para adicionar elementos a uma lista. Essa lista tem tamanho definido pelo usuario. 

```
lista = []
qnt = int(input("Digite a quantidade de elementos que deseja adicionar à lista: "))
for i in range(qnt):
    elemento = input("Digite um elemento para adicionar à lista: ")
    lista.append(elemento)
for elemento in lista:
    print(elemento)
```

Adicionei um outro trecho de codigo com um for que percorre a lista imprimindo elemento a elemento. Fique a vontade para brincar com essa estrutura.


### 6. Funções para tipos de dados especificos

#### Strings:

Algumas funções de manipulaçao de strings:
- .lower() : minusculo
- .upper() : maiscula
- split() : desmembra uma string em palavras separadas, essas palavras vão para dentro de uma lista. 

- Pode usar o 'in' para procurar um dado dentro de um texto.
- Alteração de cor das palavras

![image](https://github.com/Vitoria-Emanuele/python/assets/86628310/6810d9ed-bf00-4974-b835-5f1c36c8b40f)

```
fonte = '\033[91m' #código de cores “vermelho”
fundo = '\033[0m'
print(fonte + 'Mensagem de erro' + fundo)
```
você usa o codigo da fonte e do fundo juntos.

- Posição para exibir texto
  
  center( ) - centralizar
  
  ljust( ) - alinhar à esquerda

  rjust( ) - alinhar à direita

#### Lista:

Uma lista será um objeto que permite guardar diversos dados dentro dele, de forma organizada e indexada. Por isso é chamada variavel estruturada. 
As funções que usamos para interagir com as listas:
- append - adiciona elementos a lista
- remove() - remove elementos da lista
- del lista[num do indice]- Para deletarmos o conteúdo de um índice específico
- .index() - Para verificarmos em que posição da lista está um determinado elemento
- Pode usar o 'in' para verificar se um elemento pertence a lista

### 7. Funções personalizadas

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

### 8. Importando bibliotecas

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

## Programação Orientada a Objetos
