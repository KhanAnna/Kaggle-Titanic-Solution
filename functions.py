def task_1():
    """
    Statistics of the dead/survivors separately for men and women in each class
    """
    import pandas
    data = pandas.read_csv('train.csv')
    Pclasses = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for index, row in data.iterrows():
        if row.Sex == 'male':
            if row.Survived == 0:
                Pclasses[row.Pclass - 1][0] += 1
            else:
                Pclasses[row.Pclass - 1][1] += 1
        else:
            if row.Survived == 0:
                Pclasses[row.Pclass - 1][2] += 1
            else:
                Pclasses[row.Pclass - 1][3] += 1
    for i in range(3):
        print('\nPclass:', i + 1, '\n')
        print('Men: Died - %d\tSurvived - %d' % (Pclasses[i][0], Pclasses[i][1]))
        print('Woman: Died - %d\tSurvived - %d' % (Pclasses[i][2], Pclasses[i][3]))


def task_2():
    """
    Using the panels module, we output statistics for all numeric fields, separately for men and women
    """
    import pandas
    data = pandas.read_csv('train.csv')
    print('Death/Survivor statistics for men\n\n')
    print(data[data.Sex == 'male'].describe())
    print('Death/Survivor statistics for women\n\n')
    print(data[data.Sex == 'female'].describe())


def task_3():
    """
    Shows whether the landing port affects survival
    """
    import pandas
    data = pandas.read_csv('train.csv')
    ports = ['C', 'Q', 'S']
    people = {'C': [0, 0], 'Q': [0, 0], 'S': [0, 0]}
    for index, row in data.iterrows():
        if row.Embarked not in ports:
            continue
        if row.Survived:
            people[row.Embarked][1] += 1
        else:
            people[row.Embarked][0] += 1
    survived = 0
    for v in people.values():
        survived += v[1]
    survived = [0, 0, 0]
    i = 0
    for k, v in people.items():
        survived[i] = (v[1] / (v[0] + v[1]) * 100)
        print('\nПорт', k, ':')
        print('Survived: %d\nDied: %d\nSurvival rate: %3.3f%%' % (v[1], v[0], (v[1] / (v[0] + v[1]) * 100)))
        ++i
    if not survived[0] == survived[1] == survived[2]:
        print('\nThe port of embarkation affects survival')
    else:
        print('The port of embarkation does not affect survival')


def task_4():
    """
    Output of the top 10 popular names
    """
    import pandas
    data = pandas.read_csv('train.csv')
    names = {}
    for index, row in data.iterrows():
        name = row.Name.split(',')[0]
        names[name] = names.setdefault(name, 0) + 1
    sorted_names = sorted(names.items(), key=lambda x: x[1], reverse=True)
    print('All names:', sorted_names)
    print('The ten most popular names:')
    for i in range(10):
        print(i + 1, sorted_names[i][0])


def task_5():
    """
    Fills in all missing values in train.csv with median (by column)
    """
    import pandas
    data = pandas.read_csv('train.csv')
    print('Are there empty fields in the columns:')
    print(data.isnull().any(), '\n')
    print('Cabin, Embedded - not numeric values, fill in the empty fields in Age\n')
    print(data.isnull().any())

