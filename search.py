def search_data():
    with open('file.csv', 'r') as data:
        search = input('\nВведите слово для поиска: ')
        print('\n')
        for lines in data:
            if search in lines:
                print(lines)
    return