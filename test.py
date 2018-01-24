def another_function(func):
    """
    Function that causes itself
    """

    def other_func():
        val = "Result for %s this %s" % (func(), eval(func()))

        return val

    return other_func


@another_function
def a_function():
    """Simple function"""
    return "1+1"


if __name__ == "__main__":
    value = a_function()
    print(value)
