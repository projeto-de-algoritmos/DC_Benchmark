# DC_Benchmark

**Número da Dupla**: 6<br>
**Conteúdo da Disciplina**: Divide&Conquer<br>

## Alunos

|Matrícula | Aluno |
| -- | -- |
| 18/0037439  |  Sérgio de Almeida Cipriano Júnior |
| 18/0030264  |  Antonio Igor Carvalho |

## Sobre 

A ideia é de criar um repositório com benchmark de algoritmos categorizados como
dividir e conquistar, desse modo, é possível fazer comparações baseado na
solução de cada problema. Todos os algoritmos serão implementados na mesma
linguagem para evitar discrepâncias de performance enviesadas.

## Screenshots

![screenshot](https://user-images.githubusercontent.com/78360676/114326149-b9d9c600-9b09-11eb-87ae-495a5ff522d2.png)

## Instalação 

**Linguagem**: Python3<br>
**Ferramentas**: Docker, docker-compose<br>

É necessário ter um computador com docker instalado, tudo será virtualizado. Com
isso, basta clonar o repositório e executar os comandos de execução mostrados na
sessão de uso.

## Uso 

A criação do grafo de chamadas para visualizar as etapas de execução de cada
algoritmos é feita usando Docker e docker-compose. Desse modo, basta executar:

```
$ docker-compose up
```

Na primeira vez é necessário realizar o build, isso pode ser feito executando:

```
$ docker-compose up --build
```

Com a execução desse comando será mostrado no terminal os algoritmos com o seus
respectivos tempos

## Uso alternativo

Para utilizar o programa desta forma é necessário apenas o python3. Com o python3
instalado utilize o comando abaixo no diretorio do projeto:

```
$ python3 benchmark.py
```

