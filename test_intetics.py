# python 3.6.3
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
    a = [i for i in range(n)]

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
    factor_1 = 0
    factor_2 = 0

    for num_1 in lst_pr:
        for num_2 in lst_pr:
            res = num_1 * num_2
            if res > max_number and is_palindrome(res):
                max_number = res
                factor_1 = num_1
                factor_2 = num_2
    return max_number, factor_1, factor_2


if __name__ == "__main__":
    start = time.time()
    # Get a list of prime numbers
    list_output = list_primes()
    # print(list_output)
    print(f"Time to get the list: {time.time() - start} s.")
    # Checking the list for correctness
    d = [i for i in list_output if not is_prime(i)]
    if d:
        print(f"{d} - list not prime numbers if they are.")

    the_largest_palindrome = output_answer(list_output)
    answer = f"The largest palindrome is {the_largest_palindrome[0]}. Factors are " \
             f"{the_largest_palindrome[1]} and {the_largest_palindrome[2]}."

    # Cheking the function output_answer()
    # palindrome = output_answer([33211, 30109])
    print(answer)
    print(f"Time to get the answer: {time.time() - start} s.")
