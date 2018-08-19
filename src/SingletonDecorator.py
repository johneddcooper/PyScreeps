# helper_fuctions.py
# Defines a decorator that will wrap a function in an decorator that will return an existing instance of the class when instantiated.


class SingletonDecorator:
    def __init__(self, class_):
        self.class_ = class_
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.class_(*args, **kwds)
            return self.instance
