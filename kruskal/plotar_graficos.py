# plotar_graficos.py
import csv
import matplotlib.pyplot as plt

def carregar_dados(nome_arquivo):
    dados = {'esparso': {'x': [], 'y': [], 'erro': []},
             'denso': {'x': [], 'y': [], 'erro': []},
             'geometrico': {'x': [], 'y': [], 'erro': []}}
    
    with open(nome_arquivo, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for linha in reader:
            if not linha:
                continue
            
            tipo = linha[0]
            vertices = int(linha[1])
            tempo_exec_medio = float(linha[5])
            tempo_exec_dp = float(linha[6])
            
            if tipo in dados:
                dados[tipo]['x'].append(vertices)
                dados[tipo]['y'].append(tempo_exec_medio)
                dados[tipo]['erro'].append(tempo_exec_dp)
                
    return dados

def gerar_grafico(tipo, x, y, erro, cor, titulo):
    plt.figure(figsize=(8, 6))
    plt.errorbar(x, y, yerr=erro, fmt='-o', color=cor, capsize=5, capthick=2, ecolor='black')   
    plt.title(titulo, fontsize=14)
    plt.xlabel("Tamanho da Instância (Número de Vértices)", fontsize=12)
    plt.ylabel("Tempo de Execução (segundos)", fontsize=12)   
    plt.grid(True, linestyle='--', alpha=0.7)
    
    nome_imagem = f"resultados/grafico_kruskal_{tipo}.png"
    plt.savefig(nome_imagem, dpi=300, bbox_inches='tight')
    print(f"Gráfico salvo: {nome_imagem}")
    plt.close()

if __name__ == "__main__":
    dados = carregar_dados("resultados/resultados_kruskal.csv")
    gerar_grafico('esparso', dados['esparso']['x'], dados['esparso']['y'], dados['esparso']['erro'], 'blue', 'Desempenho Kruskal - Grafos Esparsos')
    gerar_grafico('denso', dados['denso']['x'], dados['denso']['y'], dados['denso']['erro'], 'red', 'Desempenho Kruskal - Grafos Densos')
    gerar_grafico('geometrico', dados['geometrico']['x'], dados['geometrico']['y'], dados['geometrico']['erro'], 'green', 'Desempenho Kruskal - Grafos Geométricos')  
    print("\nTodos os gráficos foram gerados")