class Snake:
    """Class for Snake objects to establish instance variables.

    Instance variables: length, weight, common_name, sci_name

    """

    def __init__(self, length, weight, common_name, sci_name):
        """Initializes a Snake object and instance variables.

        Keyword arguments:
        length -- length of the snake
        weight -- weight of the snake
        common_name -- common name of the snake
        sci_name -- scientific name of the snake

        """

        self.length = length
        self.weight = weight
        self.common_name = common_name
        self.sci_name = sci_name
