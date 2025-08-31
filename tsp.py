import random
import argparse
from typing import Optional
from tsp_sa import simulated_annealing, genetic_algorithm


def main(
    n_cities: int = 25,
    seed: int = 123,
    method: str = 'sa',
    # SA params
    sa_initial_temp: Optional[float] = None,
    sa_alpha: float = 0.995,
    sa_stopping_temp: float = 1e-3,
    sa_iter_per_temp: int = 200,
    sa_max_iter: int = 20000,
    # GA params
    ga_pop_size: int = 100,
    ga_generations: int = 500,
    ga_crossover_rate: float = 0.8,
    ga_mutation_rate: float = 0.02,
    ga_elitism: int = 1,
    ga_tournament_k: int = 3,
) -> None:
    """Gera cidades aleatórias e executa o método escolhido (sa|ga).

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

    # SA params
    parser.add_argument("--sa-initial-temp", type=float, default=None, help="Temperatura inicial para SA (default: estimada automaticamente)")
    parser.add_argument("--sa-alpha", type=float, default=0.995, help="Fator de resfriamento geométrico para SA (default: 0.995)")
    parser.add_argument("--sa-stopping-temp", type=float, default=1e-3, help="Temperatura de parada para SA (default: 1e-3)")
    parser.add_argument("--sa-iter-per-temp", type=int, default=200, help="Iterações por temperatura para SA (default: 200)")
    parser.add_argument("--sa-max-iter", type=int, default=20000, help="Número máximo de iterações para SA (default: 20000)")

    # GA params
    parser.add_argument("--ga-pop-size", type=int, default=100, help="Tamanho da população para GA (default: 100)")
    parser.add_argument("--ga-generations", type=int, default=500, help="Número de gerações para GA (default: 500)")
    parser.add_argument("--ga-crossover-rate", type=float, default=0.8, help="Taxa de crossover para GA (default: 0.8)")
    parser.add_argument("--ga-mutation-rate", type=float, default=0.02, help="Taxa de mutação para GA (default: 0.02)")
    parser.add_argument("--ga-elitism", type=int, default=1, help="Número de indivíduos de elite preservados por geração (default: 1)")
    parser.add_argument("--ga-tournament-k", type=int, default=3, help="Tamanho do torneio para seleção (default: 3)")

    args = parser.parse_args()
    # Enforce explicit initial temp for SA
    if args.method == 'sa' and args.sa_initial_temp is None:
        parser.error("--sa-initial-temp is required when --method sa (automatic estimation removed)")

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
