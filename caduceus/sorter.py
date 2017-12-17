class SnakeSorter:
    def __init__(self, snakes):
        self.snakes = snakes
        self.sorted_snakes = []

    def sort_by_weight(self):
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.weight)

    def sort_by_length(self):
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.length)


class BirdSorter:
    def __init__(self, birds):
        self.birds = birds
        self.sorted_birds = []

    def sort_by_weight(self):
        self.sorted_birds = sorted(self.birds, key=lambda bird: bird.weight)

    def sort_by_wingspan(self):
        self.sorted_birds = sorted(self.birds, key=lambda bird: bird.wingspan)
