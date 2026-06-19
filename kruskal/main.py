# main.py
# Executa os testes e salva os resultados.

import os
from kruskal import kruskal
from graph_generator import (
    generate_sparse_graph,
    generate_dense_graph,
    generate_geometric_graph
)
from benchmark import (
    benchmark_algorithm,
    benchmark_graph_generation,
    save_results_csv
)

results = [["tipo", "vertices",  "arestas", "tempo_geracao_medio", "tempo_geracao_desvio_padrao", "tempo_execucao_medio", "tempo_execucao_desvio_padrao"]]

sparse_sizes = [100, 500, 1000, 5000, 10000]
print("GRAFOS ESPARSOS")

for vertices in sparse_sizes:
    gen_mean, gen_std = benchmark_graph_generation(generate_sparse_graph, vertices, runs=10)
    edges = generate_sparse_graph(vertices)
    exec_mean, exec_std = benchmark_algorithm(kruskal, vertices, edges, runs=10)
    
    results.append([
        "esparso", vertices, len(edges), gen_mean, gen_std, exec_mean, exec_std
    ])
    
    print(f"V={vertices} | E={len(edges)} | Geração: {gen_mean:.4f}s (DP: {gen_std:.4f}s) | Execução: {exec_mean:.6f}s (DP: {exec_std:.6f}s)")


dense_sizes = [100, 500, 1000]
print("\nGRAFOS DENSOS")

for vertices in dense_sizes:
    gen_mean, gen_std = benchmark_graph_generation(generate_dense_graph, vertices, runs=10)
    edges = generate_dense_graph(vertices)
    exec_mean, exec_std = benchmark_algorithm(kruskal, vertices, edges, runs=10)
    
    results.append([
        "denso", vertices, len(edges), gen_mean, gen_std, exec_mean, exec_std
    ])
    
    print(f"V={vertices} | E={len(edges)} | Geração: {gen_mean:.4f}s (DP: {gen_std:.4f}s) | Execução: {exec_mean:.6f}s (DP: {exec_std:.6f}s)")


geometric_sizes = [100, 500, 1000]
print("\nGRAFOS GEOMÉTRICOS")

for vertices in geometric_sizes:
    gen_mean, gen_std = benchmark_graph_generation(generate_geometric_graph, vertices, runs=10)
    edges = generate_geometric_graph(vertices)
    exec_mean, exec_std = benchmark_algorithm(kruskal, vertices, edges, runs=10)
    
    results.append([
        "geometrico", vertices, len(edges), gen_mean, gen_std, exec_mean, exec_std
    ])
    
    print(f"V={vertices} | E={len(edges)} | Geração: {gen_mean:.4f}s (DP: {gen_std:.4f}s) | Execução: {exec_mean:.6f}s (DP: {exec_std:.6f}s)")


os.makedirs("resultados", exist_ok=True)
save_results_csv("resultados/resultados_kruskal.csv", results)
print("\nArquivo resultados_kruskal.csv criado na pasta 'resultados'.")