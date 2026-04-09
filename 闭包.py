# 函数中的闭包
def text(func):
    def inner():
        func()
        return 2

    return inner


@text  # 调用text()  >> inner
def main():
    print('check----')
    return 10


ch = main()  # >>inner()的返回值 调用inner
print(ch)

print("*" * 50)


# 类中的闭包
def wrapper(cls):
    def inner(*args, **kwargs):
        return cls(*args, **kwargs)

    return inner


@wrapper  # 调用text()  >> inner
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('张三', 18)
print(p.name, p.age)


class Person:
    def __init__(self, score):
        self.__score = score

    def get_lock(self):
        print('get_lock---')
        return self.__score

    def set_lock(self, score):
        print('set_lock---')
        self.__score = score

    sc = property(get_lock, set_lock)


p = Person(80)
print(p.sc)
p.sc = 20
print(p.sc)

print('*'*50)
class Balance:
    def __init__(self, balance):
        self.balance = balance

    def get_money(self):
        print('get_money')
        print(f'取出的金钱：{self.balance}')
        return self.balance

    def set_money(self, balance):
        print('set_money')
        self.balance = balance

    sc = property(get_money, set_money)


balance = Balance(20)
print(balance.sc)
balance.sc = 80
print(balance.sc)
