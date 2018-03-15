class SnakeSorter:
    def __init__(self, snakes):
	'''dasdasdsa'''
        self.snakes = snakes
        self.sorted_snakes = []

    def sort_by_weight(self):
	'''sdasdsadsadsadsa'''
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.weight)

    def sort_by_length(self):
	'''asdsadsadsada'''
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.length)
