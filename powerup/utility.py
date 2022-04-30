import time
from random import randint


def get_incremented_message():
    pass


def check_pivot_number(number, pivot):
    pass


def check_balance(balance, account):
    pass


def get_encrypted_message() -> str:
    m = str(hash(time.time()))
    if len(m) == 20:
        data = m[:5] + "-" + m[5:11] + "-" + m[11:16] + "-" + m[16:20]
        return data
    else:
        d = 20 - len(m)
        for i in range(d):
            x = randint(0, 10)
            m = m + str(x)
        data = m[:5] + "-" + m[5:11] + "-" + m[11:16] + "-" + m[16:20]
        return data
