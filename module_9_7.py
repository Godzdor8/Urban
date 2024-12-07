def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        if res <= 1:
            print('Числа меньше или равные 1 не являются простыми')
            return res
        for i in range(2, res // 2 + 1):
            if res % i == 0:
                print("Составное")
                return res
        print("Простое")
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(-26, 3, 6)
print(result)