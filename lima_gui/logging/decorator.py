from loguru import logger
import functools


def log_method_call(func, cls_name):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"{cls_name}.{func.__name__} args={args[1:]}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper


def all_methods_logger(cls):
    original_methods = set(dir(cls.__bases__[0]))  # Assuming B is the first base class
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and attr_name not in original_methods:
            original_method = getattr(cls, attr_name)
            setattr(cls, attr_name, log_method_call(original_method, cls.__name__))
    return cls