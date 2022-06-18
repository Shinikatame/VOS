def msg(file):
    with open(f'{file}', 'r', encoding = 'utf8') as file:
        return file.read()