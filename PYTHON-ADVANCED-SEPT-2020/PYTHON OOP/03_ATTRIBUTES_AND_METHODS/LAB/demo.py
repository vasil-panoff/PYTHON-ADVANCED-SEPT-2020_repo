class MyClass(object):
    class_variable = 1

    def __init__(self, i_var):
        self.instance_variable = i_var

foo = MyClass(2)
bar = MyClass(3)

print(MyClass.__dict__) # {'__module__': '__main__', ... }
print(foo.__dict__)     # { 'instance_variable': 2 }
print(bar.__dict__)     # { 'instance_variable': 3 }