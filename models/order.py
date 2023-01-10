class Order():
    """Class initializer to create order objects"""
    # Class initializer. It has 6 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, metalId, sizeId, pieceId, timestamp):
        self.id = id
        self.metalId = metalId
        self.sizeId = sizeId
        self.pieceId = pieceId
        self.timestamp = timestamp
