# main.py
# Executa os testes e salva os resultados.

import os
from prim import prim
from graph_generator import (
    gerar_grafo_esparso,
    gerar_grafo_denso,
    gerar_grafo_geometrico
)
from benchmark import (
    benchmark_algoritmo,
    benchmark_geracao_grafo,
    salvar_resultados_csv
)

resultados = [["tipo", "vertices",  "arestas", "tempo_geracao_medio", "tempo_geracao_desvio_padrao", "tempo_execucao_medio", "tempo_execucao_desvio_padrao"]]

tamanhos_esparsos = [100, 500, 1000, 5000, 10000]
print("GRAFOS ESPARSOS")

for vertices in tamanhos_esparsos:
    gen_medio, gen_desvio = benchmark_geracao_grafo(gerar_grafo_esparso, vertices, execucoes=10)
    arestas = gerar_grafo_esparso(vertices)
    exec_medio, exec_desvio = benchmark_algoritmo(prim, vertices, arestas, execucoes=10)
    
    resultados.append([
        "esparso", vertices, len(arestas), gen_medio, gen_desvio, exec_medio, exec_desvio
    ])
    
    print(f"V={vertices} | E={len(arestas)} | Geração: {gen_medio:.4f}s (DP: {gen_desvio:.4f}s) | Execução: {exec_medio:.6f}s (DP: {exec_desvio:.6f}s)")


tamanhos_densos = [100, 500, 1000]
print("\nGRAFOS DENSOS")

for vertices in tamanhos_densos:
    gen_medio, gen_desvio = benchmark_geracao_grafo(gerar_grafo_denso, vertices, execucoes=10)
    arestas = gerar_grafo_denso(vertices)
    exec_medio, exec_desvio = benchmark_algoritmo(prim, vertices, arestas, execucoes=10)
    
    resultados.append([
        "denso", vertices, len(arestas), gen_medio, gen_desvio, exec_medio, exec_desvio
    ])
    
    print(f"V={vertices} | E={len(arestas)} | Geração: {gen_medio:.4f}s (DP: {gen_desvio:.4f}s) | Execução: {exec_medio:.6f}s (DP: {exec_desvio:.6f}s)")


tamanhos_geometricos = [100, 500, 1000]
print("\nGRAFOS GEOMÉTRICOS")

for vertices in tamanhos_geometricos:
    gen_medio, gen_desvio = benchmark_geracao_grafo(gerar_grafo_geometrico, vertices, execucoes=10)
    arestas = gerar_grafo_geometrico(vertices)
    exec_medio, exec_desvio = benchmark_algoritmo(prim, vertices, arestas, execucoes=10)
    
    resultados.append([
        "geometrico", vertices, len(arestas), gen_medio, gen_desvio, exec_medio, exec_desvio
    ])
    
    print(f"V={vertices} | E={len(arestas)} | Geração: {gen_medio:.4f}s (DP: {gen_desvio:.4f}s) | Execução: {exec_medio:.6f}s (DP: {exec_desvio:.6f}s)")


os.makedirs("resultados", exist_ok=True)
salvar_resultados_csv("resultados/resultados_prim.csv", resultados)
print("\nArquivo resultados_prim.csv criado na pasta 'resultados'.")