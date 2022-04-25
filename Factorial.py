import math
import psutil
import timeit

start = timeit.default_timer()

def factorial(n):
    return (math.factorial(n))
n = 4
f = factorial(n)
print('O fatorial de', n, 'é', f)

finish = timeit.default_timer()
print('Tempo de execução:  %f' % (finish - start))
print('O uso da CPU é: ', psutil.cpu_percent(4))
print('% De memória RAM usada:', psutil.virtual_memory()[2])
print('-----------------------------------------')