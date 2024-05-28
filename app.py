from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


#    ┌────────────────────────────────────────────────────────────────────┐
#    │                                                                    │
#    │    Find a free port                                                │
#    │                                                                    │
#    │    Flask apps usually start themselves on port 5000, but it's      │
#    │    not always free.  This code finds a free port we can use.       │
#    │                                                                    │
#    └────────────────────────────────────────────────────────────────────┘
def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))  # Bind to an available port provided by the host.
        return s.getsockname()[1]  # Return the port number assigned.


#    ┌──────────────────────────────────────────────────────────┐
#    │                                                          │
#    │    This version of the Flask launch code will            │
#    │    automatically open a browser, saving you from         │
#    │    having to click.                                      │
#    └──────────────────────────────────────────────────────────┘
if __name__ == '__main__':
    port = find_free_port()
    if os.name == 'nt':
        os.system(f'explorer "http:/127.0.0.1:{port}"')
    else:
        os.system(f'open http://127.0.0.1:{port}')
    app.run(port=port, debug=False)
