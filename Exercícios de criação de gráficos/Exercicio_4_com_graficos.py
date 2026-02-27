# =================================================== DESAFIO 4 ========================================================================
# Trabalhar com lista contendo valores repetidos no eixo x.
# Criar:
# x = [1,1,2,3,4,4,5,6,6]
# y = [10,15,20,25,30,35,40,45,50]
# Remover valores repetidos de x usando set() e sorted().
# Usar esses valores únicos no eixo x com:
# - fontsize 8
# - rotation 45 graus
# - fontweight 'bold'
# Plotar os dados normalmente.
# Ativar grid com linestyle '-.'
# Aplicar autoscale apenas no eixo y.
# Mostrar gráfico.

import matplotlib.pyplot as plt

#Valores de entrada
x = [1,1,2,3,4,4,5,6,6]
y = [10,15,20,25,30,35,40,45,50]

#Eliminando os valores repetidos e deixando em ordem crescente
k = sorted(set(x))

#Gerando a área que estará o gráfico
plt.figure(figsize=(8,5),dpi=120,facecolor='white')

#Nomeando os eixos e definindo o título
plt.title('Lista contendo valores repetidos no eixo x',loc = 'center',fontsize=15,fontweight='bold')
plt.xlabel('Valores do eixo x', fontsize=8,fontweight='light',rotation=0)
plt.ylabel('Valores do eixo y', fontsize=8,fontweight='light',rotation=90)

#Definindos os valores que aparecerão no eixos
plt.xticks(k,fontsize=8,rotation=45,fontweight='bold')
plt.yticks(y,fontsize=8,rotation=45,fontweight='bold')

#Ativação do GRID
plt.grid(True,linestyle='-.',linewidth=0.5,alpha=0.7)

#Plotando valores no gráfico
plt.plot(x,y,color='blue',linestyle='-',marker='o',markerfacecolor='red',label='Curva 1')

#Ativando legenda
plt.legend()

#Ajustes finais de dimensões do gráfico
plt.autoscale(enable=True,axis='y',tight=True)
plt.tight_layout(pad=3)

#Gerando gráfico
plt.show()

#Liberando memória
plt.close()
