# Trabalho Prático: Árvore Geradora Mínima (AGM) — Kruskal e Prim

Este repositório contém a implementação computacional e análise experimental de dois algoritmos clássicos para o problema da **Árvore Geradora Mínima (MST)**, desenvolvida como parte da Avaliação Parcial 3 da disciplina de **Algoritmos em Grafos** no curso de Ciência da Computação da **Universidade Federal do Ceará (UFC) - Campus Crateús**, sob docência do Professor Rafael Martins Barros.

O objetivo principal do projeto é analisar empiricamente o comportamento dos algoritmos de Kruskal e Prim em diferentes cenários de entrada (grafos esparsos, densos e estruturados geometricamente), respeitando a restrição de utilizar apenas as bibliotecas padrão da linguagem para a lógica estrutural.

---

## Autores

* **Igor Santana** — *Implementação do Algoritmo de Kruskal, Geração de Grafos, Benchmark e Infraestrutura*
* **Ismael Ferreira** — *Implementação do Algoritmo de Prim, ...*

---

## Estrutura do Repositório

Para garantir a organização e o isolamento das execuções, o projeto foi dividido em duas pastas principais, uma para cada algoritmo. Os resultados de tempo e as imagens geradas são armazenados em subpastas dedicadas dentro de cada diretório.

/
├── kruskal/                      # Implementação do Algoritmo de Kruskal (Seu Nome)
│   ├── resultados/               # Pasta gerada automaticamente com CSVs e gráficos .png
│   ├── main.py                   # Script de automação e execução em lote dos testes
│   ├── kruskal.py                # Lógica do Kruskal e estrutura Union-Find
│   ├── graph_generator.py        # Gerador de grafos (Esparsos, Densos, Geométricos)
│   ├── benchmark.py              # Funções de cronometragem e estatísticas
│   └── plotar_graficos.py        # Leitura do CSV e geração dos gráficos (Matplotlib)
│
└── prim/                         # Implementação do Algoritmo de Prim ([Nome do Parceiro])
    ├── resultados/               # [Pasta para os CSVs e gráficos do Prim]
    ├── main.py                   # [Script de automação do Prim]
    ├── prim.py                   # [Lógica do algoritmo de Prim]
    ├── graph_generator.py        # [Gerador de grafos]
    ├── benchmark.py              # [Funções de cronometragem]
    └── plotar_graficos.py        # [Geração dos gráficos]

---

## Como Executar o Projeto

O projeto foi construído em **Python** utilizando exclusivamente pacotes nativos da linguagem para a lógica dos algoritmos de grafos. A única dependência externa utilizada é a biblioteca `matplotlib`, estritamente com o fim de gerar as visualizações gráficas.

Os testes devem ser executados individualmente, navegando para dentro da pasta de cada algoritmo.

### 1. Executando o Kruskal

A partir da raiz do repositório, abra o seu terminal e navegue até a pasta do Kruskal:

```powershell
cd kruskal
```
### 1.1 Crie e ative o ambiente virtual
```powershell
python -m venv venv
venv\Scripts\activate
```
### 1.2 Instale a dependência de plotagem
```powershell
pip install matplotlib
```
### 1.3 Execute o script main
```powershell
python main.py
```
### 1.4 Execute o script gerador de gráficos
```powershell
python plotar_graficos.py
```


