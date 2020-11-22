class Father:
    pass

class Mother:
    pass

# class Son(Father, Mother):
#     pass
class Son:
    def __init__(self):
        self.mother = Mother()
        self.father = Father()

print(Son.__mro__)