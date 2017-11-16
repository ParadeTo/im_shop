class Foo(object):
    def __init__(self):
        print('init')

    def __call__(self, func):
        def _call(*args, **kw):
            print('class decorator runing')
            return func(*args, **kw)

        return _call


class classonlymethod(classmethod):
    def __get__(self, instance, cls=None):
        if instance is not None:
            raise AttributeError("This method is available only on the class, not on instances.")
        return super(classonlymethod, self).__get__(instance, cls)

class Bar(object):
    @classonlymethod
    def bar(self, test, ids):
        print('bar')


Bar.bar('a', 'a')

def f (a, b, c='c'):
    print(a, b, c)

f(1,2,3)

if 0:
    print(1)