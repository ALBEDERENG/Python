# =================================================== DESAFIO 2 ========================================================================
# Criar um gráfico com controle manual dos eixos.
# Gerar:
# x = lista de 0 até 20
# y = x multiplicado por 3
# Definir limites:
# - xlim de 0 até 20
# - ylim de 0 até 70
# Configurar xticks para aparecer de 5 em 5.
# Configurar yticks para aparecer de 10 em 10.
# Adicionar título rotacionado 15 graus.
# Usar tight_layout com pad igual a 2.
# Mostrar o gráfico.

import matplotlib.pyplot as plt

#Área que ficará o gráfico
plt.figure(figsize=(8,5),dpi=120,facecolor='white')


#Entrada dos dados
x = []
y = []

for i in range(0,21,1):
    x.append(i)
    y.append(3*i)

#Título e nomeações dos eixos
plt.title('Gráfico com controle manual dos eixos',fontsize=15,fontweight='bold',loc='center',rotation=15)
plt.xlabel('Eixo x',fontsize=10,fontweight='light',loc='right')
plt.ylabel('Eixo y',fontsize=10,fontweight='light',loc='top',rotation=90)

#Configuração dos limites dos eixos do gráfico
plt.xlim(0,20)
plt.ylim(0,70)

#Valores que serão aparentes nos eixos
plt.xticks(range(0,21,5))
plt.yticks(range(0,71,10))

#Ajuste de posição do gráfico em relação a janela
plt.tight_layout(pad=2)

#Plotando os valores
plt.plot(x,y,linestyle='--',marker='o',markerfacecolor='black',color = 'green',label='Curva da questão 2')

#Ativando legenda
plt.legend()

#Apresentando gráfico
plt.show()

#Limpando a memória
plt.close()
