def print_data():
    with open('file.txt', 'r') as data:
        print('\n')
        for lines in data:
            print(lines)
    return