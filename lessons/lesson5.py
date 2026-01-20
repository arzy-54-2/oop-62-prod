def simple_decorator(func):
    def wrapper():
        print("перед вызовом!!")
        func()
        print("после вызово!!")
    return wrapper

# @simple_decorator
# def say_hello():
#     print("Привет!!")
#
# say_hello()
#
# @simple_decorator
# def test():
#     print('Test')
#
# test()


def greeting_decorator(func):
    def wrapper(name):
        print(f'Привет')
        func(name)
    return wrapper


@greeting_decorator
def greeting(name):
    print(f"Как дела {name}!!")

# greeting("John Doe")

def repeat_decorator(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator

@repeat_decorator(4)
def hello(name):
    print(f'Hello!! {name}')

hello()


def class_decorator(cls):
    class NewClass(cls):
        def method(self):
            print('New method!!')
    return NewClass

@class_decorator
class OldClass:
    def method(self):
        print('Old method!!')

test_obj = OldClass()

# print(type(test_obj))


def is_admin_decorator(func):
    def wrapper(user):
        if user.role == "admin":
            func()
        else:
            print('У тебя нет доступа!!')
    return wrapper

@is_admin_decorator
def ban(user):
    pass

@is_admin_decorator
def delete(user):
    pass

@is_admin_decorator
def move(user):
    pass