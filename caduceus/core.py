import csv
import sys
from .bird import Bird
from .snake import Snake
from .sorter import SnakeSorter, BirdSorter

def build_snakes(common_file, sci_file):
    '''
    Reads in the data stored in two files and builds a list of snakes
    
    Args:
        common_file: a csv file mapping common names to scientific names of snakes

        common_file structure: common name, scientific name

        sci_file: a csv file listing scientific names of snakes with lengths and weights 
    
        sci_file structure: scientific name, weight, length

    Returns: an unsorted list of Snake items
    '''
    snakes = []

    with open(common_file, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                s = Snake(0, 0, row['common name'], row['scientific name']) 
                snakes.append(s)
            except (TypeError, ValueError):
                print('Caduceus expects specific columns in csv files to work. See help(build_snakes) for the specifications')
                sys.exit()

    for snake in snakes:
        with open(sci_file, 'rb') as csvfile2:
            reader2 = csv.DictReader(csvfile2)
            for row in reader2:
                if snake.sci_name == row['scientific name']:
                    try:
                        snake.weight = int(row['weight'])
                        snake.length = int(row['length'])
                    except (TypeError, ValueError):
                        print('Caduceus expects specific columns in csv files to work. See help(build_snakes) for the specifications')
                        sys.exit()

    return snakes

def print_snakes_by_weight(snakes):
    '''
    Prints common names of snakes, one per line, sorted by weight
    Args:
        snakes: a list of Snake objects
    '''
    sorterer = SnakeSorter(snakes)
    sorterer.sort_by_weight()
    
    for snek in sorterer.sorted_snakes:
        print('{name}: {wt}g'.format(name=snek.common_name, wt=snek.weight)) 


def build_birds(common_file, sci_file):
    '''
    Reads in the data stored in two files and builds a list of birds
    
    Args:
        common_file: a csv file mapping common names to scientific names of birds

        common_file structure: common name, scientific name

        sci_file: a csv file listing scientific names of birds with weights and wingspans
    
        sci_file structure: scientific name, weight, wingspan

    Returns: an unsorted list of Bird items
    '''
    birds = []

    with open(common_file, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                b = Bird(0, 0, row['common name'], row['scientific name']) 
                birds.append(b)
            except (TypeError, ValueError):
                print('Caduceus expects specific columns in csv files to work. See help(build_birds) for the specifications')
                sys.exit()

    for bird in birds:
        with open(sci_file, 'rb') as csvfile2:
            reader2 = csv.DictReader(csvfile2)
            for row in reader2:
                if bird.sci_name == row['scientific name']:
                    try:
                        bird.weight = int(row['weight'])
                        bird.wingspan = int(row['wingspan'])
                    except (TypeError, ValueError):
                        print('Caduceus expects specific columns in csv files to work. See help(build_birds) for the specifications')
                        sys.exit()

    return birds

def print_birds_by_wingspan(birds):
    '''
    Prints common names of birds, one per line, sorted by wingspan
    
    Args:
        birds: a list of Bird objects
    '''
    sorterer = BirdSorter(birds)
    sorterer.sort_by_wingspan()
    
    for bird in sorterer.sorted_birds:
        print('{name}: {ws}cm'.format(name=bird.common_name, ws=bird.wingspan)) 
