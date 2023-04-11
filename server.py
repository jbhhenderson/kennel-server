import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from repository import all, retrieve, create, update, delete

class HandleRequests(BaseHTTPRequestHandler):
   
    def do_GET(self):
        response = None
        (resource, id) = self.parse_url(self.path)

        if id is not None:
            self._set_headers(200)
            response = retrieve(resource, id)
        else:
            self._set_headers(200)
            response = all(resource)

        self.wfile.write(json.dumps(response).encode())
    

    def parse_url(self, path):
        "Test"
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        "Test"
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (type, id) = self.parse_url(self.path)

        new_resource = create(type, post_body)
        self.wfile.write(json.dumps(new_resource).encode())


    # A method that handles any PUT request.
    def do_PUT(self):
        "Test"
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (type, id) = self.parse_url(self.path)

        update(id, type, post_body)
        self.wfile.write("".encode())


    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        "Test"
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (type, id) = self.parse_url(self.path)

        delete(id, type)
        self.wfile.write("".encode())

# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()