from read_csv import *


def test_read_csv():
    '''Checks to see if the file is read in and properly formatted'''
    assert read_csv('test1.csv') == [['name', 'age', 'eye colour'],
                                     ['Bob', '5', 'blue'],
                                     ['Mary', '27', 'brown'],
                                     ['Vij', '54', 'green']]
def test_read_csv2():
    assert read_csv('test2.csv') == [['species','age','location','Real'],
                                     ['Bear','35','Freddy','Y'],
                                     ['Moose','12','Grand Falls','Y'],
                                     ['Unicorn','54','Narnia','N']]

table = read_csv('test1.csv')
data = read_csv("test2.csv")

def test_header_map_1():
    '''Tests to make sure headers are properly placed into a dictionary'''
    hmap = header_map(table[0])
    assert hmap == { 'name': 0, 'age': 1, 'eye colour': 2 }

def test_header_map_2():
    '''Tests to make sure headers are properly placed into a dictionary'''
    hmap = header_map(data[0])
    assert hmap == {'species': 0, 'age': 1, 'location': 2, 'Real': 3}

def test_select_1():
    '''Tests the select method to see if select is successful in filtering rows'''
    #Fails sometimes based how python sorts the dictionary
    assert select(table,{'name','eye colour'}) == [['name', 'eye colour'],
                                                   ['Bob',  'blue'],
                                                   ['Mary', 'brown'],
                                                   ['Vij',  'green']]

def test_select_2():
    '''Tests the select method to see if select is successful in filtering rows'''
    #Fails sometimes based how python sorts the dictionary
    assert select(data,{'species','Real'}) == [['species', 'Real'], ['Bear', 'Y'], ['Moose', 'Y'], ['Unicorn', 'N']]                       

def test_row2dict():
    '''Confirms that a row can be transformed into a dictionary'''
    hmap = header_map(table[0])
    assert row2dict(hmap, table[1]) == {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}


def test_check_row():
    '''Tests to see if attributes of a row are equivalent to the conditions'''
    row = {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}
    assert check_row(row, ('age', '==', 5))
    assert not check_row(row, ('eye colour', '==', 5))
    assert check_row(row, ('eye colour', '==', 'blue'))
    assert check_row(row, ('age', '>=', 4))
    assert check_row(row, ('age', '<=', 1000))

def test_check_row2():
    '''Tests to see if attributes of a row are equivalent to the conditions'''
    row = {'name': 'Bear', 'age': '35', 'location': 'Freddy', 'Real' : 'Y'}
    assert check_row(row, ('age', '>=', 5))
    assert not check_row(row, ('location', '==', 'Grand Falls'))
    assert check_row(row, ('name', '==', 'Bear'))
    assert not check_row(row, ('Real', '==', "N"))

def test_check_row_logical():
    '''Tests to see if AND and OR work within check_row()'''
    row = {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}
    assert check_row(row, (('age', '==', 5),'OR',('eye colour', '==', 5)))
    assert not check_row(row, (('age', '==', 5),'AND',('eye colour', '==', 5)))

def test_filter_table1():
    '''Tests if a table can be properly filtered based on an input criteria '''
    assert filter_table(table,('age', '>=', 0)) == [['name', 'age', 'eye colour'],
                                                    ['Bob', '5', 'blue'],
                                                    ['Mary', '27', 'brown'],
                                                    ['Vij', '54', 'green']]

    assert filter_table(table,('age', '<=', 27)) == [['name', 'age', 'eye colour'],
                                                     ['Bob', '5', 'blue'],
                                                     ['Mary', '27', 'brown']]

    assert filter_table(table,('eye colour', '==', 'brown')) == [['name', 'age', 'eye colour'],
                                                                 ['Mary', '27', 'brown']]

    assert filter_table(table,('name', '==', 'Vij')) == [['name', 'age', 'eye colour'],
                                                         ['Vij', '54', 'green']]

def test_filter_table2():
    assert filter_table(data,('age', '>=', 0)) == [['species','age','location','Real'],
                                                    ['Bear','35','Freddy','Y'],
                                                    ['Moose','12','Grand Falls','Y'],
                                                    ['Unicorn','54','Narnia','N']]

    assert filter_table(data,('species', '==', 'Bear')) == [['species', 'age', 'location', 'Real'],
                                                         ['Bear', '35', 'Freddy', 'Y']]

def test_filter_table3():

    '''Filters table using additional AND and OR operators '''
    assert filter_table(table,(('age', '>=', 0),'AND',('age','>=','27'))) == [['name', 'age', 'eye colour'],
                                                                              ['Mary', '27', 'brown'],
                                                                              ['Vij', '54', 'green']]


    assert filter_table(table,(('age', '<=', 27),'AND',('age','>=','27'))) == [['name', 'age', 'eye colour'],
                                                                               ['Mary', '27', 'brown']]

    assert filter_table(table,(('eye colour', '==', 'brown'),
                               'OR',
                               ('name','==','Vij'))) == [['name', 'age', 'eye colour'],
                                                        ['Mary', '27', 'brown'],
                                                        ['Vij', '54', 'green']]
