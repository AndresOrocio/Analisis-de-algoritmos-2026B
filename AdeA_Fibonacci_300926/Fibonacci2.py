def fibonacci_dp(n):
    """
    Fibonacci mediante programacion dinamica (bottom-up).
    Complejidad temporal: O(N)
    Complejidad espacial: O(N)
    """
    if n <= 1:
        return n

    F = [0] * (n + 1)

    F[0] = 0
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]


if __name__ == "__main__":
    n = 10
    print(fibonacci_dp(n))
