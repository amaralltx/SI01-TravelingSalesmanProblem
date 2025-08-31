"""Simulated Annealing (SA) para o TSP.

Interface mínima: chame `simulated_annealing(coords, initial_temp=..., alpha=..., ...)`
e obtenha (best_route, best_cost, info).
"""

import math
import random
import time
from typing import List, Tuple

from .utils import Coordinate, Route, total_distance, random_solution, two_opt_swap


def acceptance_probability(delta: float, temperature: float) -> float:
    """Probabilidade de aceitar uma solução pior (Metropolis)."""
    if delta <= 0:
        return 1.0
    return math.exp(-delta / temperature)


def simulated_annealing(
    coords: List[Coordinate],
    initial_temp: float,
    alpha: float = 0.995,
    stopping_temp: float = 1e-3,
    iter_per_temp: int = 100,
    max_iter: int = 100000,
    seed: int = None,
) -> Tuple[Route, float, dict]:
    """Executa SA.

    initial_temp é obrigatório (a estimativa automática foi removida).
    Retorna (rota_melhor, custo, info) com info contendo tempo e histórico simplificado.
    """
    if seed is not None:
        random.seed(seed)

    n = len(coords)
    if n == 0:
        return [], 0.0, {"iterations": 0}

    current = random_solution(n)
    current_cost = total_distance(current, coords)
    best = current[:]
    best_cost = current_cost

    T = float(initial_temp)

    it = 0
    no_improve = 0
    start_time = time.time()
    history = {"best_costs": [], "temps": []}

    while T > stopping_temp and it < max_iter:
        for _ in range(iter_per_temp):
            i = random.randrange(0, n - 1)
            k = random.randrange(i + 1, n)
            neighbor = two_opt_swap(current, i, k)
            neighbor_cost = total_distance(neighbor, coords)
            delta = neighbor_cost - current_cost

            if delta < 0 or random.random() < acceptance_probability(delta, T):
                current = neighbor
                current_cost = neighbor_cost
                if current_cost < best_cost:
                    best = current[:]
                    best_cost = current_cost
                    no_improve = 0
                else:
                    no_improve += 1
            else:
                no_improve += 1

            it += 1
            if it >= max_iter:
                break

        history["best_costs"].append(best_cost)
        history["temps"].append(T)

        if no_improve > 5000:
            break

        T *= alpha

    elapsed = time.time() - start_time
    info = {"iterations": it, "time": elapsed, "best_cost_history_len": len(history["best_costs"]) }
    return best, best_cost, {**info, **history}
