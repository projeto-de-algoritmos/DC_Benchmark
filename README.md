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

Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação 

**Linguagem**: Python3<br>
**Framework**: (caso exista)<br>
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

Com a execução desse comando será gerado uma imagem com o nome de `pycallgraph.png`.
Abra ela para visualizar o grafo de chamadas. Para abrir pelo terminal basta
executar:

```
$ xdg-open pycallgraph.png 
```

## Outros 

Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.

