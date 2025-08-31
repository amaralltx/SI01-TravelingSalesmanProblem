## Tutorial

Execute o script `tsp.py` a partir da raiz do repositório.

Exemplo completo (SA) — usa todos os parâmetros SA e gerais:

```powershell
python tsp.py \
	-n 30 \
	-s 0 \
	-m sa \
	--sa-initial-temp 100.0 \
	--sa-alpha 0.995 \
	--sa-stopping-temp 0.001 \
	--sa-iter-per-temp 200 \
	--sa-max-iter 20000
```

Exemplo completo (GA) — usa todos os parâmetros GA e gerais:

```powershell
python tsp.py \
	-n 30 \
	-s 0 \
	-m ga \
	--ga-pop-size 100 \
	--ga-generations 500 \
	--ga-crossover-rate 0.8 \
	--ga-mutation-rate 0.02 \
	--ga-elitism 1 \
	--ga-tournament-k 3
```

## Parâmetros CLI

Parâmetros gerais:
- `-n`, `--n-cities` (int, padrão: 25) — número de cidades (a serem geradas aleatoriamente no quadrado [0,100]^2)
- `-s`, `--seed` (int, padrão: 123) — semente do RNG (reprodutibilidade)
- `-m`, `--method` (sa|ga, padrão: sa) — algoritmo a executar

Parâmetros de Simulated Annealing (SA):
- `--sa-initial-temp` (float, padrão: 50) — temperatura inicial 
- `--sa-alpha` (float, padrão: 0.995) — fator de resfriamento geométrico
- `--sa-stopping-temp` (float, padrão: 1e-3) — temperatura de parada
- `--sa-iter-per-temp` (int, padrão: 200) — iterações por nível de temperatura
- `--sa-max-iter` (int, padrão: 20000) — limite de iterações total

Parâmetros do Genetic Algorithm (GA):
- `--ga-pop-size` (int, padrão: 100) — tamanho da população
- `--ga-generations` (int, padrão: 500) — número de gerações
- `--ga-crossover-rate` (float, padrão: 0.8) — probabilidade de aplicar crossover
- `--ga-mutation-rate` (float, padrão: 0.02) — taxa de mutação
- `--ga-elitism` (int, padrão: 1) — quantos indivíduos de elite preservar por geração
- `--ga-tournament-k` (int, padrão: 3) — tamanho do torneio para seleção

```
