

from retrying import retry


def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)


@retry(retry_on_exception=retry_if_io_error)
def make_trouble():
    print("aaa")
    a = 1/0

if __name__ == '__main__':
    make_trouble()