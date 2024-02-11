def load_from_file(filename):
    """
    Loads and returns the configuration of game field from a rle-encoded
    file
    :param filename: Path to the file
    :return:
    """

    # Safely load the file contents
    try:
        with open(filename, 'r') as f:
            file_contents = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f'File at {filename} does not exit')

    output = {
        'name': 'No name',
        'author': 'No author',
        'description': 'No description',
        'parameters': {
            'x': 0,
            'y': 0,
            'b': [],
            's': [],
        },
        'pattern': [],
    }

    # Get the pattern's name
    line = file_contents[0]
    if line[0:2:1] == '#N':
        output['name'] = line[3::]

    # Gat the pattern's author
    line = file_contents[1]
    if line[0:2:1] == '#O':
        output['author'] = line[3::]

    # Get the pattern's description
    line = file_contents[2]
    if line[0:2:1] == '#C':
        output['description'] = line[3::]

    # Get the pattern's parameters
    line = file_contents[3].split(', ')
    output['parameters']['x'] = int(line[0].split()[2])
    output['parameters']['y'] = int(line[1].split()[2])

    rule = line[2].split()[2].split('/')
    output['parameters']['b'] = list(map(int, rule[0][1::1].split()))
    output['parameters']['s'] = list(map(int, rule[1][1::1].split()))

    # Get the pattern itself
    encoded_pattern = list(''.join(file_contents[4::]))
    encoded_pattern.remove('\n')
    line = []

    decoding = ''
    while encoded_pattern:
        char = encoded_pattern.pop(0)

        if char.isdigit():
            decoding += char

        if char == 'o':
            line += [1] * (int(decoding) if decoding != '' else 1)
            decoding = ''

        if char == 'b':
            line += [0] * (int(decoding) if decoding != '' else 1)
            decoding = ''

        if char == '$':
            output['pattern'].append(line)
            decoding = ''
            line = []

        if char == '!':
            if len(line) < output['parameters']['x']:
                line += [0] * (output['parameters']['x'] - len(line))

            output['pattern'].append(line)
            break

    return output


