class Style():
    """Class initializer to create style objects"""
    # Class initializer. It has 3 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, style, price):
        self.id = id
        self.style = style
        self.price = price
