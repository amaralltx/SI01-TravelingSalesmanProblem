## Tutorial

Execute o script `tsp.py` a partir da raiz do repositório.

Exemplo completo (SA) — usa todos os parâmetros SA e gerais:

```powershell
python tsp.py -n 30 -s 0 -m sa --sa-temperatura-inicial 100.0 --sa-alpha 0.995 --sa-temperatura-parada 0.001 --sa-iter-por-temperatura 200 --sa-iteracoes-max 20000
```

Exemplo completo (GA) — usa todos os parâmetros GA e gerais:

```powershell
python tsp.py -n 30 -s 0 -m ga --ga-tamanho-populacao 100 --ga-geracoes 500 --ga-taxa-crossover 0.8 --ga-taxa-mutacao 0.02 --ga-elitismo 1 --ga-torneio-k 3
```

## Parâmetros CLI

Parâmetros gerais:
-- `-n`, `--n-cidades` (int, padrão: 25) — número de cidades (a serem geradas aleatoriamente no quadrado [0,100]^2)
-- `-s`, `--semente` (int, padrão: 123) — semente do RNG
-- `-m`, `--metodo` (sa|ga, padrão: sa) — algoritmo a executar

Parâmetros de Simulated Annealing (SA):
-- `--sa-temperatura-inicial` (float, padrão: 50) — temperatura inicial 
-- `--sa-alpha` (float, padrão: 0.995) — fator de resfriamento geométrico
-- `--sa-temperatura-parada` (float, padrão: 1e-3) — temperatura de parada
-- `--sa-iter-por-temperatura` (int, padrão: 200) — iterações por nível de temperatura
-- `--sa-iteracoes-max` (int, padrão: 20000) — limite de iterações total

Parâmetros do Genetic Algorithm (GA):
-- `--ga-tamanho-populacao` (int, padrão: 100) — tamanho da população
-- `--ga-geracoes` (int, padrão: 500) — número de gerações
-- `--ga-taxa-crossover` (float, padrão: 0.8) — probabilidade de aplicar crossover
-- `--ga-taxa-mutacao` (float, padrão: 0.02) — taxa de mutação
-- `--ga-elitismo` (int, padrão: 1) — quantos indivíduos de elite preservar por geração
-- `--ga-torneio-k` (int, padrão: 3) — tamanho do torneio para seleção

```
