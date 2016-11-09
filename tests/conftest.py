import pytest
from threading import Thread
from socketserver import BaseRequestHandler, TCPServer

import einder


class TestHandler(BaseRequestHandler):
    """ TestHandler mimicks a set-top box and append every request to the
    server's requests attribute.

    """
    def handle(self):
        while True:
            # Every key is 8 bytes long.
            msg = self.request.recv(8)
            self.server.requests.append(msg)


@pytest.fixture
def server(request):
    """ Return a TCPServer listening on a random port. The requests handled by
    this server are added to the list TCPServer.requests. This attribute can
    be used in tests to verify that certain request have been executed.

    """
    s = TCPServer(('127.0.0.1', 0), TestHandler)

    # All requests are added to this list.
    s.requests = []

    t = Thread(target=s.serve_forever)
    t.daemon = True
    t.start()

    def fin():
        s.stop = True
        s.server_close()

    request.addfinalizer(fin)
    return s


@pytest.yield_fixture
def client(server):
    """ Return einder.Client connected with server. """
    host, port = server.socket.getsockname()

    # Mock out authorization for now. That makes testing easier.
    einder.Client.authorize = lambda _: _
    c = einder.Client(host, port)

    yield c

    c.disconnect()
