def file_reader(file):
    i = 0
    g = 0
    with open(f'{file}', 'r') as file:
        b = file.readlines()
    while True:
        if i > len(b) - 1:
            break
        activate_word = yield b[i]
        if activate_word == 'next':
            i += 1
        elif activate_word == 'pervious' and i != 0:
            g = i-1
            yield g
        elif activate_word == 'pervious' and i == 0:
            yield b[0]



activator = file_reader('fole')
print(next(activator))
print(activator.send('pervious'))
print(activator.send('next'))
print(activator.send('pervious'))
print(next(activator))
print(activator.send('next'))
print(activator.send('pervious'))
print(activator.send('next'))