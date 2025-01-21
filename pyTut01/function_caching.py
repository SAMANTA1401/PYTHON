import time
from functools import lru_cache
@lru_cache(maxsize=2)
def some_work(n):
    #some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now running some work")
    some_work(3)
    some_work(6)
    print("done..calling again")
    some_work(3)
    input()
    print("call again")