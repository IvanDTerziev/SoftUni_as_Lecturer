# която чете число n, въведено от потребителя
n = int(input())

# отпечатва всички числа  ≤  n от редицата: 1, 3, 7, 15, 31,
k = 1
while k <= n:
    print(k)
    # умножим предишното с 2 и добавим 1.
    k = k * 2 + 1
