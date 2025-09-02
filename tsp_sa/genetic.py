"""Algoritmo Genético para TSP."""

import random
from typing import List, Tuple, Dict

from .utils import distancia_total, random_solution


def torneio_selecao(populacao: List[List[int]], custos: List[float], k: int) -> List[int]:
    """Seleciona um indivíduo por torneio de tamanho k."""
    selecionados = random.sample(range(len(populacao)), k)
    selecionado = min(selecionados, key=lambda i: custos[i])
    return populacao[selecionado][:]


def cruzamento_ox(pai1: List[int], pai2: List[int]) -> Tuple[List[int], List[int]]:
    """Order Crossover (OX). Retorna dois filhos."""
    n = len(pai1)
    a, b = sorted(random.sample(range(n), 2))

    def ox(p_a, p_b):
        filho = [-1] * n
        # copia o segmento do pai A
        filho[a : b + 1] = p_a[a : b + 1]
        # preenche com a ordem do pai B
        pos = (b + 1) % n
        for gene in p_b[b + 1 :] + p_b[: b + 1]:
            if gene not in filho:
                filho[pos] = gene
                pos = (pos + 1) % n
        return filho

    return ox(pai1, pai2), ox(pai2, pai1)


def mutacao_swap(individuo: List[int], taxa_mutacao: float) -> None:
    """Aplica mutação por swap no indivíduo in-place com probabilidade taxa_mutacao por par."""
    n = len(individuo)
    for i in range(n):
        if random.random() < taxa_mutacao:
            j = random.randrange(n)
            individuo[i], individuo[j] = individuo[j], individuo[i]


def avaliar_populacao(populacao: List[List[int]], coords) -> List[float]:
    return [distancia_total(ind, coords) for ind in populacao]


def genetic_algorithm(
    coords,
    tamanho_populacao: int = 100,
    geracoes: int = 500,
    taxa_crossover: float = 0.9,
    taxa_mutacao: float = 0.02,
    elitismo: int = 1,
    torneio_k: int = 3,
    semente: int | None = None,
) -> Tuple[List[int], float, Dict]:
    """Executa o algoritmo genético e retorna o melhor indivíduo encontrado.

    Parâmetros:
    - coords: lista de coordenadas (x,y) das cidades (mesmo formato que utils espera)
    - tamanho_populacao: tamanho da população
    - geracoes: número de gerações a evoluir
    - taxa_crossover: probabilidade de aplicar cruzamento
    - taxa_mutacao: probabilidade de mutação por gene
    - elitismo: quantos melhores passam diretamente para a próxima geração
    - torneio_k: tamanho do torneio para seleção
    - semente: semente opcional para reprodutibilidade
    """
    if semente is not None:
        random.seed(semente)

    n_cidades = len(coords)
    # inicializa população com permutações aleatórias
    populacao = [random_solution(n_cidades) for _ in range(tamanho_populacao)]
    custos = avaliar_populacao(populacao, coords)

    melhor_idx = min(range(len(custos)), key=lambda i: custos[i])
    melhor_individuo = populacao[melhor_idx][:]
    melhor_custo = custos[melhor_idx]

    historico_melhor_custo = [melhor_custo]

    for gen in range(1, geracoes + 1):
        nova_populacao: List[List[int]] = []

        # elitismo: copia os N melhores
        ordenados = sorted(zip(populacao, custos), key=lambda pc: pc[1])
        for i in range(min(elitismo, len(ordenados))):
            nova_populacao.append(ordenados[i][0][:])

        # gera novos individuos
        while len(nova_populacao) < tamanho_populacao:
            # seleção
            pai1 = torneio_selecao(populacao, custos, torneio_k)
            pai2 = torneio_selecao(populacao, custos, torneio_k)

            # cruzamento
            if random.random() < taxa_crossover:
                filho1, filho2 = cruzamento_ox(pai1, pai2)
            else:
                filho1, filho2 = pai1[:], pai2[:]

            # mutação
            mutacao_swap(filho1, taxa_mutacao)
            mutacao_swap(filho2, taxa_mutacao)

            nova_populacao.append(filho1)
            if len(nova_populacao) < tamanho_populacao:
                nova_populacao.append(filho2)

        populacao = nova_populacao
        custos = avaliar_populacao(populacao, coords)

        # atualiza melhor
        idx = min(range(len(custos)), key=lambda i: custos[i])
        if custos[idx] < melhor_custo:
            melhor_custo = custos[idx]
            melhor_individuo = populacao[idx][:]

        historico_melhor_custo.append(melhor_custo)

    info = {"geracoes": geracoes, "historico_melhor_custo": historico_melhor_custo}
    return melhor_individuo, melhor_custo, info
