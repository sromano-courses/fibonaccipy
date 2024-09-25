class Fibonacci:

    def calculate(self, n):
        if n < 0 or n > 92:
            raise ValueError
        if n == 0 or n == 1:
            return n
        fib0 = 0
        fib1 = 1
        for i in range(n - 1):
            fib2 = fib1 + fib0
            fib0 = fib1
            fib1 = fib2
        return fib2

