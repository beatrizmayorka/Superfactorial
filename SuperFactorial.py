import Factorial
import math         # Fornece acesso às funções matemáticas definidas pelo padrão C
import psutil       # Biblioteca para acessar os detalhes do sistema. Exemplo: CPU, memória, discos, rede e sensores
import timeit       # Biblioteca para encontrar o tempo de execução de partes do código
import SP

start = timeit.default_timer()
n = 4
sup = 1
for i in range(n + 1):
    sup = sup * math.factorial(i)

print('O super fatorial de', n, 'é:', sup)
finish = timeit.default_timer()

print('Tempo de execução:  %f' % (finish - start))
print('O uso da CPU é: ', psutil.cpu_percent(4))
print('% De memória RAM usada:', psutil.virtual_memory()[2])