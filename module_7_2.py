

def custom_write(file_name, strings):
    file = open(file_name,'a',encoding='utf-8')
    strings_positions = {}
    items = ()
    counter_str =0
    for st in strings:
        counter_str += 1
        strings_positions[(f'{counter_str},{file.tell()}')] = f"{st}"
        file.write(f"{st}\n")
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