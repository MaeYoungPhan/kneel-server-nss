from .metal_requests import get_single_metal
from .size_requests import get_single_size
from .style_requests import get_single_style
from .piece_requests import get_single_piece

ORDERS = [
    {
    "id": 1,
    "metalId": 3,
    "sizeId": 2,
    "styleId": 3,
    "pieceId": 1,
    "timestamp": 1614659931693
    },
    {
    "id": 2,
    "metalId": 2,
    "sizeId": 1,
    "styleId": 3,
    "pieceId": 2,
    "timestamp": 1614659931693
    }
]


def get_all_orders():
    """Returns list of dictionaries stored in ORDERS variable"""
    return ORDERS


# Function with a single parameter
def get_single_order(id):
    """arg: int id, function to return a single order dictionary"""
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

            matching_metal = get_single_metal(requested_order["metalId"])
            requested_order["metal"] = matching_metal

            matching_size = get_single_size(requested_order["sizeId"])
            requested_order["size"] = matching_size

            matching_style = get_single_style(requested_order["styleId"])
            requested_order["style"] = matching_style

            matching_piece = get_single_piece(requested_order["pieceId"])
            requested_order["piece"] = matching_piece

            requested_order.pop("metalId")
            requested_order.pop("sizeId")
            requested_order.pop("styleId")
            requested_order.pop("pieceId")

    return requested_order


def create_order(order):
    """Args: order (json string), returns new dictionary with id property added"""
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order


def delete_order(id):
    """Function deletes a single order by id. arg of id"""
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Iterate the ORDERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)


def update_order(id, new_order):
    """args int id, json string order, function finds order dictionary, replaces with new one """
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
