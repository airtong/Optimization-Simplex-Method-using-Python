<h1 align='center'>Optimization Simplex Method using Python 🐍</h1>
<p align="left">Repositírio destinado ao trabalho de otimização por método simple utilizando Python.</p>

<div align="center">

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

</div>

# 📜 Passo a passo

<h3> VS Code</h3>
🚨

- Rodar a aplicação na IDE utilizada com o run nativo ou com o comando abaixo:

```
python Simplex.py
```

> A aplicação deve receber como entrada: 📥🚀

- Número de variáveis de decisão. Quantidade de parâmetros analisados;
- Número de restrições. Quantas formas serão analisadas para se ajustar o melhor resultado esperado;
- Coeficientes das variáveis da decisão --> Z no formato: Ax1 + Bx2 + Cx3, deve-se entrar com as variáveis A, B e C;
- Coeficientes das restrições --> Entrar com M, N e O, de cada restrição e Lado Direito (LD);
- Deve-se verificar se o cálculo do Delta será feito e aceito (s/n) na entrada;
- Caso o Delta for calculado, informar o Delta de cada uma das restições;🥏

> A aplicação calculará e informará a saída:📤 🎯

- A função de Maximização (Z): Z = Ax1 + Bx2, por exemplo;
- As funções de restrições em sua forma de função;
- Matriz primária;
- Matrizes secundárias. Caso exista mais de uma, enumeradas;
- Os valores ótimos para cada parâmetro;
- Preço Sombra de cada restrição;
- Se o Delta for calculado, informa o resultado obtido e se é válido; 🧮
- Finalmente, gera o resultado do novo Lucro ótimizado. 💰 💸

## Lib utilizada no projeto 🕋 🗳️

- numpy
