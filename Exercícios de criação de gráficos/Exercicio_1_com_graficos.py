# =================================================== DESAFIO 1 ========================================================================
# Criar um gráfico simples completo.
# Importar matplotlib.pyplot como plt.
# Criar uma figura com figsize (8,4) e dpi 120.
# Criar duas listas:
# x = [0,1,2,3,4,5]
# y = [0,1,4,9,16,25]
# Plotar a curva com:
# - cor azul
# - linha contínua
# - marcador círculo
# - markersize igual a 6
# Adicionar título "Função Quadrática" com:
# - fontsize 14
# - fontweight 'bold'
# Adicionar xlabel "Valores de X"
# Adicionar ylabel "Valores de Y"
# Ativar grid com:
# - linestyle pontilhado
# - alpha 0.6
# Mostrar o gráfico.

import matplotlib.pyplot as plt

#Valores de entrada
x = [0,1,2,3,4,5]
y = [0,1,4,9,16,25]

#Área de plotagem do gráfico
plt.figure(figsize=(8,4),dpi=120,facecolor='white')

#Título e nomes dos eixos
plt.title('Função Quadrática',fontsize=14,fontweight='bold')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')

#Utilização do GRID
plt.grid(True,linestyle='dotted',alpha=0.6)

#Plotando os pontos nos gráficos
plt.plot(x,y,linestyle='-',color='blue',marker = 'o',markersize = 6)

#Mostrando o gráfico
plt.show()

#Liberando a memória
plt.close()