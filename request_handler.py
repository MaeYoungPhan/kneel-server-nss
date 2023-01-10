import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_pieces, get_all_styles, get_all_metals, get_all_orders, get_all_sizes
from views import get_single_order, get_single_piece
from views import get_single_metal, get_single_size, get_single_style
from views import create_order, delete_order, update_order

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        """This method takes a single input - the path of the request - and returns a tuple."""
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /metals
        except ValueError:
            pass  # Request had trailing slash: /metals/

        return (resource, id)  # This is a tuple

    def do_GET(self):
        """Handles GET requests to the server """
        #Set the response to 'Ok'
        self._set_headers(200)
        response = {} #Default response

        #Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        #Check the path, return the correlating response
        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)

            else:
                response = get_all_metals()
        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)

            else:
                response = get_all_sizes()
        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)

            else:
                response = get_all_styles()
        elif resource == "pieces":
            if id is not None:
                response = get_single_piece(id)

            else:
                response = get_all_pieces()
        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)

            else:
                response = get_all_orders()

        #Send a JSON formatted string as a response
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """
        #Set response code to created
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        #Convert JSON string to Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Add a new order to the list
        if resource == "orders":
            #initialize new order
            new_order = None
            new_order = create_order(post_body)
            # Encode the new order and send in response
            self.wfile.write(json.dumps(new_order).encode())

#A method that handles any DELETE request.
    def do_DELETE(self):
        """Handles DELETE requests to the server"""
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single order from the list
        if resource == "orders":
            delete_order(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Update a single resource from the list
        if resource == "orders":
            update_order(id, post_body)

            # Encode the new resource and send in response
            self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()



# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
