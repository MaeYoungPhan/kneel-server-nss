SIZES = [
    {
    "id": 1,
    "carets": 0.5,
    "price": 405
    },
    {
    "id": 2,
    "carets": 0.75,
    "price": 782
    },
    {
    "id": 3,
    "carets": 1,
    "price": 1470
    },
    {
    "id": 4,
    "carets": 1.5,
    "price": 1997
    },
    {
    "id": 5,
    "carets": 2,
    "price": 3638
    }
]


def get_all_sizes():
    """Returns list of dictionaries stored in SIZES variable"""
    return SIZES


# Function with a single parameter
def get_single_size(id):
    """arg: int id, function to return a single size dictionary"""
    # Variable to hold the found size, if it exists
    requested_size = None

    # Iterate the SIZES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for size in SIZES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if size["id"] == id:
            requested_size = size

    return requested_size
