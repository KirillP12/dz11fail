def input_data():
    data_1 = input('\nВведите данные для справочника: ФИО и номер телефона:\n')
    with open('file.csv', 'a') as data:
        data.writelines(data_1)
        data.writelines('\n')
    return