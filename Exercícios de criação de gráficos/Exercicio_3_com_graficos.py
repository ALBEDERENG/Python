# =================================================== DESAFIO 3 ========================================================================
# Criar gráfico com duas curvas e legenda.
# Criar:
# x = lista de 0 até 10
# y1 = x ao quadrado
# y2 = x ao cubo
# Plotar curva 1 com:
# - cor verde
# - linestyle '--'
# - marker 'o'
# - label "x²"
# Plotar curva 2 com:
# - cor vermelha
# - linestyle '-.'
# - marker 's'
# - label "x³"
# Adicionar legenda.
# Ativar grid com linha tracejada.
# Adicionar título centralizado.
# Mostrar gráfico.

import matplotlib.pyplot as plt

#Valores de entrada
x = []
y1 = []
y2 = []

for i in range(0,10):
    x.append(i)
    y1.append(i**2)
    y2.append(i**3)


#Área de criação do gráfico
plt.figure(figsize=(8,5),dpi=120)

#Título e nome dos eixos
plt.title('Gráfico com duas curvas e legenda',loc='center',fontsize=15,fontweight='bold')
plt.xlabel('Valores do eixo x',loc = 'right',fontweight='light',fontsize='10')
plt.ylabel('Valores do eixo y',loc = 'top',fontweight='light',fontsize='10')

#Ativação das grades
plt.grid(True,linestyle='--',linewidth=0.5,alpha=0.7)

#Plotando os pontos e criando as curvas
plt.plot(x,y1,linestyle='--',marker='o',color='green',label='x²')
plt.plot(x,y2,linestyle='-.',marker='s',color='red',label='x³')

#Ativação da legenda
plt.legend()

#Gerando gráfico
plt.show()

#Liberando a memória
plt.close()
