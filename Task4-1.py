def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):  # فحص القسمة فقط حتى الجذر التربيعي
        if number % i == 0:
            return False
    return True

    
is_prime(9)

