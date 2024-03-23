"""Timer functions
"""
import time

def timer(func):
    """Timer decorator
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"exec of {func.__name__} in {execution_time:.2f} seconds")
        return result
    return wrapper