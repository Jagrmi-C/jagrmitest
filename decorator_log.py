import logging

def log(func):
    """
    log what function is called
    :param func:
    :return:
    """
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # open file log for record
        fh = logging.FileHandler("{}.log".format(name))
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Call func:{}".format(name))
        result = func(*args, **kwargs)
        logger.info("Result: {}".format(result))
        return func
    return wrap_log


@log
def double_func(a):
    return a*2


if __name__ == '__main':
    value = double_func(2)
