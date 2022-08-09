from multiprocessing import Pool, current_process, cpu_count
from time import time


def worker(number):
    result = []
    for num in range(1, number + 1):
        if number % num == 0:
            result.append(num)
    return result


def factorize_simple(*number, func=worker):
    result = []
    for num in number:
        result.append(func(num))
    return result


def factorize_pool(*number, func=worker):
    with Pool(cpu_count()) as pool:
        result = pool.map(func, number)
        return result


def assert_factorize(a, b, c, d):
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]


if __name__ == '__main__':
    stime = time()
    a, b, c, d = factorize_simple(128, 255, 99999, 10651060)
    print(f'Simple:  {time() - stime} sec')

    assert_factorize(a, b, c, d)

    stime = time()
    a, b, c, d = factorize_pool(128, 255, 99999, 10651060)
    print(f'Pool:  {time() - stime} sec')

    assert_factorize(a, b, c, d)
