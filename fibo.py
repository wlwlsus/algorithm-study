def fibo(n):
    cache = [-1 for _ in range(n+1)]

    def iterate(n):
        if n < 2:
	        return n

        if cache[n] != -1:
	        return cache[n]

        cache[n] = iterate(n-1) + iterate(n-2)
        return cache[n]

    return iterate(n)
    
print(fibo(100))