PIECES = [
{"id": 1,
"type": "Ring"
},
{"id": 2,
"type": "Earrings"
},
{"id": 3,
"type": "Necklace"
}
]


def get_all_pieces():
        """Returns list of dictionaries stored in PIECES variable"""
        return PIECES


# Function with a single parameter
def get_single_piece(id):
    """arg: int id, function to return a single piece dictionary"""
    # Variable to hold the found piece, if it exists
    requested_piece = None

    # Iterate the PIECES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for piece in PIECES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if piece["id"] == id:
            requested_piece = piece

    return requested_piece
