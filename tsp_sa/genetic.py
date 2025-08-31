"""Algoritmo Genético simples para TSP.

Permutação, torneio, Order Crossover (OX), swap mutation.
"""

import random
from typing import List, Tuple

from .utils import Coordinate, Route, total_distance, random_solution


def tournament_selection(population: List[Route], costs: List[float], k: int = 3) -> Route:
    """Seleciona por torneio e retorna uma cópia do vencedor."""
    best = None
    best_cost = float("inf")
    for _ in range(k):
        i = random.randrange(len(population))
        if costs[i] < best_cost:
            best = population[i]
            best_cost = costs[i]
    return best[:]


def order_crossover(parent1: Route, parent2: Route) -> Route:
    """Order Crossover (OX) robusto para permutações."""
    n = len(parent1)
    a = random.randrange(0, n - 1)
    b = random.randrange(a + 1, n)
    child = [-1] * n
    child[a:b] = parent1[a:b]

    # Preencher as posições vazias na ordem de parent2
    fill_pos = b % n
    for gene in parent2:
        if gene not in child:
            child[fill_pos] = gene
            fill_pos = (fill_pos + 1) % n

    return child


def swap_mutation(route: Route, mutation_rate: float = 0.02) -> Route:
    """Mutação por troca simples; probabilidade por posição."""
    r = route[:]
    n = len(r)
    for i in range(n):
        if random.random() < mutation_rate:
            j = random.randrange(n)
            r[i], r[j] = r[j], r[i]
    return r


def genetic_algorithm(
    coords: List[Coordinate],
    pop_size: int = 100,
    generations: int = 500,
    crossover_rate: float = 0.9,
    mutation_rate: float = 0.02,
    elitism: int = 1,
    seed: int = None,
) -> Tuple[Route, float, dict]:
    """Executa o GA e retorna (best_route, best_cost, info)."""
    if seed is not None:
        random.seed(seed)

    n = len(coords)
    if n == 0:
        return [], 0.0, {"generations": 0}

    population = [random_solution(n) for _ in range(pop_size)]
    costs = [total_distance(p, coords) for p in population]

    best_idx = min(range(pop_size), key=lambda i: costs[i])
    best = population[best_idx][:]
    best_cost = costs[best_idx]

    history = {"best_costs": [], "avg_costs": []}

    for gen in range(generations):
        new_pop = []
        # Elitism: mantém os melhores
        elite_idxs = sorted(range(pop_size), key=lambda i: costs[i])[:elitism]
        for i in elite_idxs:
            new_pop.append(population[i][:])

        while len(new_pop) < pop_size:
            p1 = tournament_selection(population, costs)
            p2 = tournament_selection(population, costs)
            if random.random() < crossover_rate:
                child = order_crossover(p1, p2)
            else:
                child = p1[:]
            child = swap_mutation(child, mutation_rate)
            new_pop.append(child)

        population = new_pop
        costs = [total_distance(p, coords) for p in population]

        # Atualiza melhor
        gen_best_idx = min(range(pop_size), key=lambda i: costs[i])
        gen_best_cost = costs[gen_best_idx]
        if gen_best_cost < best_cost:
            best_cost = gen_best_cost
            best = population[gen_best_idx][:]

        history["best_costs"].append(best_cost)
        history["avg_costs"].append(sum(costs) / len(costs))

    info = {"generations": generations, "best_cost_history_len": len(history["best_costs"]) }
    return best, best_cost, {**info, **history}


if __name__ == '__main__':
    # Exemplo rápido quando executado isoladamente
    import random as _r
    _r.seed(0)
    coords = [(0, 0), (1, 0), (1, 1), (0, 1)]
    best, cost, info = genetic_algorithm(coords, pop_size=30, generations=100, seed=0)
    print("best", best, cost)
