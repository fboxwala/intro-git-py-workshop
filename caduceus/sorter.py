class SnakeSorter:
    def __init__(self, snakes):
    '''
    Reads in the data stored in two files and builds a list of snakes
    
    Args:
        common_file: a csv file mapping common names to scientific 
        names of snakes
        sci_file: a csv file listing scientific names of snakes with 
        lengths and weights 
    
    Returns: an unsorted list of Snake items
    '''
        self.snakes = snakes
        self.sorted_snakes = []

    def sort_by_weight(self):
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.weight)

    def sort_by_length(self):
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.length)
