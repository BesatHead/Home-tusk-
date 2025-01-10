data_structure = [
    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure(data_structure):

    total_sum = 0
    if isinstance(data_structure, int):
        total_sum += data_structure
    elif isinstance(data_structure, str):
        total_sum += len(data_structure)
    elif isinstance(data_structure, (set, list, tuple)):
        for item in data_structure:
            total_sum += calculate_structure(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total_sum += calculate_structure(key)
            total_sum += calculate_structure(value)

    return total_sum

result = calculate_structure(data_structure)
print(result)