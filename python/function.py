def sysout(msg, count):
    #doc
    'show msg * count 次'

    for i in range(0, count):
        print(str(i) + '_' + msg)
    return count**2


def fun_args(*args):
    print(*args)


def fun_args_2(**args):
    for k, v in args.items():
        print(k + '__' + v)


#closure 動態生成 function 指的事拋出去的 function 嗎?
def fun_closure(_str):
    def innerFun():
        return _str + _str

    return innerFun


res = sysout('a', 5)

print(res)

# 類似 null 的存在
a = None

#show function doc
help(sysout)

fun_args('a', 'b')
fun_args_2(a='aa', b='bb')

# closure
a = fun_closure('aaa')
b = fun_closure('bbb')

print(a())
print(b())


#lambda 匿名函式  可取代小函式
def lambda_fun(input, fun):
    for k, v in input.items():
        print(fun(k) + ':' + fun(v))

input = {'a': 'aaa', 'b': 'bbbb', 'c': 'cccc'}
lambda_fun(input, lambda a: a.capitalize() + "!")

# range
print(sum(range(1,101)))


# decorator 裝飾器
def document_it(func):
    def new_function(*args, **kwargs):
        print('function name : ', func.__name__)
        print('args : ', args)
        print('keyword arguments : ', kwargs)
        result = func(*args, **kwargs)
        print('result1 : ', result)
        return result
    return new_function

def square_it(func):
    def new_fuction(*args, **kwargs):
        result = func(*args, **kwargs)
        print('result2 : ', result)
        return result * result
    return new_fuction

@square_it
@document_it
def add_ints(a, b):
    return(a+b)

add_ints(3, 8)