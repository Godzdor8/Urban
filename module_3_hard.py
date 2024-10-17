def calculate_structure_sum(args):
    sum = 0
    for i in args:
        if isinstance(i, list) or isinstance(i, set) or isinstance(i, tuple):
            sum += calculate_structure_sum(i)
        elif isinstance(i, dict):
            sum += calculate_structure_sum(i)
            sum += calculate_structure_sum(i.values())
        elif isinstance(i, int) or isinstance(i, float):
            sum += i
        elif isinstance(i, str):
            sum += len(i)
    return sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)