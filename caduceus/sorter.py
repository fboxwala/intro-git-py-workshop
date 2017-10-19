class SnakeSorter:
    """Class to sort snakes.

    Instance variables:
    snakes -- snakes to be sorted
    sorted_snames -- list of sorted snakes

    Instance methods:
    sort_by_weight() -- returns snakes sorted by weight
    sort_by_length() -- returns snakes sorted by length

    """

    def __init__(self, snakes):
        """Initializes a SnakeSorter object and instance variables.

        Keyword arguments:
        snakes -- snakes to be sorted
        sorted_snames -- list of sorted snakes

        """
        self.snakes = snakes
        self.sorted_snakes = []

    def sort_by_weight(self):
        """Sorts snakes by weight and stores in sorted_snakes."""
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.weight)

    def sort_by_length(self):
        """Sorts snakes by length and stores in sorted_snakes."""
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.length)
