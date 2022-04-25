import psutil
import timeit

start = timeit.default_timer()

def superfactorial(n):
    val = 1
    ans = []

    for i in range(1, n + 1):
        val = val * i
        ans.append(val)

    arr = [1]
    for i in range(1, len(ans)):
        arr.append((arr[-1] * ans[i]))

    return arr

    n = 4
    arr = superfactorial(n)

finish = timeit.default_timer()

print('O super fatorial de ', n, 'é:', arr[-1])
print('Tempo de execução:  %f' % (finish - start))
print('O uso da CPU é: ', psutil.cpu_percent(4))
print('% De memória RAM usada:', psutil.virtual_memory()[2])
print('-----------------------------------------')