import sys


def f(num_steps):
    for i in range(num_steps):
        num_cages = i + 1
        gaps = num_steps - num_cages
        res = "{}{}".format(gaps*"", num_cages*'#')
        print(res)


if __name__ == '__main__':
    f(int(sys.argv[1]))
