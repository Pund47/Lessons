import math

def is_prime(func):
    def chek_prime(*args):
        res_1 = func(*args)
        if res_1 <= 1:
           return False
        for i in range(2, int(math.sqrt(res_1)) + 1):
            if res_1 % i == 0:
                 print('Составное')
        print('Простое')
        return res_1
    return chek_prime

@is_prime
def sum_three(*args):
    my_result =0
    for i in args:
        my_result += i
    return my_result

result = sum_three(2, 3, 6)
print(result)