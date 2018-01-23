def another_function(func):
    """
    function that takes itself
    """

    def other_func():
        val = "Result from {} - this {}".format(func(), eval(func()))
        return val
    return other_func

@another_function
def s_func():
    """
    Simple function
    :return:
    """
    return '1+1'


if __name__ == "__main__":
    value = s_func()
    print(value)
