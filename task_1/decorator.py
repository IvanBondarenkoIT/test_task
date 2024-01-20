import time
import logging


def retry_on_exception(exceptions, max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            err: Exception
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except tuple(exceptions) as e:
                    attempts += 1
                    logging.warning(
                        f"Attempt {attempts}/{max_attempts} failed. Retrying in 1 second..."
                    )
                    time.sleep(1)
                    err = e
            else:
                logging.error(
                    f"Maximum attempts ({max_attempts}) reached. Exception still persists. Logging and raising..."
                )

                logging.error(err)
                raise err

        return wrapper

    return decorator


# @retry_on_exception(exceptions=[TypeError, KeyError], max_attempts=3)
@retry_on_exception(exceptions=[ZeroDivisionError, KeyError], max_attempts=3)
def risky_operation(x, y):
    # result = x + y
    result = x / y
    return result


# Testing the decorated function
try:
    result = risky_operation(10, 0)
except Exception as error:
    print(f"Caught exception: {error}")
