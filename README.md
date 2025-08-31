## Como rodar

Use Python 3.8+ e execute o script `tsp.py` a partir da raiz do repositório.

Exemplo mínimo (SA):

```powershell
python tsp.py -n 30 -s 0 -m sa --sa-initial-temp 100.0
```

Exemplo GA:

```powershell
python tsp.py -n 30 -s 0 -m ga --ga-pop-size 100 --ga-generations 500
```

## Parâmetros CLI

Parâmetros gerais:
- `-n`, `--n-cities` (int, default: 25) — número de cidades (a serem geradas aleatoriamente no quadrado [0,100]^2)
- `-s`, `--seed` (int, default: 123) — semente do RNG (reprodutibilidade)
- `-m`, `--method` (sa|ga, default: sa) — algoritmo a executar

Parâmetros de Simulated Annealing (SA):
- `--sa-initial-temp` (float, required quando `--method sa`) — temperatura inicial (a estimativa automática foi removida para reprodutibilidade)
- `--sa-alpha` (float, default: 0.995) — fator de resfriamento geométrico (T <- alpha * T)
- `--sa-stopping-temp` (float, default: 1e-3) — temperatura de parada
- `--sa-iter-per-temp` (int, default: 200) — iterações por nível de temperatura
- `--sa-max-iter` (int, default: 20000) — limite de iterações total

Parâmetros do Genetic Algorithm (GA):
- `--ga-pop-size` (int, default: 100) — tamanho da população
- `--ga-generations` (int, default: 500) — número de gerações
- `--ga-crossover-rate` (float, default: 0.8) — probabilidade de aplicar crossover
- `--ga-mutation-rate` (float, default: 0.02) — taxa de mutação (por gene/posição)
- `--ga-elitism` (int, default: 1) — quantos indivíduos de elite preservar por geração
- `--ga-tournament-k` (int, default: 3) — tamanho do torneio para seleção

> Nota: o wrapper exige `--sa-initial-temp` quando `--method sa` — caso contrário o parser falha com mensagem de erro.

```