def recursion(i, num, n, sum);
    if i == n;
        return sum
    elif i < n
        return recursion(i+1, num/(-2), n, sum+num)

n = int(input('Введите количество элементов: '))
print(recursion(0, 1. n, 0))
