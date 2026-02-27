# =================================================== DESAFIO 5 ========================================================================
# Criar um gráfico com aparência profissional.
# Criar figure com:
# - figsize (10,6)
# - facecolor 'lightgray'
# - dpi 150
# Criar duas curvas quaisquer.
# Cada curva deve ter:
# - cor diferente
# - linewidth diferente
# - alpha diferente
# Adicionar título com:
# - fontstyle 'italic'
# - fontweight 'bold'
# - fontsize 16
# - loc 'left'
# Adicionar xlabel com fontsize 12.
# Adicionar ylabel com fontsize 12.
# Ativar grid com:
# - linestyle '--'
# - linewidth 0.5
# - alpha 0.8
# Salvar o gráfico como "meu_grafico.png".
# Mostrar o gráfico.
# Fechar a figura após exibir.


import matplotlib.pyplot as plt
from random import randint as rd

#Valores de entrada

x = []
y = []
z = []
k = [] #Lista de valores juntos y e z, para filtrar repetição

for i in range(0,11):
    j = rd(0,10)
    x.append(j)
    j = rd(0,10)
    y.append(j)
    j = rd(0,10)
    z.append(j)

i = 0

for i in y:
    k.append(i)

i = 0

for i in z:
    k.append(i)

print(k)

#Gerando a região de criação de gráficos
plt.figure(figsize=(10,6),dpi=150,facecolor='lightgray')

#Definindo nomeações
plt.title('Gráfico com aparência profissional',loc = 'left',fontsize=16,fontweight='bold',fontstyle='italic')
plt.xlabel('Valores para o eixo x',loc='right',fontweight='light',fontsize=12)
plt.ylabel('Valores para o eixo y',loc='top',fontweight='light',fontsize=12,rotation=90)

#Valores aparentes nos eixos
plt.xticks(sorted(set(x)))
plt.yticks(sorted(set(k)))

#Ativação do GRID
plt.grid(True,linestyle='--',linewidth=0.5,alpha=0.8)

#Plotando valores no gráfico
plt.plot(x,y,label='Curva 1',color='blue',linestyle='-',marker='o',markerfacecolor='blue',alpha=0.8,linewidth=0.5)
plt.plot(x,z,label='Curva 2', color='red',linestyle='-',marker='x',markerfacecolor='red',alpha=0.5,linewidth=1)

#Ativando legenda
plt.legend()

#Salvando gráfico
plt.savefig('meu_grafico.png')

#Gerando gráfico
plt.show()

#Liberando memória
plt.close()