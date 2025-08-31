"""Utilitários mínimos para TSP.

Contém funções de distância, avaliação de rota e operadores de vizinhança.
Todos os itens usam apenas a biblioteca padrão.
"""

import math
import random
from typing import List, Tuple

Coordinate = Tuple[float, float]
Route = List[int]


def euclidean_distance(a: Coordinate, b: Coordinate) -> float:
    """Retorna a distância Euclidiana entre dois pontos (x, y)."""
    return math.hypot(a[0] - b[0], a[1] - b[1])


def total_distance(route: Route, coords: List[Coordinate]) -> float:
    """Calcula o custo total de uma rota (ciclo que retorna ao início)."""
    dist = 0.0
    n = len(route)
    for i in range(n):
        a = coords[route[i]]
        b = coords[route[(i + 1) % n]]
        dist += euclidean_distance(a, b)
    return dist


def two_opt_swap(route: Route, i: int, k: int) -> Route:
    """Opera 2-opt: retorna uma nova rota com segmento [i..k] invertido."""
    return route[:i] + list(reversed(route[i:k + 1])) + route[k + 1:]


def random_solution(n: int) -> Route:
    """Gera uma permutação aleatória de n índices (rota inicial)."""
    route = list(range(n))
    random.shuffle(route)
    return route
