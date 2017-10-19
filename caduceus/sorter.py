class SnakeSorter:
    '''
    this class has methods to sort the snakes by different variables
    '''
    def __init__(self, snakes):
        self.snakes = snakes
        self.sorted_snakes = []

    def sort_by_weight(self):
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.weight)

    def sort_by_length(self):
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.length)
