from datetime import datetime


def loger(path):
    def loger_(some_function):
        def new_function(*args, **kwargs):
            date = datetime.now().strftime("%b %d %Y %H:%M:%S")
            name = some_function.__name__
            args_ = args
            result = some_function(*args, **kwargs)
            with open(path + '/data.txt', 'a') as file:
                file.write(f'{date} | {name} | {args_} | {result}\n')
            return result
        return new_function
    return loger_