import csv
from .snake import Snake
from .sorter import SnakeSorter

def build_snakes(common_file, sci_file):
    '''
    Reads in the data stored in two files and builds a list of snakes
    
    Args:
        common_file: a csv file mapping common names to scientific 
        names of snakes
        sci_file: a csv file listing scientific names of snakes with 
        lengths and weights 
    
    Returns: an unsorted list of Snake items
    '''
    snakes = []

    with open(common_file, 'rt') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                s = Snake(0, 0, row['common name'], row['scientific name']) 
                snakes.append(s)
            except ValueError:
                print("Caduceus expects specific columns in csv files to work.\
                See help(build_snakes) for the specifications")
    
    for snake in snakes:
        with open(sci_file, 'rt') as csvfile2:
            reader2 = csv.DictReader(csvfile2)
            for row in reader2:
                if snake.sci_name == row['scientific name']:
                    try:
                        snake.weight = int(row['weight'])
                        snake.length = int(row['length'])
                    except ValueError:
                        print("Caduceus expects specific columns in csv files \
                        to work. See help(build_snakes) for the specifications")

    return snakes

def print_snakes_by_length(snakes):
    '''
    prints common names of snakes, one per line, sorted by length
    Args:
        snakes: a list of Snake objects
    '''

    sorterer = SnakeSorter(snakes)
    sorterer.sort_by_weight()

    for snek in sorterer.sorted_snakes:
        print('{name}: {wt}cm'.format(name=snek.common_name, wt=snek.length))

def print_snakes_by_weight(snakes):
    '''
    Prints common names of snakes, one per line, sorted by weight
    Args:
        snakes: a list of Snake objects
    '''
    sorterer = SnakeSorter(snakes)
    sorterer.sort_by_weight()
    
    for snek in sorterer.sorted_snakes:
        print('{name}: {len}g'.format(name=snek.common_name, len=snek.weight)) 
