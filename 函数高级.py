def outer(origin):
    def inner(*args, **kwargs):
        res = origin(*args, **kwargs)
        print("after")
        return res

    return inner

def outer(origin):
    def inner(*args, **kwargs)
        print()
        res = origin(*args, **kwargs)
        print()
        return res

    return inner

@outer
def func(a1):
    return a1 + "傻叉"


@outer
def base(a1, a2):
    return a1 + a2 + '傻缺'


@outer
def foo(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4 + '傻蛋'


v1 = func("1")
print(v1)

v2 = base("11","222")
print(v2)