# benchmark.py
# Contém:
# medição de tempo
# média
# desvio padrão

import time
import statistics
import csv


def save_results_csv(filename, results):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for row in results:
            writer.writerow(row)

def benchmark_algorithm(func, *args, runs=10):
    execution_times = []

    for _ in range(runs):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        execution_times.append(end - start)

    mean_time = statistics.mean(execution_times)
    std_dev = statistics.stdev(execution_times)
    return mean_time, std_dev

def benchmark_graph_generation(generator, *args, runs=10):
    times = []

    for _ in range(runs):
        start = time.perf_counter()
        generator(*args)
        end = time.perf_counter()
        times.append(end - start)

    return (
        statistics.mean(times),
        statistics.stdev(times)
    )