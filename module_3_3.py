def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(3, '5', False)
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [5, False, 'str']
values_dict = {'a': 9, 'b': True, 'c': 'fsdaaf'}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [3, 'asd']
print_params(*values_list_2, 42)