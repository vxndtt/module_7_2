def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding = 'utf-8')
    strings_positions = {}
    string_number = 0
    byte_start = file.seek(0)
    for string in strings:
        file.write(f'{string}, \n')
        string_number += 1
        key = (string_number, byte_start)
        strings_positions[key] = string
        byte_start = file.tell()
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
