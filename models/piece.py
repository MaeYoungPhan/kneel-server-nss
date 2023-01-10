class Piece():
    """Class initializer to create piece objects"""
    # Class initializer. It has 2 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, type):
        self.id = id
        self.type = type
