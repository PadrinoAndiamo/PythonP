#DEKORATORY

def uppercase(func):
    def wrapper(*args,**kwargs):
        return func(*args, **kwargs).upper()

    return wrapper
@uppercase
def foo():
    return 'bar'

@uppercase
def hello(name):
    return f'Hello {name}'

print(foo())
print(hello('Money $500$'))