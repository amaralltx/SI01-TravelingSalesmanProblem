import random
import argparse
from typing import Optional
from tsp_sa import simulated_annealing, genetic_algorithm


def main(
    # Parâmetros Gerais
    n_cities: int = 25,
    seed: int = 123,
    method: str = 'sa',
    # Parâmetros Têmpera Simulada
    sa_initial_temp: float = 50.0,
    sa_alpha: float = 0.995,
    sa_stopping_temp: float = 1e-3,
    sa_iter_per_temp: int = 200,
    sa_max_iter: int = 20000,
    # Parâmetros Algoritmo Genético
    ga_pop_size: int = 100,
    ga_generations: int = 500,
    ga_crossover_rate: float = 0.8,
    ga_mutation_rate: float = 0.02,
    ga_elitism: int = 1,
    ga_tournament_k: int = 3,
) -> None:
    """Gera cidades aleatórias e executa o método escolhido.

    Parâmetros configuráveis por CLI:
    - para SA: initial_temp, alpha, stopping_temp, iter_per_temp, max_iter
    - para GA: pop_size, generations, crossover_rate, mutation_rate, elitism, tournament_k
    """
    random.seed(seed)
    coords = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n_cities)]

    if method == 'sa':
        print(f"Executando Simulated Annealing (SA) para TSP com {n_cities} cidades (seed={seed})")
        print(f"Parâmetros SA: initial_temp={sa_initial_temp}, alpha={sa_alpha}, stopping_temp={sa_stopping_temp}, iter_per_temp={sa_iter_per_temp}, max_iter={sa_max_iter}")
        best_route, best_cost, info = simulated_annealing(
            coords,
            initial_temp=sa_initial_temp,
            alpha=sa_alpha,
            stopping_temp=sa_stopping_temp,
            iter_per_temp=sa_iter_per_temp,
            max_iter=sa_max_iter,
            seed=seed,
        )
        print(f"Melhor custo encontrado: {best_cost:.4f}")
        print(f"Iterações: {info.get('iterations', info.get('generations'))}, tempo: {info.get('time', 0):.3f}s")
        print(f"Rota (índices): {best_route}")
    elif method == 'ga':
        print(f"Executando Algoritmo Genético (GA) para TSP com {n_cities} cidades (seed={seed})")
        print(f"Parâmetros GA: pop_size={ga_pop_size}, generations={ga_generations}, crossover_rate={ga_crossover_rate}, mutation_rate={ga_mutation_rate}, elitism={ga_elitism}, tournament_k={ga_tournament_k}")
        best_route, best_cost, info = genetic_algorithm(
            coords,
            pop_size=ga_pop_size,
            generations=ga_generations,
            crossover_rate=ga_crossover_rate,
            mutation_rate=ga_mutation_rate,
            elitism=ga_elitism,
            tournament_k=ga_tournament_k,
            seed=seed,
        )
        print(f"Melhor custo encontrado: {best_cost:.4f}")
        print(f"Gerações: {info.get('generations')}, histórico: {info.get('best_cost_history_len')}")
        print(f"Rota (índices): {best_route}")
    else:
        raise ValueError("method deve ser 'sa' ou 'ga'")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Executar SA ou GA para TSP (pacote tsp_sa)")
    parser.add_argument("-n", "--n-cities", type=int, default=25, help="número de cidades (padrão: 25)")
    parser.add_argument("-s", "--seed", type=int, default=123, help="semente RNG (padrão: 123)")
    parser.add_argument("-m", "--method", type=str, choices=["sa", "ga"], default="sa", help="algoritmo: 'sa' (Simulated Annealing) ou 'ga' (Genetic Algorithm)")

    # Parâmetros Têmpera Simulada
    parser.add_argument("--sa-initial-temp", type=float, default=50.0, help="Temperatura inicial para SA (padrão: 50.0)")
    parser.add_argument("--sa-alpha", type=float, default=0.995, help="Fator de resfriamento geométrico para SA (padrão: 0.995)")
    parser.add_argument("--sa-stopping-temp", type=float, default=1e-3, help="Temperatura de parada para SA (padrão: 1e-3)")
    parser.add_argument("--sa-iter-per-temp", type=int, default=200, help="Iterações por temperatura para SA (padrão: 200)")
    parser.add_argument("--sa-max-iter", type=int, default=20000, help="Número máximo de iterações para SA (padrão: 20000)")

    # Parâmetros Algoritmo Genético
    parser.add_argument("--ga-pop-size", type=int, default=100, help="Tamanho da população para GA (padrão: 100)")
    parser.add_argument("--ga-generations", type=int, default=500, help="Número de gerações para GA (padrão: 500)")
    parser.add_argument("--ga-crossover-rate", type=float, default=0.8, help="Taxa de crossover para GA (padrão: 0.8)")
    parser.add_argument("--ga-mutation-rate", type=float, default=0.02, help="Taxa de mutação para GA (padrão: 0.02)")
    parser.add_argument("--ga-elitism", type=int, default=1, help="Número de indivíduos de elite preservados por geração (padrão: 1)")
    parser.add_argument("--ga-tournament-k", type=int, default=3, help="Tamanho do torneio para seleção (padrão: 3)")

    args = parser.parse_args()

    main(
        n_cities=args.n_cities,
        seed=args.seed,
        method=args.method,
        sa_initial_temp=args.sa_initial_temp,
        sa_alpha=args.sa_alpha,
        sa_stopping_temp=args.sa_stopping_temp,
        sa_iter_per_temp=args.sa_iter_per_temp,
        sa_max_iter=args.sa_max_iter,
        ga_pop_size=args.ga_pop_size,
        ga_generations=args.ga_generations,
        ga_crossover_rate=args.ga_crossover_rate,
        ga_mutation_rate=args.ga_mutation_rate,
        ga_elitism=args.ga_elitism,
        ga_tournament_k=args.ga_tournament_k,
    )
