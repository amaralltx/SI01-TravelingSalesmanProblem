import random
import argparse
from typing import Optional
from tsp_sa import simulated_annealing, genetic_algorithm


def main(
    # Parâmetros Gerais Iniciais
    n_cidades: int = 25,
    semente: int = 123,
    metodo: str = 'sa',
    # Parâmetros Têmpera Simulada
    sa_temperatura_inicial: float = 50.0,
    sa_alpha: float = 0.995,
    sa_temperatura_parada: float = 1e-3,
    sa_iter_por_temperatura: int = 200,
    sa_iteracoes_max: int = 20000,
    # Parâmetros Algoritmo Genético
    ga_tamanho_populacao: int = 100,
    ga_geracoes: int = 500,
    ga_taxa_crossover: float = 0.8,
    ga_taxa_mutacao: float = 0.02,
    ga_elitismo: int = 1,
    ga_torneio_k: int = 3,
) -> None:
    """Gera cidades aleatórias e executa o método escolhido.

    Parâmetros configuráveis por CLI:
    - para SA: initial_temp, alpha, stopping_temp, iter_per_temp, max_iter
    - para GA: pop_size, generations, crossover_rate, mutation_rate, elitism, tournament_k
    """
    random.seed(semente)
    coords = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n_cidades)]

    if metodo == 'sa':
        print(f"Executando Simulated Annealing (SA) para TSP com {n_cidades} cidades (semente={semente})")
        print(
            f"Parâmetros SA: temperatura_inicial={sa_temperatura_inicial}, alpha={sa_alpha}, temperatura_parada={sa_temperatura_parada}, iter_por_temperatura={sa_iter_por_temperatura}, iteracoes_max={sa_iteracoes_max}"
        )
        best_route, best_cost, info = simulated_annealing(
            coords,
            temperatura_inicial=sa_temperatura_inicial,
            alpha=sa_alpha,
            temperatura_parada=sa_temperatura_parada,
            iter_por_temperatura=sa_iter_por_temperatura,
            iteracoes_max=sa_iteracoes_max,
            seed=semente,
        )
        print(f"Melhor custo encontrado: {best_cost:.4f}")
        print(f"Iterações: {info.get('iteracoes', info.get('geracoes'))}, tempo: {info.get('tempo', 0):.3f}s")
        print(f"Rota (índices): {best_route}")
    elif metodo == 'ga':
        print(f"Executando Algoritmo Genético (GA) para TSP com {n_cidades} cidades (semente={semente})")
        print(
            f"Parâmetros GA: tamanho_populacao={ga_tamanho_populacao}, geracoes={ga_geracoes}, taxa_crossover={ga_taxa_crossover}, taxa_mutacao={ga_taxa_mutacao}, elitismo={ga_elitismo}, torneio_k={ga_torneio_k}"
        )
        best_route, best_cost, info = genetic_algorithm(
            coords,
            tamanho_populacao=ga_tamanho_populacao,
            geracoes=ga_geracoes,
            taxa_crossover=ga_taxa_crossover,
            taxa_mutacao=ga_taxa_mutacao,
            elitismo=ga_elitismo,
            torneio_k=ga_torneio_k,
            semente=semente,
        )
        print(f"Melhor custo encontrado: {best_cost:.4f}")
        print(f"Gerações: {info.get('geracoes')}, histórico: {len(info.get('historico_melhor_custo', []))}")
        print(f"Rota (índices): {best_route}")
    else:
        raise ValueError("metodo deve ser 'sa' ou 'ga'")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Executar SA ou GA para TSP (pacote tsp_sa)")
    parser.add_argument("-n", "--n-cidades", type=int, default=25, help="número de cidades (padrão: 25)")
    parser.add_argument("-s", "--semente", type=int, default=123, help="semente RNG (padrão: 123)")
    parser.add_argument("-m", "--metodo", type=str, choices=["sa", "ga"], default="sa", help="algoritmo: 'sa' (Simulated Annealing) ou 'ga' (Algoritmo Genético)")

    # Parâmetros Têmpera Simulada (nomes em português)
    parser.add_argument("--sa-temperatura-inicial", type=float, default=50.0, help="Temperatura inicial para SA (padrão: 50.0)")
    parser.add_argument("--sa-alpha", type=float, default=0.995, help="Fator de resfriamento geométrico para SA (padrão: 0.995)")
    parser.add_argument("--sa-temperatura-parada", type=float, default=1e-3, help="Temperatura de parada para SA (padrão: 1e-3)")
    parser.add_argument("--sa-iter-por-temperatura", type=int, default=200, help="Iterações por temperatura para SA (padrão: 200)")
    parser.add_argument("--sa-iteracoes-max", type=int, default=20000, help="Número máximo de iterações para SA (padrão: 20000)")

    # Parâmetros Algoritmo Genético (nomes em português)
    parser.add_argument("--ga-tamanho-populacao", type=int, default=100, help="Tamanho da população para GA (padrão: 100)")
    parser.add_argument("--ga-geracoes", type=int, default=500, help="Número de gerações para GA (padrão: 500)")
    parser.add_argument("--ga-taxa-crossover", type=float, default=0.8, help="Taxa de crossover para GA (padrão: 0.8)")
    parser.add_argument("--ga-taxa-mutacao", type=float, default=0.02, help="Taxa de mutação para GA (padrão: 0.02)")
    parser.add_argument("--ga-elitismo", type=int, default=1, help="Número de indivíduos de elite preservados por geração (padrão: 1)")
    parser.add_argument("--ga-torneio-k", type=int, default=3, help="Tamanho do torneio para seleção (padrão: 3)")

    args = parser.parse_args()

    main(
        n_cidades=args.n_cidades,
        semente=args.semente,
        metodo=args.metodo,
        sa_temperatura_inicial=args.sa_temperatura_inicial,
        sa_alpha=args.sa_alpha,
        sa_temperatura_parada=args.sa_temperatura_parada,
        sa_iter_por_temperatura=args.sa_iter_por_temperatura,
        sa_iteracoes_max=args.sa_iteracoes_max,
        ga_tamanho_populacao=args.ga_tamanho_populacao,
        ga_geracoes=args.ga_geracoes,
        ga_taxa_crossover=args.ga_taxa_crossover,
        ga_taxa_mutacao=args.ga_taxa_mutacao,
        ga_elitismo=args.ga_elitismo,
        ga_torneio_k=args.ga_torneio_k,
    )
