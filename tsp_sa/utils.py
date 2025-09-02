"""Utilitários mínimos para TSP.

Contém funções de distância, avaliação de rota e operadores de vizinhança.
Todos os itens usam apenas a biblioteca padrão.
"""

import math
import random
from typing import List, Tuple

Coordenada = Tuple[float, float]
Rota = List[int]


def distancia_euclidiana(a: Coordenada, b: Coordenada) -> float:
    """Retorna a distância Euclidiana entre dois pontos (x, y)."""
    return math.hypot(a[0] - b[0], a[1] - b[1])


def distancia_total(route: Rota, coords: List[Coordenada]) -> float:
    """Calcula o custo total de uma rota (ciclo que retorna ao início)."""
    dist = 0.0
    n = len(route)
    for i in range(n):
        a = coords[route[i]]
        b = coords[route[(i + 1) % n]]
        dist += distancia_euclidiana(a, b)
    return dist


def two_opt_swap(route: Rota, i: int, k: int) -> Rota:
    """Opera 2-opt: retorna uma nova rota com segmento [i..k] invertido."""
    return route[:i] + list(reversed(route[i:k + 1])) + route[k + 1:]


def random_solution(n: int) -> Rota:
    """Gera uma permutação aleatória de n índices (rota inicial)."""
    route = list(range(n))
    random.shuffle(route)
    return route
