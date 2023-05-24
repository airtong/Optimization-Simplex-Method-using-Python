from pulp import *

# Criação do problema
prob = LpProblem("Problema de Otimizacao", LpMaximize)

# Definição das variáveis de decisão
L = LpVariable("L", lowBound=0)
V = LpVariable("V", lowBound=0)
U = LpVariable("U", lowBound=0)

# Definição da função objetivo
prob += 4*L + 5*V + 1*U

# Definição das restrições
prob += 2*L + 3*V <= 10
prob += 4*L + V <= 11
prob += 3*L + 3*V + U <= 13

# Resolvendo o problema
prob.solve()

# Impressão da função objetivo
print("Função objetivo: " + str(prob.objective))

# Exportação do modelo para um arquivo LP
prob.writeLP("problema.lp")

# Exibindo a solução ótima
print("Solução ótima:")
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Exibindo o preço sombra
print("\nPreço sombra:")
for name, c in prob.constraints.items():
    print(name, ":", c.pi)

# Exibindo as possíveis variações
print("\nPossíveis variações:")
for name, c in prob.constraints.items():
    print(name, ":", c.slack)

# Imprimindo a solução
print("\nLucro ótimo:", value(prob.objective))


# Impressão das possíveis variações
print("\nPossíveis variações:")
for name, c in prob.constraints.items():
    slack = c.slack
    pi = c.pi
    if slack >= 0:
        print(name, "pode ser aumentada em até", slack, "unidades")
    else:
        print(name, "já está ativa")
    print("Preço sombra:", pi)
    print()