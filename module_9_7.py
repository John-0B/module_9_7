def is_prime(func):
    def wrapper(*args):
        sum_ = func(*args)
        counter = 0
        for i in range(sum_):
            if i <= 1:
                continue
            if sum_ % i == 0:
                counter += 1
        if counter == 0:
            print('Простое')
        else:
            print('Составное')
        return sum_
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
