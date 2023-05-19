
#lib
import numpy as np

alfabeto = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ALFABETO = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nVar = 0
nRestricoes = 0

# exemplo
nVar = int(input(f"Entre com o numero de variaveis: "))
nRestricoes = int(input(f"Entre com o numero de restricoes: "))

#DEFININDO MINHAS VARIAVEIS DE DECISÃO
variaveis = ALFABETO[0:nVar]

#coletando coeficientes das variaveis de decisão
coeficientes_var = []
formula_z = ""
for i in range(0,nVar):
    coeficientes_var.append(int(input(f"Entre com o coeficiente de {variaveis[i]}: ")))
    formula_z += str(coeficientes_var[i])+str(variaveis[i])
    if i != nVar-1:
        formula_z += " + "

#mostrando Maximize
print(f'Maximize: Z = {formula_z}')


restricoes = alfabeto[0:nRestricoes]

print(f"Restricoes: {restricoes}")


coeficientes_restricoes = []
print("Preenchendo restrições:")
for i in range(0,nRestricoes):
    print(f'Restricao {restricoes[i]}:')
    restri_dict = {}
    for j in range(0,nVar):
        restri_dict[variaveis[j]] = int(input(f"Entre com o valor do coeficiente de {variaveis[j]}: "))
    #entrando com lado direito da restrição
    restri_dict["LD"] = int(input(f"Entre com o valor do lado direito: "))
    coeficientes_restricoes.append(restri_dict)

print(f'Coeficientes restricoes: {coeficientes_restricoes}')


#montando matriz
# a matriz deve possuir
matriz_linha = 1 + nRestricoes
matriz_coluna = nVar + nRestricoes + 1

matriz = np.zeros((matriz_linha,matriz_coluna))
print(matriz)
#loop de linhas
try:
    for i in range(0,matriz_linha):
        #loop de colunas
        for j in range(0,matriz_coluna):
            #definindo linha Z
            if i == 0:
                if j < nVar:
                    matriz[i][j] = coeficientes_var[j] * -1
                else:
                    matriz[i][j] = 0
            #definindo linha restricoes
            else:
                if j < nVar:
                    matriz[i][j] = coeficientes_restricoes[i-1][variaveis[j]]
                elif j == nVar + i - 1:
                    matriz[i][j] = 1
                elif j == matriz_coluna-1:
                    matriz[i][j] = coeficientes_restricoes[i-1]['LD']
                else:
                    matriz[i][j] = 0
except:
    pass
print(matriz)