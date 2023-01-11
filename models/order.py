class Order():
    """Class initializer to create order objects"""
    # Class initializer. It has 6 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, metal_id, size_id, piece_id, timestamp):
        self.id = id
        self.metal_id = metal_id
        self.size_id = size_id
        self.piece_id = piece_id
        self.timestamp = timestamp
