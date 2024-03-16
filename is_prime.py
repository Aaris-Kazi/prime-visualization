def is_prime_number(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    elif n <= 3:
        return True  # 2 and 3 are prime numbers
    elif n % 2 == 0 or n % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # If divisible by current number or current number + 2, not prime
        i += 6  # Increment by 6 (optimization for checking primes)
    
    return True 