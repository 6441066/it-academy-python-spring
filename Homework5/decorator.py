from datetime import datetime
from random import randint
from time import localtime
from time import strftime


MY_LOG_FILE = "./data5/fib.log"


# 2 --------------------------------------------------------------------------
# Создайте декоратор, который хранит результаты вызовы функции
# (за все время вызовов, не только текущий запуск программы)
def dec_logfile(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        with open(MY_LOG_FILE, "a") as f:
            f.write("Time: {}, Function: {}, number {} => {}\n".
                    format(datetime.now(), fun.__name__, args[0], result))
        return result

    return wrapper


# Write result that the function returns in log-file
@dec_logfile
# Show first n random fibonacci numbers
def funfib(n):
    f_prev = 0
    f_curr = 1
    for i in range(n - 1):
        f_prev, f_curr = f_curr, f_curr + f_prev
    return f_prev


with open(MY_LOG_FILE, "a") as f:
    f.write("Begin in " + strftime("%Y-%m-%d %H:%M:%S\n", localtime()))
for index in range(50):
    funfib(randint(1, 100))
