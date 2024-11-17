def custom_write(file_name: str, string: list):
    strings_positions = {}
    file = open(file_name, "w", encoding="utf-8")

    for i in range(len(string)):
        _tuple = tuple((i + 1, file.tell()))
        file.write(string[i] + "\n")
        strings_positions[_tuple] = string[i]

    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)