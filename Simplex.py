
#lib
import numpy as np
from utils import *
np.set_printoptions(precision=2,suppress=True)

alfabeto_restricoes = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabeto_variaveis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nVar = 0
nRestricoes = 0
nDelta = [-120,0,240]

# DESCOMENTAR!!!
# nVar = int(input(f"Entre com o numero de variaveis: "))
# nRestricoes = int(input(f"Entre com o numero de restricoes: "))
# TEMPORARIO
nVar = 2
nRestricoes = 3

#DEFININDO MINHAS VARIAVEIS DE DECISÃO
variaveis = alfabeto_variaveis[0:nVar]

#coletando coeficientes das variaveis de decisão
coeficientes_var = []
# DESCOMENTAR!!!
# formula_z = ""
# for i in range(0,nVar):
#     coeficientes_var.append(int(input(f"Entre com o coeficiente de {variaveis[i]}: ")))
#     formula_z += str(coeficientes_var[i])+str(variaveis[i])
#     if i != nVar-1:
#         formula_z += " + "

# TEMPORARIO
coeficientes_var = [12,60]
matriz_dados = (
    [6,30,2160],
    [6,45,1320],
    [6,24,900]
    )

#mostrando Maximize
# print(f'Maximize: Z = {formula_z}')
restricoes = alfabeto_restricoes[0:nRestricoes]
# print(f"Restricoes: {restricoes}")

print("Preenchendo restrições:")
coeficientes_restricoes = define_coeficientes_restricoes(matriz_dados, nRestricoes, nVar, variaveis)
print(f'Coeficientes restricoes: {coeficientes_restricoes}')


#montando matriz
# a matriz deve possuir
matriz_linha = 1 + nRestricoes
matriz_coluna = nVar + nRestricoes + 1

#definindo primeira matriz
matriz = define_matriz_primaria(matriz_linha,matriz_coluna,coeficientes_var,coeficientes_restricoes,variaveis,nVar)

print(matriz)

#MAIN_LOOP
continuar = True
valores_otimos = {}
#definindo nova matriz
while continuar:
    coluna_pivo = define_coluna_pivo(matriz, matriz_linha, matriz_coluna)
    linha_referencia = define_linha_referencia(matriz, matriz_linha, matriz_coluna, coluna_pivo)

    if(len(valores_otimos) < nVar):
        valores_otimos[variaveis[coluna_pivo]] = linha_referencia

    nova_matriz = np.zeros((matriz_linha,matriz_coluna),dtype='float')
    #calculando linha de referencia
    for j in range(0,matriz_coluna):
        nova_matriz[linha_referencia][j] = matriz[linha_referencia][j]/matriz[linha_referencia][coluna_pivo]
    #calculando restante da nova matriz
    for i in range(0,matriz_linha):
        if i != linha_referencia:
            for j in range(0,matriz_coluna):
                nova_matriz[i][j] = matriz[i][j] + (matriz[i][coluna_pivo]*-1)*nova_matriz[linha_referencia][j]
    matriz = nova_matriz

    continuar = False
    for sk in range(0,matriz_coluna):
        if matriz[0][sk] < 0:
            continuar = True
    print(matriz)

'''
- Valores ótimos 
- Lucro Ótimo
- Preço Sombra
- Se Delta >> viável? caso sim: Novo lucro
'''

for k, v in valores_otimos.items():
    valores_otimos[k] = matriz[v][matriz_coluna-1]

valores_otimos['Z'] = matriz[0][matriz_coluna-1]

print("Valores Ótimos: ", sorted(valores_otimos.items()))

# preço sombra
for s in range(nVar,matriz_coluna-1):
    print(f'Preço sombra da restrição {restricoes[s-nVar]} = {matriz[0][s]}')


valido = True
#valida deltas
for x, d in enumerate(restricoes):
    print(f'Delta {restricoes[x]} = {nDelta[x]}')
    linha = x+1
    soma = 0
    indice_delta = 0
    for coluna in range(nVar,matriz_coluna-1):
        soma += nDelta[indice_delta]*matriz[linha][coluna]
        indice_delta += 1
    soma += matriz[linha][matriz_coluna-1]
    print(soma)
    if soma > 0:
        print(f'restrição {restricoes[x]} valida')
    else:
        valido = False

#novo lucro ótimo
if valido:
    linha = 0
    indice_delta = 0
    soma = valores_otimos['Z']
    for coluna in range(nVar,matriz_coluna-1):
        soma += nDelta[indice_delta]*matriz[linha][coluna]
        indice_delta += 1
print(f'Novo lucro ótimo = {soma}')