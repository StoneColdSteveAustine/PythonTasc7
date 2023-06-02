str = input()
str_list = s.split()
tp = tuple(map(lambda x: tuple(x.split('=')), str_list))
