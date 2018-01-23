import time


def is_prime(number):
    """
    Check if the number is a simple
    :param number:
    :return:
    """
    if number == 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
        else:
            return True


def list_primes():
    """
    To search for prime numbers I use Sieve Eratosthenes
    Create collection with n items. From 0 to 99999. n = 99999 + 1
    :return: lst - list for prime numbers
    """
    n = 99999 + 1
    a = [0] * n
    for i in range(n):
        a[i] = i

    #  Create list for prime numbers
    lst = []
    # 1 is not simple number.
    a[1] = 0

    # First simple number is 2
    m = 2

    while m < n:
        if a[m] != 0:
            j = m + m
            if m > 9999:
                lst.append(a[m])
            while j < n:
                a[j] = 0
                j += m
        m += 1
    return lst


def is_palindrome(n):
    """
    Check if the number is a palindrome
    :param n:
    :return:
    """
    str_n = str(n)
    return str_n == str_n[::-1]


def output_answer(lst_pr):
    lst_pr.reverse()
    max_number = 0
    r = dict()
    r[max_number] = ()
    for num_1 in lst_pr:
        for num_2 in lst_pr:
            product = num_1 * num_2
            if product > max_number and is_palindrome(product):
                max_number = product
                r[max_number] = (num_1, num_2)
    greatest_number = max(r.keys())
    return greatest_number, r[greatest_number]


# def list_primes(number_start, number_end):
#     for i in range(number_start, number_end + 1, 2):
#         if i % 10 == 5:
#             continue

if __name__ == "__main__":
    start = time.time()
    # Get a ;ist of prime numbers
    list_output = list_primes()
    print(time.time() - start)
    # list_output.append(12)
    # Checking the list for correctness
    for i in list_output:
        if not is_prime(i):
            print(f"{i} - is not simple numbers")
            break

    # print(list_output)

    biggest_polindrom = output_answer(list_output)
    # polindrom = output_answer([33211, 30109])
    print(biggest_polindrom)
    print(time.time() - start)