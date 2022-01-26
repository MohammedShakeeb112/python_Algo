import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' Completion time ' + str((end - start) * 1000) + ' milli seconds')
        return result
    return wrapper