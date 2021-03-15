def vowel_filter(function):
    def wrapper():
        res = function()
        filtered = [x for x in res if x.lower() in "aeiou"]
        return filtered
    return wrapper


# class UpperCase:
#     def say_hi(self):
#
#         @uppercase
#         def say_hi():
#             return 'hello there'
