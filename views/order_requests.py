import sqlite3
import json
from models import Order
from .metal_requests import get_single_metal
from .size_requests import get_single_size
from .style_requests import get_single_style
from .piece_requests import get_single_piece

ORDERS = [
    {
        "id": 1,
        "metal_id": 3,
        "size_id": 2,
        "style_id": 3,
        "piece_id": 1,
        "timestamp": 1614659931693.0
    }
]

def get_all_orders():
    """Returns list of dictionaries stored in ORDERS variable"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.piece_id,
            o.timestamp
        FROM orders o
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            order = Order(row['id'], row['metal_id'], row['size_id'],
                        row['style_id'], row['piece_id'], row['timestamp'])

            orders.append(order.__dict__)

    return orders

# Function with a single parameter
def get_single_order(id):
    """arg: int id, function to return a single order dictionary"""
    #Open the connection to the server
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.piece_id,
            o.timestamp
        FROM orders o
        WHERE o.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        order = Order(data['id'], data['metal_id'], data['size_id'],
                        data['style_id'], data['piece_id'], data['timestamp'])

    return order.__dict__


def create_order(new_order):
    """Args: new_order (json string), returns new dictionary with id property added"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, size_id, style_id, piece_id, timestamp )
        VALUES
            (?, ?, ?, ?, ?);
        """, (new_order['metalId'], new_order['sizeId'], new_order['styleId'],
            new_order['pieceId'], new_order['timestamp'], ))

        id = db_cursor.lastrowid

        new_order['id'] = id

    return new_order


def delete_order(id):
    """Function deletes a single order by id. arg of id"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM orders
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    """args int id, json string order, function finds order dictionary, replaces with new one """
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
