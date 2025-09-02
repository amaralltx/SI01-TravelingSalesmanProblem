import math
import random
import time
from typing import List, Tuple

from .utils import Coordenada, Rota, distancia_total, random_solution, two_opt_swap


def probabilidade_aceitacao(delta: float, temperatura: float) -> float:
    """Probabilidade de aceitar uma solução pior."""
    if delta <= 0:
        return 1.0
    return math.exp(-delta / temperatura)


def simulated_annealing(
    coords: List[Coordenada],
    temperatura_inicial: 50,
    alpha: float = 0.995,
    temperatura_parada: float = 1e-3,
    iter_por_temperatura: int = 100,
    iteracoes_max: int = 100000,
    seed: int = 123,
) -> Tuple[Rota, float, dict]:
    if seed is not None:
        random.seed(seed)

    n = len(coords)
    if n == 0:
        return [], 0.0, {"iteracoes": 0}

    atual = random_solution(n)
    custo_atual = distancia_total(atual, coords)
    melhor = atual[:]
    melhor_custo = custo_atual

    temperatura = float(temperatura_inicial)

    iteracoes = 0
    sem_melhoria = 0
    inicio = time.time()
    history = {"historico_melhor_custo": [], "temperaturas": []}

    while temperatura > temperatura_parada and iteracoes < iteracoes_max:
        # Para cada iteração na temperatura atual
        for _ in range(iter_por_temperatura):
            # Gera um vizinho usando 2-opt
            i = random.randrange(0, n - 1)
            k = random.randrange(i + 1, n)
            vizinho = two_opt_swap(atual, i, k)
            custo_vizinho = distancia_total(vizinho, coords)
            delta = custo_vizinho - custo_atual

            # Se a nova solução for melhor ou for aceita aleatoriamente, adote a solução
            if delta < 0 or random.random() < probabilidade_aceitacao(delta, temperatura):
                atual = vizinho
                custo_atual = custo_vizinho
                if custo_atual < melhor_custo:
                    melhor = atual[:]
                    melhor_custo = custo_atual
                    sem_melhoria = 0
                else:
                    sem_melhoria += 1
            else:
                sem_melhoria += 1

            iteracoes += 1
            if iteracoes >= iteracoes_max:
                break

        # fim do nível de temperatura: registre histórico
        history["historico_melhor_custo"].append(melhor_custo)
        history["temperaturas"].append(temperatura)

        # Verifica parada por estagnação
        if sem_melhoria > 5000:
            break

        # Resfriamento
        temperatura *= alpha

    # Registro de informações
    elapsed = time.time() - inicio
    info = {"iteracoes": iteracoes, "tempo": elapsed, "tamanho_historico_melhor_custo": len(history["historico_melhor_custo"]) }
    return melhor, melhor_custo, {**info, **history}
