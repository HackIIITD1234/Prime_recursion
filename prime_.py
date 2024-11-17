def prime(n, divisor = 2):
    if n <= 1:
        return "Undefined"
    elif divisor * divisor > n:
        return True
    elif n % divisor == 0:
        return False
    return prime(n, divisor + 1)

print(prime(53))