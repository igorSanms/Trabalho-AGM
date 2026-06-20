# benchmark.py
# Contém:
# medição de tempo
# média
# desvio padrão

import time
import statistics
import csv


def salvar_resultados_csv(nome_arquivo, resultados):
    with open(nome_arquivo, "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        for linha in resultados:
            writer.writerow(linha)

def benchmark_algoritmo(func, *args, execucoes=10):
    tempos_execucao = []

    for _ in range(execucoes):
        inicio = time.perf_counter()
        func(*args)
        fim = time.perf_counter()
        tempos_execucao.append(fim - inicio)

    tempo_medio = statistics.mean(tempos_execucao)
    desvio_padrao = statistics.stdev(tempos_execucao)
    return tempo_medio, desvio_padrao

def benchmark_geracao_grafo(gerador, *args, execucoes=10):
    tempos = []

    for _ in range(execucoes):
        inicio = time.perf_counter()
        gerador(*args)
        fim = time.perf_counter()
        tempos.append(fim - inicio)

    return (
        statistics.mean(tempos),
        statistics.stdev(tempos)
    )