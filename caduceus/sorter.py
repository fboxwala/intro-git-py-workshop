class SnakeSorter:
    def __init__(self, snakes):
    	'''Initializer for the SnakeSorter class'''
        self.snakes = snakes
        self.sorted_snakes = []

    def sort_by_weight(self):
    	'''Sort snakes by weight'''
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.weight)

    def sort_by_length(self):
    	'''Sort snakes by length'''
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.length)
