def fibonacci(n):
    """
    Fibonacci mediante recursividad, sin programacion dinamica.
    Complejidad temporal aproximada: O(2^N)
    Complejidad espacial por la pila de recursion: O(N)
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = 10
    print(fibonacci(n))
