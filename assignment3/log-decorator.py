import functools
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pos_params = list(args) if args else "none"
        kw_params = kwargs if kwargs else "none"
        result = func(*args, **kwargs)

        log_entry = (
            f"function: {func.__name__}\n"
            f"positional parameters: {pos_params}\n"
            f"keyword parameters: {kw_params}\n"
            f"return: {result}"
        )
        logger.log(logging.INFO, log_entry)
        return result

    return wrapper


@logger_decorator
def greet():
    print("Hello, World!")


@logger_decorator
def sum_all(*args):
    return True


@logger_decorator
def process_kwargs(**kwargs):
    return logger_decorator


greet()
sum_all(1, 2, 3)
process_kwargs(a=1, b=2)

