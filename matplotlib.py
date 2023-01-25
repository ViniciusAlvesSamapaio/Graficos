import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (22, 7) # determina a altura e largura do grafico 

d = pd.read_csv('titanic_train.csv') # importa o arquivo csv 

plt.plot(d.Age,)
plt.xlabel('Passageiros', size = 16) # coloca uma informação do lado do grafico 'passageiro' e o tamanho da informação 'size = 16'
plt.ylabel('Idades', size = 16)
d.Age.plot()
plt.show() # apresenta o gráfico 

plt.scatter(d.PassengerId, d.Age, color='r') # apresenta um outro tipo de grafico
plt.show()

#histogramas

print(d.Age.describe())

d.Age.hist()
plt.xlabel('Idades', size = 16)
plt.ylabel('Frequência', size = 16)
plt.savefig('grafico.png') #vai salvar o grafico com um png
plt.show()

