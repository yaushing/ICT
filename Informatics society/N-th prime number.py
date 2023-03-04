def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def nth_prime(n):
    prime_count = 0
    candidate = 2
    while prime_count < n:
        if is_prime(candidate):
            prime_count += 1
        candidate += 1
    return candidate - 1
print(nth_prime(int(input("N: "))))